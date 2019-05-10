from ROOT import *

f = TFile("test.root", "recreate")

h = TH1D("test", "1D",100,0,10)
h2 = TH1D("test2", "1D",100,0,10)
h3 = TH1D("test3", "1D",100,0,10)
r = TRandom()

for x in range(10000):
  h.Fill(r.Gaus()+5)
  h3.Fill(r.Gaus()+5)
for x in range(100000):
  h2.Fill(r.Exp(7))
  h3.Fill(r.Exp(7))

f.Write()


