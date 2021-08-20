#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

from src.YachtMod import Yacht, Keel, Rudder
from src.SailMod import Main, Jib, Kite
from src.VPPMod import VPP
from src.UtilsMod import VPPResults

# Values here taken form a VPRN certificate and owner measurements.
# The headsail is the self-tacking jib
# The Volume is calculated by taking the boat weight and multiplying by the 
# density of seawater (1.025)
# The wing keel is odd and not properly modelled in this VPP.
#
#
Hanse301_wing = Yacht(Name="Dragonfly hanse 301",
             Lwl=7.91,
             Vol=3.87,
             Bwl=2.38,
             Tc=0.41,
             WSA=17.92,
             Tmax=1.08,
             Amax=1.051,
             Mass=3537,
             Ff=1.0,
             Fa=1.0,
             Boa=2.74,
             Loa=8.9,
             App=[Keel(Cu=1.36, Cl=1.00, Span=1.67),
                   Rudder(Cu=0.38, Cl=0.22, Span=1.06),],
             Sails=[Main("MN1", P=11.42, E=3.87, Roach=0.1, BAD=1.0),
                    Jib("J1", I=9.61, J=3.25, LPG=4.30, HBI=0.8),
                    Kite("A2", area=64.1, vce=6.0)]
       )

vpp = VPP(Yacht=Hanse301_wing)

vpp.set_analysis(tws_range=np.arange(4.0,21.0,4.0),
                 twa_range=np.linspace(30.0,180.0,32))

vpp.run(verbose=True)
vpp.polar(n=3, save=False)
vpp.SailChart(save=True)
vpp.write('results')
