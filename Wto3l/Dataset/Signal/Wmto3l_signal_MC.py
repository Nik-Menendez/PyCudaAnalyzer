import os
from hep.cms.Dataset.CMSDataset import CMSDataset
from hep.root.TFile import TFile

input_dir = "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/"
#input_dir = "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/signal/signal_sel/"
tree_path_in_file = "passedEvents"

mass_points = [4,5,10,15,30,60]
wm_xs_dict = {
	4:  3.251,
	5:  2.352,
	10: 0.9761,
	15: 0.4916,
	30: 0.08033,
	60: 0.0009349,
	}
wp_xs_dict = {
	4:  4.223,
	5:  3.101,
	10: 1.263,
	15: 0.5126,
	30: 0.09952,
	60: 0.001245,
	}

#mass_points = [15]#,20,30,45,60]
#wm_xs_dict = {
#	15: 0.4504013, 
#	20: 0.2425901, 
#	30: 0.07259808, 
#	45: 0.00989203, 
#	60: 0.0008656826,
#	}
#epsilon = 1.0

# ____________________________________________________________________________________________________________________________________________ ||
wm_sample_dict = {}
wp_sample_dict = {}
for m in mass_points:
	wm_sample_dict[m] = CMSDataset(
		"WmTo3l_ZpM"+str(m),
		[TFile(os.path.join(input_dir,"WmTo3l_M%s.root"%str(m)),tree_path_in_file,),],
		xs = wm_xs_dict[m],
		plot_name = "WmTo3l_ZpM"+str(m),
		isSignal = True,
		)
	#wm_sample_dict[m].read_sumw_by_text_file(os.path.join(input_dir,"WmTo3l_M%s.txt"%str(m)))
	wm_sample_dict[m].sumw = 50000

	wp_sample_dict[m] = CMSDataset(
		"WpTo3l_ZpM"+str(m),
		[TFile(os.path.join(input_dir,"WpTo3l_M%s.root"%str(m)),tree_path_in_file,),],
		xs = wp_xs_dict[m],
		plot_name = "WpTo3l_ZpM"+str(m),
		isSignal = True,
		)
	#wp_sample_dict[m].read_sumw_by_text_file(os.path.join(input_dir,"WpTo3l_M%s.txt"%str(m)))
	wp_sample_dict[m].sumw = 50000
# ____________________________________________________________________________________________________________________________________________ ||

all_signal = [wm_sample_dict[4],wm_sample_dict[5],wm_sample_dict[10],wm_sample_dict[15],wm_sample_dict[30],wm_sample_dict[60],wp_sample_dict[4],wp_sample_dict[5],wp_sample_dict[10],wp_sample_dict[15],wp_sample_dict[30],wp_sample_dict[60]]
wm_signal = [wm_sample_dict[4],wm_sample_dict[5],wm_sample_dict[10],wm_sample_dict[15],wm_sample_dict[30],wm_sample_dict[60]]
wp_signal = [wp_sample_dict[4],wp_sample_dict[5],wp_sample_dict[10],wp_sample_dict[15],wp_sample_dict[30],wp_sample_dict[60]]

#wm_signal = [wm_sample_dict[15]]#,wm_sample_dict[20],wm_sample_dict[30],wm_sample_dict[45],wm_sample_dict[60],]

for m,sig in wm_sample_dict.items():
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
		#"ip3dL1",
		#"ip3dL2",
		#"ip3dL3",
		#"sip3dL1",
		#"sip3dL2",
		#"sip3dL3",
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
                ]

for m,sig in wp_sample_dict.items():
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
		#"ip3dL1",
		#"ip3dL2",
		#"ip3dL3",
		#"sip3dL1",
		#"sip3dL2",
		#"sip3dL3",
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
                ]

#for m,sig in wm_sample_dict.items():
#	sig.branches = [
#		"genWeight",
#        "sumweight",
#        "passedFullSelection",
#        "passedZXCRSelection",
#        "dataMCWeight",
#        "pileupWeight",
#        "k_qqZZ_qcd_M",
#        "k_qqZZ_ewk",
#        "idL1",
#        "idL2",
#        "idL3",
#        "pTL1",
#        "pTL2",
#        "pTL3",
#        "etaL1",
#        "etaL2",
#        "etaL3",
#        "phiL1",
#        "phiL2",
#        "phiL3",
#        "massL1",
#        "massL2",
#        "massL3",
#        "IsoL1",
#        "IsoL2",
#        "IsoL3",
#        "MomIdL1",
#        "MomIdL2",
#        "MomIdL3",
#        "met",
#        "met_phi",
#        "dR12",
#        "dR13",
#        "dR23",
#        "m3l",
#        "mt",
#		]
