import os
from hep.cms.Dataset.CMSDataset import CMSDataset
from hep.root.TFile import TFile

input_dir = "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/signal/new3"
tree_path_in_file = "passedEvents"

mass_points = [15,20,30,45,60]
wp_xs_dict = {
    15: 0.5649641,
    20: 0.3004604,
    30: 0.08894534,
    45: 0.012078543,
    60: 0.0011469974,
    }
epsilon = 1.0

# ____________________________________________________________________________________________________________________________________________ ||
wp_sample_dict = {}
for m in mass_points:
    wp_sample_dict[m] = CMSDataset(
        "WpTo3l_ZpM"+str(m),
        [TFile(os.path.join(input_dir,"WpTo3l_ZpM%s.root"%str(m)),tree_path_in_file,),],
        xs = wp_xs_dict[m]*epsilon**2,
        plot_name = "WpTo3l_ZpM"+str(m),
        isSignal = True,
        )
    wp_sample_dict[m].read_sumw_by_text_file(os.path.join(input_dir,"WpTo3l_ZpM%s.txt"%str(m)))
# ____________________________________________________________________________________________________________________________________________ ||

wp_signal = [wp_sample_dict[15],wp_sample_dict[20],wp_sample_dict[30],wp_sample_dict[45],wp_sample_dict[60],]

for m,sig in wp_sample_dict.items():
    sig.branches = [
        "genWeight",
        "sumweight",
        "passedFullSelection",
        "passedZXCRSelection",
        "dataMCWeight",
        "pileupWeight",
        "k_qqZZ_qcd_M",
        "k_qqZZ_ewk",
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
        "MomIdL1",
        "MomIdL2",
        "MomIdL3",
        "met",
        "met_phi",
        "dR12",
        "dR13",
        "dR23",
        "m3l",
        "mt",
        ]
