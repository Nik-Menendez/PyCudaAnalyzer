from Common.Dataset import Dataset
from Common.Collector import Collector

from Wto3l.Dataset.Run2017.Wto3l_MC import *
from Wto3l.Dataset.Run2017.Wto3l_Data import *
from Wto3l.Dataset.Signal.Wmto3l_signal_MC import *
from Wto3l.Dataset.Signal.Wpto3l_signal_MC import *

from hep.cms.Weighter.CrossSectionWeighter import CrossSectionWeighter
from hep.cms.Dataset.MergedCMSDataset import MergedCMSDataset
from Stat.Hist1D import Hist1D
from hep.RunPlotter.RunPlotter import RunPlotter
from hep.RunPlotter.Plot import Plot

from Wto3l.Skimmer.ZSelector import ZSelector
from Wto3l.Skimmer.Optimizer import Optimizer
from Wto3l.Skimmer.AnalysisSkimmer import SignalRegionSkimmer
from Wto3l.Weighter.DataMCWeighter import DataMCWeighter#,GPUDataMCWeighter
from Wto3l.Weighter.FakeRateWeighter import FakeRateWeighter


verbose = True
nblock = 1024
ngrid = 10
entrysteps = nblock*ngrid
namedecode = "utf-8" 
plot_data = True

if plot_data: dataset_list = bkgSamples_2017 + [data2017] + [w_sample_dict[5]]
else: dataset_list = bkgSamples_2017 + [w_sample_dict[5]] #+ w_signal
dataset_list = [w_sample_dict[4],w_sample_dict[5],w_sample_dict[10],w_sample_dict[15],w_sample_dict[30],w_sample_dict[60]]

#dataset_list = bkgSamples_2017 + [data2017] + w_signal

#dataset_list = [data2017, WZTo3LNu_2017, fake2017] + wp_signal
#dataset_list = [data2017, WZTo3LNu_2017]

#dataset_list = [data2017, fake2017, w_sample_dict[5]]

for d in dataset_list:
    d.lumi = 41.4*1000.
merged_dataset_list = [
	
	]

collector = Collector(
	#output_path = "./output/2017_MC_Background/",
	#output_path = "./output/2017_Data_Driven_Background/",
	#output_path = "./output/Fake_Rate_Calc/",
	output_path = "./output/Signal/",
	)

if plot_data:
	plots = [
		Plot("pTL1",lambda data,dataset,cfg: data["pTL1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,100.),),
		Plot("pTL2",lambda data,dataset,cfg: data["pTL2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,100.),),
		Plot("pTL3",lambda data,dataset,cfg: data["pTL3"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,100.),),
		Plot("WorstPt",lambda data,dataset,cfg: data["WorstPt"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,100.),),
		Plot("etaL1",lambda data,dataset,cfg: data["etaL1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(120,-3.,3.),),
	    Plot("etaL2",lambda data,dataset,cfg: data["etaL2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(120,-3.,3.),),
	    Plot("etaL3",lambda data,dataset,cfg: data["etaL3"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(120,-3.,3.),),
		Plot("phiL1",lambda data,dataset,cfg: data["phiL1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(40,-4.,4.),),
	    Plot("phiL2",lambda data,dataset,cfg: data["phiL2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(40,-4.,4.),),
	    Plot("phiL3",lambda data,dataset,cfg: data["phiL3"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(40,-4.,4.),),
		Plot("IsoL1",lambda data,dataset,cfg: data["IsoL1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,0.2),),
	    Plot("IsoL2",lambda data,dataset,cfg: data["IsoL2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,0.2),),
	    Plot("IsoL3",lambda data,dataset,cfg: data["IsoL3"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,0.2),),
		Plot("WorstIso",lambda data,dataset,cfg: data["WorstIso"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,0.2),),
		Plot("ip3dL1",lambda data,dataset,cfg: data["ip3dL1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,0.2),),
		Plot("ip3dL2",lambda data,dataset,cfg: data["ip3dL2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,0.2),),
		Plot("ip3dL3",lambda data,dataset,cfg: data["ip3dL3"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,0.2),),
		Plot("WorstIP",lambda data,dataset,cfg: data["WorstIP"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,0.2),),
		Plot("sip3dL1",lambda data,dataset,cfg: data["sip3dL1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,10.),),
		Plot("sip3dL2",lambda data,dataset,cfg: data["sip3dL2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,10.),),
		Plot("sip3dL3",lambda data,dataset,cfg: data["sip3dL3"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,10.),),
		Plot("WorstSIP",lambda data,dataset,cfg: data["WorstSIP"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,10.),),
		Plot("met",lambda data,dataset,cfg: data["met"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(50,0.,250.),),
		Plot("met_phi",lambda data,dataset,cfg: data["met_phi"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(40,-4.,4.),),
		Plot("dRL1L2",lambda data,dataset,cfg: data["dR12"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,6.),),
		Plot("dRL1L3",lambda data,dataset,cfg: data["dR13"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,6.),),
		Plot("dRL2L3",lambda data,dataset,cfg: data["dR23"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,6.),),
		Plot("LowestdR",lambda data,dataset,cfg: data["LowestdR"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,6.),),
		Plot("HighestdR",lambda data,dataset,cfg: data["HighestdR"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,6.),),
		Plot("SamedR",lambda data,dataset,cfg: data["SamedR"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,6.),),
		Plot("m3l",lambda data,dataset,cfg: data["m3l"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(90,0.,90.),),
		Plot("mt",lambda data,dataset,cfg: data["mt"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(200,0.,200.),),
		Plot("SameMass",lambda data,dataset,cfg: data["M0"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,100.),),
		Plot("passedDiMu",lambda data,dataset,crf: data["passedDiMu"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(2,0.,1.),),
		Plot("passedTriMu",lambda data,dataset,crf: data["passedTriMu"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(2,0.,1.),),
		]
else:
	plots = [
		Plot("mass1",lambda data,dataset,cfg: data["M1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(200,0.,80.),),
		Plot("mass2",lambda data,dataset,cfg: data["M2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(200,0.,80.),),
	]

modules = [
	CrossSectionWeighter("CrossSection"),
	ZSelector("ZSelector"),
	#Optimizer("Optimizer"),
	SignalRegionSkimmer("SignalRegion"),
	DataMCWeighter("DataMCWeighter"),
	#FakeRateWeighter("FakeRateWeighter"),
	RunPlotter("Plot",),
	]




