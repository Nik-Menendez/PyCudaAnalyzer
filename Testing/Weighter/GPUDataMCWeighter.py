import numpy as np
import pickle,os

from Common.Module import Module

import pycuda.autoinit
import pycuda.driver as drv
from pycuda.compiler import SourceModule

mod = SourceModule("""
#include <stdio.h>

__global__ void calculate(float *dest, float *xs_weight, float *selection_weight, float* dataMCWeight, float* pileupWeight, float *k_qqZZ_qcd_M, float* k_qqZZ_ewk)
{
  const int i = threadIdx.x + blockDim.x * blockIdx.x;
  dest[i] = xs_weight[i]*selection_weight[i]*dataMCWeight[i]*pileupWeight[i]*k_qqZZ_qcd_M[i]*k_qqZZ_ewk[i];
}
""")
calculate_event_weight = mod.get_function("calculate")

class GPUDataMCWeighter(Module):
    def analyze(self,data,dataset,cfg):
        if not dataset.skip_weight:
            if dataset.isMC:
                cfg.collector.event_weight = np.zeros(cfg.entrysteps).astype(np.float32)
                calculate_event_weight(
                        drv.Out(cfg.collector.event_weight),
                        drv.In(cfg.collector.xs_weight.astype(np.float32)),
                        drv.In(cfg.collector.selection_weight.astype(np.float32)),
                        drv.In(data["dataMCWeight"].astype(np.float32)),
                        drv.In(data["pileupWeight"].astype(np.float32)),
                        drv.In(data["k_qqZZ_qcd_M"].astype(np.float32)),
                        drv.In(data["k_qqZZ_ewk"].astype(np.float32)),
                        block=(cfg.nblock,1,1),
                        grid=(cfg.ngrid,1),
                        )
                cfg.collector.event_weight = cfg.collector.event_weight[:cfg.ibatch]
            else:
                cfg.collector.event_weight = np.ones(data["genWeight"].shape) * cfg.collector.selection_weight
