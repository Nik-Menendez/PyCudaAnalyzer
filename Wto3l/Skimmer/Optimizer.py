from Common.Module import Module

class Optimizer(Module):
	def __init__(self,name):
		super(Optimizer,self).__init__(name)

	def analyze(self,data,dataset,cfg):
		print(dataset)
