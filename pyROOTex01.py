from ROOT import *

f = TFile("test.root", "recreate")

h = TH1D("test", "1D",200,-5,5)
r = TRandom()

for x in range(10000):
  h.Fill(r.Gaus())

f.Write()


