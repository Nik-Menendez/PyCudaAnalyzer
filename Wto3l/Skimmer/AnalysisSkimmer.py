import numpy as np
import pickle,os

from Common.Module import Module

class SignalRegionSkimmer(Module):
	def analyze(self,data,dataset,cfg):
		cfg.collector.selection_weight = 1
		
		cfg.collector.selection_weight *= data["nMu"] == 2
		cfg.collector.selection_weight *= data["trueL3"]
		cfg.collector.selection_weight *= data["nMuons"] == 3 
		cfg.collector.selection_weight = (data["medIdL1"] * cfg.collector.selection_weight)
		cfg.collector.selection_weight = (data["medIdL2"] * cfg.collector.selection_weight)
		cfg.collector.selection_weight = (data["medIdL3"] * cfg.collector.selection_weight)
		if "Fake" in dataset.name:
			cfg.collector.selection_weight *= data["IsoL3"] >= 0.20
		else:
			cfg.collector.selection_weight *= data["IsoL3"] < 0.20
		cfg.collector.selection_weight *= data["IsoL1"] < 0.20
		cfg.collector.selection_weight *= data["IsoL2"] < 0.20
		#cfg.collector.selection_weight *= np.abs(data["etaL3"]) >= 1.4
		#cfg.collector.selection_weight *= (data["M1"] > 83.) & (data["M1"] < 97.)
		#cfg.collector.selection_weight *= data["met"] < 25.
		#cfg.collector.selection_weight *= data["dR12"] < 0.5
		#cfg.collector.selection_weight *= data["dR13"] < 0.5
		#cfg.collector.selection_weight *= data["dR23"] < 0.5
		#cfg.collector.selection_weight *= ((data["dR13"] < 0.5) | (data["dR23"] < 0.5))
		#cfg.collector.selection_weight *= (data["pTL3"] < data["pTL1"]) & (data["pTL3"] < data["pTL2"])

		cfg.collector.selection_weight *= data["pTL1"] > 20
		cfg.collector.selection_weight *= data["pTL2"] > 10
		cfg.collector.selection_weight *= data["pTL3"] > 5
		#cfg.collector.selection_weight *= (data["M1"] < 80.) | (data["M1"] > 100.)
		#cfg.collector.selection_weight *= (data["M2"] < 80.) | (data["M2"] > 100.)
		cfg.collector.selection_weight *= (data["M1"] < 8.) | (data["M1"] > 11.)
		cfg.collector.selection_weight *= (data["M2"] < 8.) | (data["M2"] > 11.)
		#cfg.collector.selection_weight *= (data["M2"] > 3.3) | (data["M2"] < 2.9)
		cfg.collector.selection_weight *= data["M2"] > 4.

		#cfg.collector.selection_weight *= data["dR23"] < 2.
		#cfg.collector.selection_weight *= data["m3l"] < 80.
		#cfg.collector.selection_weight *= (data["mt"] < 150.)
