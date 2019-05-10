from ROOT import *

gROOT.SetBatch(1)

f = TFile("test.root")

keyList = [x.GetName() for x in f.GetListOfKeys()]
hList = [f.Get(x) for x in keyList]

myFitFun = TF1("myFitFun","gaus")

for x in hList:
  x.Fit(myFitFun)
  fitR = TVirtualFitter.GetFitter()
  print fitR.GetParameter(0), fitR.GetParameter(1), fitR.GetParameter(2)
