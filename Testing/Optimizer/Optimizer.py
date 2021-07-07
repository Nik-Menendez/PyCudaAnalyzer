from __future__ import division
import numpy as np
import pandas as pd
import uproot
import matplotlib.pyplot as plt

# Choose Files to import

bkg_files = ["/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/background/signal_sel/pt/DYJetsToLL_M10To50.root",
			 "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/background/signal_sel/pt/DYJetsToLL_M50.root",
			 "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/background/signal_sel/pt/TTJets_DiLept.root",
			 "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/background/signal_sel/pt/WJetsToLNu.root",
			 "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/background/signal_sel/pt/WWTo2L2Nu.root",
			 "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/background/signal_sel/pt/WZTo3LNu.root",
			 "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/background/signal_sel/pt/ZZTo4L.root"
			 ]

sig_files = [#"/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/signal_sel/pt/Wto3l_M4.root",
			 "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/signal_sel/pt/Wto3l_M5.root",
			 #"/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/signal_sel/pt/Wto3l_M10.root",
			 #"/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/signal_sel/pt/Wto3l_M15.root",
			 #"/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/signal_sel/pt/Wto3l_M30.root",
			 #"/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/signal_sel/pt/Wto3l_M60.root"
			 ]

treename = 'passedEvents'

xs = [18610.0,6077.22,54.23,61526.7,12.178,5.052,1.369]
sumw = [39505301.0,459628904471.0,28349068.0,33043732.0,22155848.0,94563223.0,55658966.0]

# Choose variables to import and test over

vars_in = ["dR12","dR13","dR23","IsoL1","IsoL2","IsoL3","sip3dL1","sip3dL2","sip3dL3","ip3dL1","ip3dL2","ip3dL3","idL1","idL2","idL3"]
vars_test = ["LowestdR","HighestdR","SamedR","HighestIso","HighestSIP","HighestIP"]
limits_0 = np.array([0,0,0,0,0,0])
limits_1 = np.array([5,5,5,.2,10,.2])
limits_2 = np.array([500,500,500,200,1000,200])
limits_3 = np.array([0,1,1,0,0,0])

# Import files

signal = uproot.open(sig_files[0])[treename].pandas.df(vars_in)
signal["Weight"] = 5.453/500000

bkgrnd = uproot.open(bkg_files[0])[treename].pandas.df(vars_in)
bkgrnd["Weight"] = xs[0]/sumw[0]
for i in range(len(bkg_files)):
	temp_bkg = uproot.open(bkg_files[i])[treename].pandas.df(vars_in)
	temp_bkg["Weight"] = xs[i]/sumw[i]
	bkgrnd = bkgrnd.append(temp_bkg)

sig_weight = signal["Weight"].sum()
bkg_weight = bkgrnd["Weight"].sum()
print("Original sig/sqrt(bkg) = %.2f"%(sig_weight/np.sqrt(bkg_weight)))
print()

# Compute variables to test over

signal["LowestdR"] = signal[["dR12","dR13","dR23"]].min(axis=1)
bkgrnd["LowestdR"] = bkgrnd[["dR12","dR13","dR23"]].min(axis=1)

signal["HighestdR"] = signal[["dR12","dR13","dR23"]].max(axis=1)
bkgrnd["HighestdR"] = bkgrnd[["dR12","dR13","dR23"]].max(axis=1)

signal["SamedR"] = signal["dR12"]*(signal["idL1"]==signal["idL2"])+signal["dR13"]*(signal["idL1"]==signal["idL3"])+signal["dR23"]*(signal["idL2"]==signal["idL3"])
bkgrnd["SamedR"] = bkgrnd["dR12"]*(bkgrnd["idL1"]==bkgrnd["idL2"])+bkgrnd["dR13"]*(bkgrnd["idL1"]==bkgrnd["idL3"])+bkgrnd["dR23"]*(bkgrnd["idL2"]==bkgrnd["idL3"])

signal["HighestIso"] = signal[["IsoL1","IsoL2","IsoL3"]].max(axis=1)
bkgrnd["HighestIso"] = bkgrnd[["IsoL1","IsoL2","IsoL3"]].max(axis=1)

signal["HighestSIP"] = signal[["sip3dL1","sip3dL2","sip3dL3"]].max(axis=1)
bkgrnd["HighestSIP"] = bkgrnd[["sip3dL1","sip3dL2","sip3dL3"]].max(axis=1)

signal["HighestIP"] = signal[["ip3dL1","ip3dL2","ip3dL3"]].max(axis=1)
bkgrnd["HighestIP"] = bkgrnd[["ip3dL1","ip3dL2","ip3dL3"]].max(axis=1)

# Calculate optimal cuts

for i in range(len(vars_test)):
	var = vars_test[i]
	limits = np.linspace(limits_0[i],limits_1[i],num=limits_2[i],endpoint=False)
	effs = np.zeros(len(limits))
	sig_per = np.zeros(len(limits))
	bkg_per = np.zeros(len(limits))
	eff_idx = 0
	for limit in limits:
		if limits_3[i]==0:
			sig_eff = signal[(signal[var]<limit)]["Weight"].sum() #len(signal[(signal[var]<limit)])
			bkg_eff = bkgrnd[(bkgrnd[var]<limit)]["Weight"].sum() #len(bkgrnd[(bkgrnd[var]<limit)])
		else:
			sig_eff = signal[(signal[var]>limit)]["Weight"].sum() #len(signal[(signal[var]>limit)])
			bkg_eff = bkgrnd[(bkgrnd[var]>limit)]["Weight"].sum() #len(bkgrnd[(bkgrnd[var]>limit)])
		if bkg_eff!=0:
			effs[eff_idx] = sig_eff/np.sqrt(bkg_eff)
		else:
			effs[eff_idx] = -1
		sig_per[eff_idx] = sig_eff/sig_weight
		bkg_per[eff_idx] = bkg_eff/bkg_weight
		eff_idx+=1

	print(var)
	print("Best sig/sqrt(bkg) = %.2f"%(np.max(effs)))
	print("Best cut = %.4f"%(limits[np.argmax(effs)]))
	print()
	plt.plot(bkg_per,sig_per)
	plt.plot([0,1],[0,1],'--')
	plt.plot(bkg_per[np.argmax(effs)],sig_per[np.argmax(effs)],'o')
	plt.xlabel("Background Efficiency")
	plt.ylabel("Signal Efficiency")
	plt.title(var+" ROC Curve")
	plt.savefig("output/ROC/"+var+".png")
	plt.close()

