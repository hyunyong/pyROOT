from ROOT import *
gROOT.SetBatch(1)
gStyle.SetOptStat(111100)


def histMaker(name, title, binSet, xName, yName, event, tdraw, cut):
  hist = TH1D(name, title, binSet[0], binSet[1], binSet[2])
  hist.GetXaxis().SetTitle(xName)
  hist.GetYaxis().SetTitle(yName)
  hist.Sumw2()
  event.Project(name, tdraw, cut)
  c1 = TCanvas("", "", 800, 600)
  hist.Draw("Hist")
  c1.SaveAs(name+".png")
  return hist

def histMaker2D(name, title, binSet, xName, yName, event, tdraw, cut):
  hist = TH2D(name, title, binSet[0], binSet[1], binSet[2], binSet[3], binSet[4], binSet[5])
  hist.GetXaxis().SetTitle(xName)
  hist.GetYaxis().SetTitle(yName)
  hist.Sumw2()
  event.Project(name, tdraw, cut)
  c1 = TCanvas("", "", 800, 600)
  hist.Draw("colz")
  c1.SaveAs(name+".png")
  return hist

tf = TFile("GEM_test.root")
event = tf.Get("SliceTestAnalysis/MuonData")

histMaker("muonpt", "muon p_{T}", [100,20,70], "p_{T}", "number of Muon", event, "muonpt", "")
histMaker("muonphi", "muon #phi", [80,-4,4], "#phi", "number of Muon", event, "muonphi", "")
histMaker("muoneta", "muon #eta", [80,-4,4], "#eta", "number of Muon", event, "muoneta", "")
histMaker("propGE11Roll", "Muon prop. hit by Roll", [10,0,10], "Roll", "number of Muon", event, "roll_propGE11", "")
histMaker("roll_GE11", "GE11 hit by Roll", [10,0,10], "Roll", "number of Muon", event, "roll_GE11", "")
histMaker("localDxl1", "local dx l1", [100,-30,30], "dx [cm]", "number of Muon", event, "rechit_prop_dX_GE11[0]", "")
histMaker("localDxl2", "local dx l2", [100,-30,30], "dx [cm]", "number of Muon", event, "rechit_prop_dX_GE11[1]", "")
for x in range(1,9):
  histMaker("localDxl1Roll%d"%x, "local dx l1 roll %d"%x, [100,-30,30], "dx [cm]", "number of Muon", event, "rechit_prop_dX_GE11[0]", "roll_GE11[0] == %d"%x)
  histMaker("localDxl2Roll%d"%x, "local dx l2 roll %d"%x, [100,-30,30], "dx [cm]", "number of Muon", event, "rechit_prop_dX_GE11[1]", "roll_GE11[1] == %d"%x)
for x in range(1,37):
  histMaker("localDxl1Ch%d"%x, "local dx l1 chamber %d"%x, [100,-30,30], "dx [cm]", "number of Muon", event, "rechit_prop_dX_GE11[0]", "chamber_GE11[0] == %d"%x)
  histMaker("localDxl2Ch%d"%x, "local dx l2 Chamber %d"%x, [100,-30,30], "dx [cm]", "number of Muon", event, "rechit_prop_dX_GE11[1]", "chamber_GE11[1] == %d"%x)
  histMaker2D("gmeLocalHitsL1ch%d"%x, "GE11 local recHits L1 chamber %d"%x,[600,-30,30,20,0,10], "x [cm]", "roll [iEta]", event, "roll_GE11[0]:rechit_localx_GE11[0]","chamber_GE11[0] == %d"%x)
  histMaker2D("gmeLocalHitsL2%d"%x, "GE11 local recHits L2 chamber %d"%x,[600,-30,30,20,0,10], "x [cm]", "roll [iEta]", event, "roll_GE11[1]:rechit_localx_GE11[1]","chamber_GE11[0] == %d"%x)
  for y in range(1,9):
    v = {"c":x,"r":y }
    histMaker("localDxl1Ch{c}dRoll{r}".format(**v), "local dx l1 chamber {c} roll {r}".format(**v), [100,-30,30], "dx [cm]", "number of Muon", event, "rechit_prop_dX_GE11[0]", "chamber_GE11[0] == {c} && roll_GE11[0] == {r}".format(**v))
    histMaker("localDxl2Ch{c}dRoll{r}".format(**v), "local dx l2 chamber {c} roll {r}".format(**v), [100,-30,30], "dx [cm]", "number of Muon", event, "rechit_prop_dX_GE11[1]", "chamber_GE11[1] == {c} && roll_GE11[1] == {r}".format(**v))

histMaker2D("propHitsGEM", "Muon prop. hit on GE11",[800,-400,400,800,-400,400], "x [cm]", "y [cm]", event, "prop_x_GE11:prop_y_GE11","")
histMaker2D("GEMRecHits", "GE11 RecHits",[800,-400,400,800,-400,400], "x [cm]", "y [cm]", event, "rechit_x_GE11:rechit_y_GE11","")
