from ROOT import *
from array import array
gROOT.SetBatch(1)


f = TFile("testTTree.root")

tr = f.Get("pxy")

hPx = TH1D("hPx","px",100,-5,5)
hPy = TH1D("hPy","py",100,-5,5)
hPxy = TH2D("hPxy","px, py",100,-5,5,100,-5,5)

for e in tr:
  px = e.px_b
  py = e.py_b
  hPx.Fill(px)
  hPy.Fill(py)
  hPxy.Fill(px,py)

c1 = TCanvas("c1","c1",600,600)

hPx.Draw()
hPx.Fit("gaus")
c1.SaveAs("px.png")

hPy.Draw()
hPy.Fit("gaus")
c1.SaveAs("py.png")

hPxy.Draw("colz")
f2 = TF2("f2","bigaus")
hPxy.Fit(f2)
c1.SaveAs("pxy.png")


