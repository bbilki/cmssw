import FWCore.ParameterSet.Config as cms

# maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/relval/CMSSW_2_2_0/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v1/0000/0C13CE62-12B9-DD11-834C-000423D9A2AE.root',
       '/store/relval/CMSSW_2_2_0/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v1/0000/0E8561F2-75B9-DD11-A8CA-000423D996C8.root',
       '/store/relval/CMSSW_2_2_0/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v1/0000/141F01F9-75B9-DD11-95D8-000423D9890C.root',
       '/store/relval/CMSSW_2_2_0/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v1/0000/2C57B026-76B9-DD11-9D34-000423D99E46.root',
       '/store/relval/CMSSW_2_2_0/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v1/0000/3A1F5010-76B9-DD11-8659-001617C3B73A.root',
       '/store/relval/CMSSW_2_2_0/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v1/0000/42A0C797-11B9-DD11-99BD-000423D99614.root',
       '/store/relval/CMSSW_2_2_0/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v1/0000/541BE1FA-75B9-DD11-8D7D-000423D98930.root',
       '/store/relval/CMSSW_2_2_0/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v1/0000/5C9DEE5B-0FB9-DD11-B983-000423D6006E.root',
       '/store/relval/CMSSW_2_2_0/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v1/0000/64C857EB-10B9-DD11-85A7-000423D6AF24.root',
       '/store/relval/CMSSW_2_2_0/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v1/0000/666EA814-76B9-DD11-B86B-001617DBD472.root',
       '/store/relval/CMSSW_2_2_0/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v1/0000/82FA6419-76B9-DD11-A24F-000423D951D4.root',
       '/store/relval/CMSSW_2_2_0/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v1/0000/92FE5523-76B9-DD11-BB4C-001617C3B76A.root',
       '/store/relval/CMSSW_2_2_0/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v1/0000/96B20C55-76B9-DD11-9A76-001617C3B654.root',
       '/store/relval/CMSSW_2_2_0/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v1/0000/9CAFB616-76B9-DD11-A778-000423D98B5C.root',
       '/store/relval/CMSSW_2_2_0/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v1/0000/AEADC123-76B9-DD11-A1D7-001617C3B706.root',
       '/store/relval/CMSSW_2_2_0/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v1/0000/CC0FF41B-76B9-DD11-85CE-000423D6B48C.root',
       '/store/relval/CMSSW_2_2_0/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v1/0000/D0EBC618-76B9-DD11-B76E-001617E30F48.root',
       '/store/relval/CMSSW_2_2_0/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v1/0000/F0F1FD13-0FB9-DD11-A23F-000423D94494.root',
       '/store/relval/CMSSW_2_2_0/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v1/0000/F201E71F-76B9-DD11-9FB8-000423D6B42C.root',
       '/store/relval/CMSSW_2_2_0/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP_V7_v1/0000/FA3362EF-B4B9-DD11-91F1-001617E30E2C.root' ] );


secFiles.extend( [
               ] )
