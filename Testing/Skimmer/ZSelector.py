from Common.Module import Module
import uproot_methods
import math as m
import numpy as np
#import pandas as pd
#from tensorflow.keras.models import load_model
#from tensorflow.keras.backend import clear_session

class ZSelector(Module):
	def __init__(self,name):
		super(ZSelector,self).__init__(name)

		#clear_session()
		#global ZModel
		#ZModel = load_model('/blue/avery/nikmenendez/Wto3l/Analyzer/PyCudaAnalyzer/Wto3l/MVA/ZSelector_model_mass_test.h5')

	def analyze(self,data,dataset,cfg):
		cfg.collector.Met = uproot_methods.classes.TLorentzVector.PtEtaPhiMassLorentzVectorArray(data["met"],0,data["met_phi"],0)
		cfg.collector.Lep1 = uproot_methods.classes.TLorentzVector.PtEtaPhiMassLorentzVectorArray(data["pTL1"],data["etaL1"],data["phiL1"],data["massL1"])
		cfg.collector.Lep2 = uproot_methods.classes.TLorentzVector.PtEtaPhiMassLorentzVectorArray(data["pTL2"],data["etaL2"],data["phiL2"],data["massL2"])
		cfg.collector.Lep3 = uproot_methods.classes.TLorentzVector.PtEtaPhiMassLorentzVectorArray(data["pTL3"],data["etaL3"],data["phiL3"],data["massL3"])

		# Define 3 possible Zp combinations
		P1 = cfg.collector.Lep1 + cfg.collector.Lep2
		P2 = cfg.collector.Lep1 + cfg.collector.Lep3
		P3 = cfg.collector.Lep2 + cfg.collector.Lep3

		# Define 3 groups of possible combinations of muons
		data["p1"] = data["idL1"]!=data["idL2"]
		data["p2"] = data["idL1"]!=data["idL3"]
		data["p3"] = data["idL2"]!=data["idL3"]

		# --------- Define Mass1 as (not) the highest pT muon + highest pT anti-muon -------------------------------------
		#data["M1"] = (P3).mass*data["p3"] + (P2).mass*(data["p2"] & np.logical_not(data["p3"])) # pick lowest mass possible pair
		#data["M2"] = (P1).mass*data["p1"] + (P2).mass*(data["p2"] & np.logical_not(data["p1"])) # pick higher mass possible pair
		#data["M1"] = (P1).mass
		#data["M2"] = (P2).mass*data["p2"] + (P3).mass*data["p3"]
		# ----------------------------------------------------------------------------------------------------------------

		# --------- Define Mass1 as (not) the highest pT muon + highest pT anti-muon -------------------------------------
		M0 = (P1).mass*np.logical_not(data["p1"]) + (P2).mass*np.logical_not(data["p2"]) + (P3).mass*np.logical_not(data["p3"])
		M1 = (P3).mass*data["p3"] + (P2).mass*(data["p2"] & np.logical_not(data["p3"]))
		M2 = (P1).mass*data["p1"] + (P2).mass*(data["p2"] & np.logical_not(data["p1"]))
		#Zmass = 91.1876
		#Zdiff1 = np.abs(M1-Zmass)
		#Zdiff2 = np.abs(M2-Zmass)
		#Diff1C = Zdiff1 < Zdiff2
		#Diff2C = Zdiff1 > Zdiff2
		#data["M1"] = M1*Diff1C + M2*Diff2C
		#data["M2"] = M2*Diff1C + M1*Diff2C
		data["M0"] = M0
		data["M1"] = np.fmax(M1,M2) # pick higher mass possible pair
		data["M2"] = np.fmin(M1,M2) # pick lowest mass possible pair
        # ----------------------------------------------------------------------------------------------------------------

		#data["M1"] = (P1).mass
		#data["M2"] = (P1).mass

		data["isMuL1"] = (np.abs(data["idL1"]) == 13).astype(int)
		data["isMuL2"] = (np.abs(data["idL2"]) == 13).astype(int)
		#data["isMuL3"] = (np.abs(data["idL3"]) == 13).astype(int)
		data["nMu"] = data["isMuL1"] + data["isMuL2"]# + data["isMuL3"]

		IsoM1 = np.fmax(data["IsoL1"],data["IsoL2"])
		data["WorstIso"] = np.fmax(IsoM1,data["IsoL3"])
		IpM1 = np.fmax(data["ip3dL1"],data["ip3dL2"])
		data["WorstIP"] = np.fmax(IpM1,data["ip3dL3"])
		SipM1 = np.fmax(data["sip3dL1"],data["sip3dL2"])
		data["WorstSIP"] = np.fmax(SipM1,data["sip3dL3"])
		PtM1 = np.fmax(data["pTL1"],data["pTL2"])
		data["WorstPt"] = np.fmax(PtM1,data["pTL3"])
		dRM1 = np.fmin(data["dR12"],data["dR13"])
		data["LowestdR"] = np.fmin(dRM1,data["dR23"])
		dRM2 = np.fmax(data["dR12"],data["dR13"])
		data["HighestdR"] = np.fmax(dRM1,data["dR23"])
		
		data["SamedR"] = data["dR12"]*np.logical_not(data["p1"]) + data["dR13"]*np.logical_not(data["p2"]) + data["dR23"]*np.logical_not(data["p3"])


