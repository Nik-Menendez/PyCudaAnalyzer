from Common.Dataset import Dataset
from Common.Collector import Collector

from Zprime.Dataset.Run2017.SkimMC import qqZZ,ggZZ
from Zprime.Dataset.Run2017.SkimData import data2017

from hep.cms.Weighter.CrossSectionWeighter import CrossSectionWeighter

from Stat.Hist1D import Hist1D

from hep.RunPlotter.RunPlotter import RunPlotter
from hep.RunPlotter.Plot import Plot

from Zprime.Skimmer.AnalysisSkimmer import SignalRegionSkimmer
from Zprime.Weighter.DataMCWeighter import DataMCWeighter

branches = [
                "mass4l",
                "massZ1",
                "massZ2",
                "genWeight",
                "passedFullSelection",
                "dataMCWeight",
                "pileupWeight",
                "k_qqZZ_qcd_M",
                "k_qqZZ_ewk",
                "idL1",
                "idL2",
                "idL3",
                "idL4",
                ]
verbose = True
entrysteps = 1024*10
namedecode = "utf-8" 

dataset_list = [
        qqZZ,
        ggZZ,
        data2017,
        ]
for d in dataset_list:
    d.lumi = 41.7*1000.

collector = Collector(
        output_path = "./output/2020-10-12_plot_SR_Run2017_cfg/",
        )

plots = [
        Plot("mZ1",lambda data,dataset,cfg: data["massZ1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(120,0.,120.),), 
        Plot("mZ2",lambda data,dataset,cfg: data["massZ2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(60,0.,60.),), 
        Plot("m4l",lambda data,dataset,cfg: data["mass4l"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(130,70.,200.),), 
        ]

modules = [
        CrossSectionWeighter("CrossSection"),
        SignalRegionSkimmer("SignalRegion"),
        DataMCWeighter("DataMCWeighter"),
        RunPlotter("Plot",),
        ]
