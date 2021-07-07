from Common.Module import Module
import uproot_methods
import math as m
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.backend import clear_session

class ZSelector(Module):
	def __init__(self,name):
		super(ZSelector,self).__init__(name)

		clear_session()
		global ZModel
		ZModel = load_model('/blue/avery/nikmenendez/Wto3l/Analyzer/PyCudaAnalyzer/Wto3l/MVA/ZSelector_model_mass_test.h5')

	def normalize(self,df):
		mins = np.array([2.65,-2.399986,-3.141562,0.,-13.,1.33,-2.39997,-3.141574,0.,-13.,5.17,-2.399923,-3.141588,0.,-13.,.28749,-3.141591,.613,.7271,.837,0.,0.,0.,0.])
		maxs = np.array([1742.62117,2.4,3.141587,4.511298,13.,62.98735,2.399974,3.141591,9.888725,13.,135.678162,2.399995,3.141589,4.849213,13.,146.858643,3.14158,5.847,4.8885,5.28722,1.,1.,1.,1.])
		#mins = np.array([-2.399986,-3.141562,.,-13.,-2.39997,-3.141574,.,-13.,-2.399923,-3.141588,.,-13.,.28749,-3.141591,.613,.7271,.837,.,.,.,.])
		#maxs = np.array([2.4,3.141587,4.511298,13.,2.399974,3.141591,9.888725,13.,2.399995,3.141589,4.849213,13.,146.858643,3.14158,5.847,4.8885,5.28722,1.,1.,1.,1.])
		for i in range(df.size):
			df[i] = (df[i] - mins[i]) / (maxs[i] - mins[i])
		
		return df

	def analyze(self,data,dataset,cfg):
		cfg.collector.Met = uproot_methods.classes.TLorentzVector.PtEtaPhiMassLorentzVectorArray(data["met"],0,data["met_phi"],0)
		cfg.collector.Lep1 = uproot_methods.classes.TLorentzVector.PtEtaPhiMassLorentzVectorArray(data["pTL1"],data["etaL1"],data["phiL1"],data["massL1"])
		cfg.collector.Lep2 = uproot_methods.classes.TLorentzVector.PtEtaPhiMassLorentzVectorArray(data["pTL2"],data["etaL2"],data["phiL2"],data["massL2"])
		#cfg.collector.Lep3 = uproot_methods.classes.TLorentzVector.PtEtaPhiMassLorentzVectorArray(data["pTL3"],data["etaL3"],data["phiL3"],data["massL3"])

		# Define 3 possible Zp combinations
		P1 = cfg.collector.Lep1 + cfg.collector.Lep2
		#P2 = cfg.collector.Lep1 + cfg.collector.Lep3
		#P3 = cfg.collector.Lep2 + cfg.collector.Lep3

		# Define 3 groups of possible combinations of muons
		#data["p1"] = data["idL1"]!=data["idL2"]
		#data["p2"] = data["idL1"]!=data["idL3"]
		#data["p3"] = data["idL2"]!=data["idL3"]

		# --------- Define Mass1 as (not) the highest pT muon + highest pT anti-muon -------------------------------------
		#data["M1"] = (P3).mass*data["p3"] + (P2).mass*(data["p2"] & np.logical_not(data["p3"])) # pick lowest mass possible pair
		#data["M2"] = (P1).mass*data["p1"] + (P2).mass*(data["p2"] & np.logical_not(data["p1"])) # pick higher mass possible pair
		# ----------------------------------------------------------------------------------------------------------------

		# --------- Define Mass1 as (not) the highest pT muon + highest pT anti-muon -------------------------------------
		#M1 = (P3).mass*data["p3"] + (P2).mass*(data["p2"] & np.logical_not(data["p3"]))
		#M2 = (P1).mass*data["p1"] + (P2).mass*(data["p2"] & np.logical_not(data["p1"]))
		#data["M1"] = np.fmin(M1,M2) # pick lowest mass possible pair
		#data["M2"] = np.fmax(M1,M2) # pick higher mass possible pair
		data["M2"] = (P1).mass
        # ----------------------------------------------------------------------------------------------------------------

		# --------- Define Mass1 From Neural Network ---------------------------------------------------------------------
		#Selector_vars = ["pTL1","etaL1","phiL1","IsoL1","idL1",
		#				 "pTL2","etaL2","phiL2","IsoL2","idL2",
		#				 "pTL3","etaL3","phiL3","IsoL3","idL3",
		#				 "met","met_phi","dR12","dR13","dR23"]
		#df = pd.DataFrame.from_dict(data)
		#data["guess"] = np.argmax(ZModel.predict(df[Selector_vars]),axis=1)+1
		#data["g3"] = (data["guess"]//3).astype(bool)
		#data["g2"] = (data["guess"]//2).astype(bool) & ~(data["g3"])
		#data["g1"] = ~(data["g2"]) & ~(data["g3"])
		#data["M1"] = (P1).mass*data["g1"] + (P2).mass*data["g2"] + (P3).mass*data["g3"] # pick NN guess
		#data["M2"] = (P1).mass*(data["p1"] & ~(data["g1"])) + (P2).mass*(data["p2"] & ~(data["g2"])) + (P3).mass*(data["p3"] & ~(data["g3"])) # pick the possible pair NOT chosen by the NN
		# ----------------------------------------------------------------------------------------------------------------

