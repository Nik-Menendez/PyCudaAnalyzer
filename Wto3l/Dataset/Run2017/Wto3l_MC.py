import os
from hep.cms.Dataset.CMSDataset import CMSDataset
from hep.root.TFile import TFile

# ____________________________________________________________________________________________________________________________________________ ||
#input_dir = "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/"
input_dir = "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/background/signal_sel/pt/"
#input_dir = "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/NanoAOD/2017/background/control_sel/pt/"
tree_path_in_file = "passedEvents"

#sumws = [39505108.0,48655356.0,15005665.0,10536966.0]
#sumws = [37951928.0,18700012.0,100907248.0,8721088.0,20897068.0]
sumws = [39505301.0,459628904471.0,28349068.0,94563223.0,55658966.0,33043732.0,22155848.0]

sum_check = 1.0 #0.5

# ____________________________________________________________________________________________________________________________________________ ||
DYJetsToLL_M10To50_2017 = CMSDataset(
    "DYJetsToLL_M10To50",
    #[TFile(os.path.join(input_dir,"DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8.root"),tree_path_in_file,),],
	[TFile(os.path.join(input_dir,"DYJetsToLL_M10To50.root"),tree_path_in_file,),],
    xs = 18610.0, #15810.0,
    sumw = sumws[0]*sum_check,
    plot_name = "DYJetsToLL_M10To50"
    )
# ____________________________________________________________________________________________________________________________________________ ||
DYJetsToLL_M50_2017 = CMSDataset(
	"DYJetsToLL_M50",
	#[TFile(os.path.join(input_dir,"DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8.root"),tree_path_in_file,),],
	[TFile(os.path.join(input_dir,"DYJetsToLL_M50.root"),tree_path_in_file,),],
	xs = 6077.22, #6529.0,
	sumw = sumws[1]*sum_check,
	plot_name = "DYJetsToLL_M50"
	)
# ____________________________________________________________________________________________________________________________________________ ||
TTJets_2017 = CMSDataset(
	"TTJets_DiLept",
	#[TFile(os.path.join(input_dir,"TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8.root"),tree_path_in_file,),],
	[TFile(os.path.join(input_dir,"TTJets_DiLept.root"),tree_path_in_file,),],
	xs = 54.23,
	sumw = sumws[2]*sum_check,
	plot_name = "TTJets_DiLept"
	)
# ____________________________________________________________________________________________________________________________________________ ||
WZTo3LNu_2017 = CMSDataset(
	"WZTo3LNu",
	#[TFile(os.path.join(input_dir,"WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"),tree_path_in_file,),],
	[TFile(os.path.join(input_dir,"WZTo3LNu.root"),tree_path_in_file,),],
	xs = 5.052,
	sumw = sumws[3]*sum_check,
	plot_name = "WZTo3LNu"
	)
# ____________________________________________________________________________________________________________________________________________ ||
ZZTo4L_2017 = CMSDataset(
	"ZZTo4L",
    [TFile(os.path.join(input_dir,"ZZTo4L.root"),tree_path_in_file,),],
    xs = 1.369,
    sumw = sumws[4]*sum_check,
    plot_name = "ZZTo4L"
	)
# ____________________________________________________________________________________________________________________________________________ ||
WJetsToLNu_2017 = CMSDataset(
    "WJetsToLNu",
    #[TFile(os.path.join(input_dir,"WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"),tree_path_in_file,),],
    [TFile(os.path.join(input_dir,"WJetsToLNu.root"),tree_path_in_file,),],
    xs = 61526.7, #52940.0,
    sumw = sumws[5]*sum_check,
    plot_name = "WJetsToLNu"
    )
# ____________________________________________________________________________________________________________________________________________ ||
WWTo2L2Nu_2017 = CMSDataset(
    "WWTo2L2Nu",
    #[TFile(os.path.join(input_dir,"WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8.root"),tree_path_in_file,),],
    [TFile(os.path.join(input_dir,"WWTo2L2Nu.root"),tree_path_in_file,),],
    xs = 12.178,
    sumw = sumws[6]*sum_check,
    plot_name = "WWTo2L2Nu"
    )
# ____________________________________________________________________________________________________________________________________________ ||
bkgSamples_2017 = [WWTo2L2Nu_2017,ZZTo4L_2017,WJetsToLNu_2017,WZTo3LNu_2017,TTJets_2017,DYJetsToLL_M10To50_2017,DYJetsToLL_M50_2017]

for b in bkgSamples_2017:
    b.branches = [
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

#for b in bkgSamples_2017:
#    b.branches = [
#        "genWeight",
#        "sumweight",
#        "passedFullSelection",
#        "passedZXCRSelection",
#        "passedZ1LSelection",
#        "dataMCWeight",
#        "pileupWeight",
#        "k_qqZZ_qcd_M",
#        "k_qqZZ_ewk",
#        "nLeptons",
#        "nElectrons",
#        "nMuons",
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
#        "tightIdL1",
#        "tightIdL2",
#        "tightIdL3",
#        "MomIdL1",
#        "MomIdL2",
#        "MomIdL3",
#        "met",
#        "met_phi",
#        "dR12",
#        "dR13",
#        "dR23",
#        "trueL3",
#        "m3l",
#        "mt",
#                ]
