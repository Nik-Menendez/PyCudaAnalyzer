import numpy as np
import pickle,os

from Common.Module import Module

class DataMCWeighter(Module):
    def analyze(self,data,dataset,cfg):
        if not dataset.skip_weight:
            if dataset.isMC:
                cfg.collector.event_weight = cfg.collector.xs_weight * cfg.collector.selection_weight #* data["pileupWeight"]
            else:
                cfg.collector.event_weight = np.ones(data["genWeight"].shape) * cfg.collector.selection_weight
        else:
            cfg.collector.event_weight = np.ones(data["genWeight"].shape) * cfg.collector.selection_weight
