import numpy as np
import pickle,os

from Common.Module import Module

np.seterr(all='ignore')

class SignalRegionSkimmer(Module):
	def analyze(self,data,dataset,cfg):
		cfg.collector.selection_weight = 1
	
		cfg.collector.selection_weight *= data["passedDiMu"]==1

		#cfg.collector.selection_weight *= data["nMu"] == 2
		##cfg.collector.selection_weight *= data["trueL3"]
		#cfg.collector.selection_weight *= data["nMuons"] == 3 
		#cfg.collector.selection_weight = (data["tightIdL1"] * cfg.collector.selection_weight)
		#cfg.collector.selection_weight = (data["tightIdL2"] * cfg.collector.selection_weight)
		#cfg.collector.selection_weight = (data["tightIdL3"] * cfg.collector.selection_weight)
		#if "Fake" in dataset.name:
		#	cfg.collector.selection_weight *= data["IsoL3"] >= 0.20
		#else:
		#	cfg.collector.selection_weight *= data["IsoL3"] < 0.20
		#cfg.collector.selection_weight *= data["IsoL1"] < 0.20
		#cfg.collector.selection_weight *= data["IsoL2"] < 0.20
		#cfg.collector.selection_weight *= np.abs(data["etaL3"]) >= 1.4
		#cfg.collector.selection_weight *= (data["M1"] > 83.) & (data["M1"] < 97.)
		#cfg.collector.selection_weight *= data["met"] < 25.
		#cfg.collector.selection_weight *= data["dR12"] > 0.5
		#cfg.collector.selection_weight *= data["dR13"] > 0.4
		#cfg.collector.selection_weight *= data["dR23"] < 1
		#cfg.collector.selection_weight *= ((data["dR13"] < 0.5) | (data["dR23"] < 0.5))
		#cfg.collector.selection_weight *= (data["pTL3"] < data["pTL1"]) & (data["pTL3"] < data["pTL2"])

		#cfg.collector.selection_weight *= data["WorstPt"] > 20
		#cfg.collector.selection_weight *= data["pTL1"] > 23
		#cfg.collector.selection_weight *= data["pTL2"] > 13
		#cfg.collector.selection_weight *= data["pTL3"] > 8
		#cfg.collector.selection_weight *= (data["M1"] < 80.) | (data["M1"] > 100.)
		#cfg.collector.selection_weight *= (data["M2"] < 80.) | (data["M2"] > 100.)
		#cfg.collector.selection_weight *= data["M1"] < 81.
		#cfg.collector.selection_weight *= data["M2"] < 81.
		cfg.collector.selection_weight *= (data["M1"] < 8.) | (data["M1"] > 11.)
		cfg.collector.selection_weight *= (data["M2"] < 8.) | (data["M2"] > 11.)
		#cfg.collector.selection_weight *= (data["M2"] > 3.3) | (data["M2"] < 2.9)
		cfg.collector.selection_weight *= data["M1"] > 4.
		cfg.collector.selection_weight *= data["M2"] > 4.
		#cfg.collector.selection_weight *= data["M0"] > 10.

		#cfg.collector.selection_weight *= data["dR23"] < 2.
		#cfg.collector.selection_weight *= data["m3l"] < 81.
		#cfg.collector.selection_weight *= data["met"] < 70.
		#cfg.collector.selection_weight *= (data["mt"] < 150.)

		# OG 0.025
		#cfg.collector.selection_weight *= data["IsoL1"] < 0.1
		#cfg.collector.selection_weight *= data["IsoL2"] < 0.1
		#cfg.collector.selection_weight *= data["IsoL3"] < 0.1

		### OG 0.025
		#cfg.collector.selection_weight *= data["ip3dL1"] < 0.1
		#cfg.collector.selection_weight *= data["ip3dL2"] < 0.1
		#cfg.collector.selection_weight *= data["ip3dL3"] < 0.1

		### OG 3
		#cfg.collector.selection_weight *= data["sip3dL1"] < 2.
		#cfg.collector.selection_weight *= data["sip3dL2"] < 2.
		#cfg.collector.selection_weight *= data["sip3dL3"] < 2.

		cfg.collector.selection_weight *= data["WorstIso"] < 0.17 #OG 0.025
		cfg.collector.selection_weight *= data["WorstIP"] < 0.01 #OG 0.025
		cfg.collector.selection_weight *= data["WorstSIP"] < 2.72 #2. #OG 2.
		cfg.collector.selection_weight *= data["LowestdR"] < .64
		#cfg.collector.selection_weight *= data["SamedR"] > 0.66

		#if not "Data" in dataset.name:
		#	cfg.collector.selection_weight *= data["passedDiMu"]==1
