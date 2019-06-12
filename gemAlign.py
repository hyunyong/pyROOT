import ROOT, os
from DataFormats.FWLite import Events, Handle

ROOT.gROOT.SetBatch(1)

GE11RecHit = ROOT.TH2D("chamberRecHits", "recHits", 500, -25, 25,8,1,9)
GE11ClusterSize = ROOT.TH1D("clusterSize", "cluster Size", 25, 0, 25)
GE11SimResol = ROOT.TH1D("GE11SimReso", "Simresolution", 100, -5,5)
GE11Resol = ROOT.TH1D("GE11ResoRoll", "resolution", 100, -5,5)
GE11ResolRoll = []
for x in range(8):
  GE11ResolRoll.append(ROOT.TH1D("GE11ResoRoll%d"%(x+1), "resolution Roll %d"%(x+1), 100, -5,5))

gemRecHitsLabel, gemRecHits = "gemRecHits", Handle("edm::RangeMap<GEMDetId,edm::OwnVector<GEMRecHit,edm::ClonePolicy<GEMRecHit> >,edm::ClonePolicy<GEMRecHit> >")
simLabel, sim = ("g4SimHits", "MuonGEMHits", "SIM"), Handle("vector<PSimHit>")
muonsLable, muons = "muons", Handle("vector<reco::Muon>")

path = "/afs/cern.ch/user/h/hyunyong/CMSSW_10_5_0_pre2/src/"
rl = [x for x in os.listdir(".") if x.endswith(".root")]
for x in rl:
  events = Events('file:'+path+x)
  for e in events:
    #print e.eventAuxiliary().run(), e.eventAuxiliary().event()
    e.getByLabel(gemRecHitsLabel,gemRecHits)
    e.getByLabel(simLabel, sim)
    e.getByLabel(muonsLable, muons)

    if gemRecHits.isValid():
      for rh in gemRecHits.product():
        #print rh.gemId().region(), rh.gemId().station(), rh.gemId().layer(), rh.gemId().chamber(), rh.localPosition().x(), rh.gemId().roll()
        if rh.gemId().station() == 1:
          GE11RecHit.Fill(rh.localPosition().x(), rh.gemId().roll())
          GE11ClusterSize.Fill(rh.clusterSize())
          for sh in sim.product():
            if sh.detUnitId() == rh.gemId().rawId():
              simDx = sh.localPosition().x() - rh.localPosition().x()
              GE11SimResol.Fill(simDx)
              GE11ResolRoll[rh.gemId().roll()-1].Fill(simDx)
    if muons.isValid():
      for mu in muons.product():
        for chamber in mu.matches():
          for seg in chamber.gemMatches:
            if seg.gemSegmentRef.gemDetId().station()  == 1:
              dx = chamber.x - seg.gemSegmentRef.get().localPosition().x()
              GE11Resol.Fill(dx)

c1 = ROOT.TCanvas("","",800,600)
#GE11SimResol.Fit("gaus")
#GE11Resol.Fit("gaus")

GE11RecHit.Draw("colz")
c1.SaveAs(GE11RecHit.GetName()+".png")
GE11ClusterSize.Draw("Hist")
c1.SaveAs(GE11ClusterSize.GetName()+".png")
GE11SimResol.Draw("Hist")
c1.SaveAs(GE11SimResol.GetName()+".png")
for x in GE11ResolRoll:
  x.Draw("Hist")
  c1.SaveAs(x.GetName()+".png")

