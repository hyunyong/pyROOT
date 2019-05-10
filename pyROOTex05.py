from ROOT import *

gROOT.SetBatch(1)

f = TFile("test.root")

keyList = [x.GetName() for x in f.GetListOfKeys()]
hList = [f.Get(x) for x in keyList]

myFitFun = TF1("myFitFun","gaus(0)+expo(3)",0,10)
myFitFun.SetParLimits(0,0,1000)
myFitFun.SetParLimits(1,4,6)
myFitFun.SetParLimits(2,0,5)

c1 = TCanvas("c1","c1",800,600)
for x in hList:
  x.Draw()
  x.Fit(myFitFun)
  fitR = TVirtualFitter.GetFitter()
  print fitR.GetParameter(0), fitR.GetParameter(1), fitR.GetParameter(2), fitR.GetParameter(3), fitR.GetParameter(4)
  c1.SaveAs(x.GetName()+".png")
