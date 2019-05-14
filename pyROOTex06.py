from ROOT import *
from array import array

f = TFile("testTTree.root", "recreate")
tr_b = TTree("pxy", "px,py")
px = array('f', [0])
py = array('f', [0])

tr_b.Branch("px_b", px, "px_b")
tr_b.Branch("py_b", py, "py_b")
r = TRandom()
for x in range(10000):
  px[0] = r.Gaus()
  py[0] = r.Gaus()
  tr_b.Fill()

f.Write()
f.Close()

