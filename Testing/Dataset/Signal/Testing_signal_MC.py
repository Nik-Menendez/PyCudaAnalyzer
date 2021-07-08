import os
from hep.cms.Dataset.CMSDataset import CMSDataset
from hep.root.TFile import TFile

input_dir = "/afs/cern.ch/user/n/nimenend/public/"
tree_path_in_file = "passedEvents"

mass_points = [5]
w_xs_dict = {
	4:  7.474,
	5:  5.453,
	10: 2.2391,
	15: 1.0042,
	30: 0.17985,
	60: 0.0021799,
	}

# ____________________________________________________________________________________________________________________________________________ ||
w_sample_dict = {}
for m in mass_points:
	w_sample_dict[m] = CMSDataset(
		"Wto3l_ZpM"+str(m),
		[TFile(os.path.join(input_dir,"Wto3l_M%s.root"%str(m)),tree_path_in_file,),],
		xs = w_xs_dict[m]*.01,
		plot_name = "Wto3l_ZpM"+str(m),
		isSignal = True,
		)
	#wm_sample_dict[m].read_sumw_by_text_file(os.path.join(input_dir,"WmTo3l_M%s.txt"%str(m)))
	w_sample_dict[m].sumw = 500000
# ____________________________________________________________________________________________________________________________________________ ||

w_signal = [w_sample_dict[5]]

for m,sig in w_sample_dict.items():
    sig.branches = [
        "genWeight",
        "nLeptons",
        "nElectrons",
        "nMuons",
        "idL1",
        "idL2",
        "idL3",
        "pTL1",
        "pTL2",
        "pTL3",
        "etaL1",
        "etaL2",
        "etaL3",
        "phiL1",
        "phiL2",
        "phiL3",
        "massL1",
        "massL2",
        "massL3",
        "IsoL1",
        "IsoL2",
        "IsoL3",
		"ip3dL1",
		"ip3dL2",
		"ip3dL3",
		"sip3dL1",
		"sip3dL2",
		"sip3dL3",
        "tightIdL1",
        "tightIdL2",
        "tightIdL3",
        "medIdL1",
        "medIdL2",
        "medIdL3",
        "met",
        "met_phi",
        "dR12",
        "dR13",
        "dR23",
        "trueL3",
        "m3l",
        "mt",
		"passedDiMu",
		"passedTriMu",
                ]

