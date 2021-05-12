import numpy as np
import pickle,os

from Common.Module import Module

class FakeRateWeighter(Module):
	def analyze(self,data,dataset,cfg):
		if dataset.name == "ZX":
			cfg.collector.event_weight = np.ones(data["genWeight"].shape) * cfg.collector.selection_weight
			idx_3p1f = data["nFailedLeptonsZ2"] == 1
			idx_2p2f = data["nFailedLeptonsZ2"] == 2
			cfg.collector.event_weight[idx_3p1f] *= data["FRWeightProd"][idx_3p1f]
			cfg.collector.event_weight[idx_2p2f] *= -1.*data["FRWeightProd"][idx_2p2f]

		if "Fake" in dataset.name:
			#ptbins = [5,10,20,30,45,100]
			ptbins = [5,10,20,30,45,60,80,100]
			#fakerate_b = [0.47941238, 0.25981017, 0.14687288, 0.14682184, 0.24102997] # Fewer bins
			#fakerate_e = [0.59418372, 0.37545705, 0.2626037,  0.26221264, 0.43978349] # Fewer bins
			#fakerate_b = [0.47941238, 0.25981017, 0.14687288, 0.14682184, 0.20095694, 0.29208633, 0.35238095] # More bins
			#fakerate_e = [0.59418372, 0.37545705, 0.2626037,  0.26221264, 0.36705882, 0.52118644, 0.58974359] # More bins
			fakerate_b = [0.47755192, 0.25319881, 0.14168969, 0.14253394, 0.19903912, 0.28695652, 0.3492823 ] # Upsilon and JPsi veto
			fakerate_e = [0.59588139, 0.37110256, 0.25400458, 0.25421245, 0.35799523, 0.51082251, 0.58974359] # Upsilon and JPsi veto
			fakeratio_b = [0] * len(fakerate_b)
			fakeratio_e = [0] * len(fakerate_e)

			for i in range(len(fakerate_b)):
				fakeratio_b[i] = fakerate_b[i]/(1-fakerate_b[i])
				fakeratio_e[i] = fakerate_e[i]/(1-fakerate_e[i])

			pTbin  = [0] * len(fakerate_b)
			for i in range(len(pTbin)):
				pTbin[i] = (data["pTL3"] >= ptbins[i]) & (data["pTL3"] < ptbins[i+1])

			barrel = np.abs(data["etaL3"]) <= 1.4
			endcap = np.abs(data["etaL3"]) >= 1.4

			fake_weight_final_b = 0
			fake_weight_final_e = 0
			for i in range(len(fakeratio_b)):
				fake_weight_final_b += pTbin[i]*fakeratio_b[i]
				fake_weight_final_e += pTbin[i]*fakeratio_e[i]
			fake_weight_final_b = fake_weight_final_b*barrel
			fake_weight_final_e = fake_weight_final_e*endcap

			fake_weight_final = fake_weight_final_b + fake_weight_final_e
			cfg.collector.event_weight *= fake_weight_final
