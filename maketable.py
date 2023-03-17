#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 12:22:30 2023

@author: LaurasMacBook
"""

from astropy import units as u
from astropy import constants as c
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.table import Table
import numpy as np

#to make tables
#pip install tabulate

from tabulate import tabulate

#Let's start with an equatorial coordinate...
c = SkyCoord('06 23 57.10988', ' -52 41 44.3810', frame='icrs',  unit=('hour','deg'))
#Pick an observational time - 10pm at SSO is 12 UT.

obstime5 = Time('2023-4-15 08:00:00')
obstime15 = Time('2023-5-15 08:00:00')

obstime6 = Time('2023-4-15 09:00:00')
obstime16 = Time('2023-5-15 09:00:00')

obstime00 = Time('2023-4-15 10:00:00')
obstime001 = Time('2023-5-15 10:00:00')

obstime0 = Time('2023-4-15 11:00:00')
obstime01 = Time('2023-5-15 11:00:00')

obstime = Time('2023-4-15 12:00:00')
obstime1 = Time('2023-5-15 12:00:00')

obstime2 = Time('2023-4-15 13:00:00')
obstime12 = Time('2023-5-15 13:00:00')

obstime3 = Time('2023-4-15 14:00:00')
obstime13 = Time('2023-5-15 14:00:00')

obstime4 = Time('2023-4-15 15:00:00')
obstime14 = Time('2023-5-15 15:00:00')


#Find our observatory's location
obsloc5 = EarthLocation.of_site('SSO')
obsloc15 = EarthLocation.of_site('SSO')

obsloc6 = EarthLocation.of_site('SSO')
obsloc16 = EarthLocation.of_site('SSO')

obsloc00 = EarthLocation.of_site('SSO')
obsloc001 = EarthLocation.of_site('SSO')

obsloc0 = EarthLocation.of_site('SSO')
obsloc001 = EarthLocation.of_site('SSO')

obsloc = EarthLocation.of_site('SSO')
obsloc1 = EarthLocation.of_site('SSO')

obsloc2 = EarthLocation.of_site('SSO')
obsloc12 = EarthLocation.of_site('SSO')

obsloc3 = EarthLocation.of_site('SSO')
obsloc13 = EarthLocation.of_site('SSO')

obsloc4 = EarthLocation.of_site('SSO')
obsloc14 = EarthLocation.of_site('SSO')


#Let's convert to Alt-Az coords. Note that these details can be found at:
#https://docs.astropy.org/en/stable/generated/examples/coordinates/plot_obs-planning.html
c_altaz5 = c.transform_to(AltAz(obstime=obstime5,location=obsloc))
c_altaz15 = c.transform_to(AltAz(obstime=obstime15,location=obsloc1))

c_altaz6 = c.transform_to(AltAz(obstime=obstime6,location=obsloc))
c_altaz16 = c.transform_to(AltAz(obstime=obstime16,location=obsloc1))

c_altaz00 = c.transform_to(AltAz(obstime=obstime00,location=obsloc))
c_altaz001 = c.transform_to(AltAz(obstime=obstime001,location=obsloc1))

c_altaz0 = c.transform_to(AltAz(obstime=obstime0,location=obsloc))
c_altaz01 = c.transform_to(AltAz(obstime=obstime01,location=obsloc1))

c_altaz = c.transform_to(AltAz(obstime=obstime,location=obsloc))
c_altaz1 = c.transform_to(AltAz(obstime=obstime1,location=obsloc1))

c_altaz2 = c.transform_to(AltAz(obstime=obstime2,location=obsloc))
c_altaz12 = c.transform_to(AltAz(obstime=obstime12,location=obsloc1))

c_altaz3 = c.transform_to(AltAz(obstime=obstime3,location=obsloc))
c_altaz13 = c.transform_to(AltAz(obstime=obstime13,location=obsloc1))

c_altaz4 = c.transform_to(AltAz(obstime=obstime4,location=obsloc))
c_altaz14 = c.transform_to(AltAz(obstime=obstime14,location=obsloc1))


table = [['Month', 'Time', 'Altitude (degs)', 'Azimuth (degs)'], 
         ['April', '6pm','{:.2f}'.format(c_altaz5.alt),'{:.2f}'.format(c_altaz5.az) ], 
         ['May', '6pm', '{:.2f}'.format(c_altaz15.alt),'{:.2f}'.format(c_altaz15.az)], 
         ['April', '7pm','{:.2f}'.format(c_altaz6.alt),'{:.2f}'.format(c_altaz6.az) ], 
         ['May', '7pm', '{:.2f}'.format(c_altaz16.alt),'{:.2f}'.format(c_altaz16.az)], 
         ['April', '8pm', '{:.2f}'.format(c_altaz00.alt),'{:.2f}'.format(c_altaz00.az) ], 
         ['May', '8pm', '{:.2f}'.format(c_altaz001.alt),'{:.2f}'.format(c_altaz001.az)],
         ['April', '9pm', '{:.2f}'.format(c_altaz0.alt),'{:.2f}'.format(c_altaz0.az) ], 
         ['May', '9pm', '{:.2f}'.format(c_altaz01.alt),'{:.2f}'.format(c_altaz01.az)],
         ['April', '10pm', '{:.2f}'.format(c_altaz.alt),'{:.2f}'.format(c_altaz.az) ], 
         ['May', '10pm', '{:.2f}'.format(c_altaz1.alt),'{:.2f}'.format(c_altaz1.az)],  
         ['April', '11pm', '{:.2f}'.format(c_altaz2.alt),'{:.2f}'.format(c_altaz2.az)], 
         ['May', '11pm', '{:.2f}'.format(c_altaz12.alt),'{:.2f}'.format(c_altaz12.az)],
         ['April', '12am','{:.2f}'.format(c_altaz3.alt),'{:.2f}'.format(c_altaz3.az)], 
         ['May', '12am', '{:.2f}'.format(c_altaz13.alt),'{:.2f}'.format(c_altaz13.az)],
         ['April', '1am','{:.2f}'.format(c_altaz4.alt),'{:.2f}'.format(c_altaz4.az) ], 
         ['May', '1am', '{:.2f}'.format(c_altaz14.alt),'{:.2f}'.format(c_altaz14.az)], 
         ]
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

#Now write to a csv file:
dat = Table(np.array(table[1:]), names=table[0])
dat.write('star_altaz.csv', format='ascii.csv', overwrite=True)


#12 47 43.26877 -59 41 19.5792 betcru
#obstime = Time('2019-9-02 12:00:00')
#06 45 08.91728 -16 42 58.0171 sirius
#06 23 57.10988 -52 41 44.3810 canopus
#01 37 42.84548 -57 14 12.3101 a
#22 57 39.04625 -29 37 20.0533 formalhaut
#05 14 32.27210 -08 12 05.8981 rigel
#18 24 10.31840 -34 23 04.6193 esgr
#17 37 19.12985 -42 59 52.1808 sargas
#20 21 42.27678 -56 53 50.1058 apav
