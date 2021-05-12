from Common.Dataset import Dataset
from Common.Collector import Collector

from Wto3l.Dataset.Run2017.Wto3l_MC import *
from Wto3l.Dataset.Run2017.Wto3l_Data import *
from Wto3l.Dataset.Signal.Wmto3l_signal_MC import *
#from Wto3l.Dataset.Signal.Wpto3l_signal_MC import *

from hep.cms.Weighter.CrossSectionWeighter import CrossSectionWeighter
from hep.cms.Dataset.MergedCMSDataset import MergedCMSDataset
from Stat.Hist1D import Hist1D
from hep.RunPlotter.RunPlotter import RunPlotter
from hep.RunPlotter.Plot import Plot

from Wto3l.Skimmer.ZSelector import ZSelector
from Wto3l.Skimmer.AnalysisSkimmer import SignalRegionSkimmer
from Wto3l.Weighter.DataMCWeighter import DataMCWeighter#,GPUDataMCWeighter
from Wto3l.Weighter.FakeRateWeighter import FakeRateWeighter


verbose = True
nblock = 1024
ngrid = 10
entrysteps = nblock*ngrid
namedecode = "utf-8" 
plot_data = False

if plot_data: dataset_list = bkgSamples_2017 + [data2017]
else: dataset_list = bkgSamples_2017 + all_signal + [data2017]

#dataset_list = [data2017, WZTo3LNu_2017, fake2017]
#dataset_list = [data2017, WZTo3LNu_2017]

for d in dataset_list:
    d.lumi = 41.7*1000.
merged_dataset_list = [
	
	]

collector = Collector(
	#output_path = "./output/2017_MC_Background/",
	#output_path = "./output/2017_Data_Driven_Background/",
	#output_path = "./output/Fake_Rate_Calc/",
	output_path = "./output/signal/",
	)

plots = [
	Plot("pTL1",lambda data,dataset,cfg: data["pTL1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,100.),),
	Plot("pTL2",lambda data,dataset,cfg: data["pTL2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,100.),),
	Plot("pTL3",lambda data,dataset,cfg: data["pTL3"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,100.),),
	Plot("etaL1",lambda data,dataset,cfg: data["etaL1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(120,-3.,3.),),
    Plot("etaL2",lambda data,dataset,cfg: data["etaL2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(120,-3.,3.),),
    Plot("etaL3",lambda data,dataset,cfg: data["etaL3"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(120,-3.,3.),),
	Plot("phiL1",lambda data,dataset,cfg: data["phiL1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(40,-4.,4.),),
    Plot("phiL2",lambda data,dataset,cfg: data["phiL2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(40,-4.,4.),),
    Plot("phiL3",lambda data,dataset,cfg: data["phiL3"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(40,-4.,4.),),
	Plot("IsoL1",lambda data,dataset,cfg: data["IsoL1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(20,0.,0.5),),
    Plot("IsoL2",lambda data,dataset,cfg: data["IsoL2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(20,0.,0.5),),
    Plot("IsoL3",lambda data,dataset,cfg: data["IsoL3"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(20,0.,0.5),),
	Plot("met",lambda data,dataset,cfg: data["met"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(50,0.,250.),),
	Plot("met_phi",lambda data,dataset,cfg: data["met_phi"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(40,-4.,4.),),
	Plot("dRL1L2",lambda data,dataset,cfg: data["dR12"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,6.),),
	Plot("dRL1L3",lambda data,dataset,cfg: data["dR13"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,6.),),
	Plot("dRL2L3",lambda data,dataset,cfg: data["dR23"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,6.),),
	Plot("m3l",lambda data,dataset,cfg: data["m3l"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,200.),),
	Plot("mt",lambda data,dataset,cfg: data["mt"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,200.),),
	Plot("mass1",lambda data,dataset,cfg: data["M1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(200,0.,200.),),
	Plot("mass2",lambda data,dataset,cfg: data["M2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(200,0.,200.),),
	]

modules = [
	CrossSectionWeighter("CrossSection"),
	ZSelector("ZSelector"),
	SignalRegionSkimmer("SignalRegion"),
	DataMCWeighter("DataMCWeighter"),
	FakeRateWeighter("FakeRateWeighter"),
	RunPlotter("Plot",),
	]




