import os

from hep.cms.Dataset.CMSDataset import CMSDataset
from hep.root.TFile import TFile

# ______________________________________________________________________ ||
#input_dir	= "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/data2017/new_dimu/"
#input_dir   = "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/Di_Muon/"
input_dir 	= "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/data/"
tree_path_in_file = "passedEvents"

# ______________________________________________________________________ ||
data2017 = CMSDataset(
        "Data2017",
        [TFile(os.path.join(input_dir,"total_data_no_dupe.root"),tree_path_in_file,),],
        isMC = False,
        )

fake2017 = CMSDataset(
        "Fake_Weight_Data2017",
        [TFile(os.path.join(input_dir,"total_data_no_dupe.root"),tree_path_in_file,),],
        isMC = True,
		skip_weight = True,
        )
# ____________________________________________________________________________________________________________________________________________ ||
datas = [data2017,fake2017]

for d in datas:
    d.branches = [
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

#for d in datas:
#	d.branches = [
#		"genWeight",
#		"sumweight",
#		"passedFullSelection",
#		"passedZXCRSelection",
#    	"dataMCWeight",
#		"pileupWeight",
#		"k_qqZZ_qcd_M",
#		"k_qqZZ_ewk",
#		"nLeptons",
#		"nElectrons",
#		"nMuons",
#		"idL1",
#		"idL2",
#		"idL3",
#		"pTL1",
#		"pTL2",
#		"pTL3",
#		"etaL1",
#		"etaL2",
#		"etaL3",
#		"phiL1",
#		"phiL2",
#		"phiL3",
#		"massL1",
#		"massL2",
#		"massL3",
#		"IsoL1",
#		"IsoL2",
#		"IsoL3",
#		"tightIdL1",
#		"tightIdL2",
#		"tightIdL3",
#		"MomIdL1",
#		"MomIdL2",
#		"MomIdL3",
#		"met",
#		"met_phi",
#		"dR12",
#		"dR13",
#		"dR23",
#		"trueL3",
#		"m3l",
#		"mt",
#		]
