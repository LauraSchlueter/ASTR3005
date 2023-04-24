#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 12:22:30 2023

@author: LaurasMacBook
"""

from astropy import units as u
from astropy import constants as c
from astropy.coordinates import SkyCoord
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz

#to make tables
#pip install tabulate

from tabulate import tabulate

#Let's start with an equatorial coordinate...
c = SkyCoord('12 47 43.26877', ' -59 41 19.5792', frame='icrs',  unit=('hour','deg'))
#Pick an observational time - 10pm at SSO is 12 UT.

obstime5 = Time('2023-5-15 08:00:00')
obstime15 = Time('2023-6-15 08:00:00')

obstime_six_thirty = Time('2023-5-15 08:30:00')
obstime1_six_thirty = Time('2023-6-15 08:30:00')

obstime6 = Time('2023-5-15 09:00:00')
obstime16 = Time('2023-6-15 09:00:00')

obstime_seven_thirty = Time('2023-5-15 09:30:00')
obstime1_seven_thirty = Time('2023-6-15 09:30:00')

obstime00 = Time('2023-5-15 10:00:00')
obstime001 = Time('2023-6-15 10:00:00')

obstime_eight_thirty = Time('2023-5-15 10:30:00')
obstime1_eight_thirty = Time('2023-6-15 10:30:00')

obstime0 = Time('2023-5-15 11:00:00')
obstime01 = Time('2023-6-15 11:00:00')

obstime_nine_thirty = Time('2023-5-15 11:30:00')
obstime1_nine_thirty = Time('2023-6-15 11:30:00')

obstime = Time('2023-5-15 12:00:00')
obstime1 = Time('2023-6-15 12:00:00')

obstime_ten_thirty = Time('2023-5-15 12:30:00')
obstime1_ten_thirty = Time('2023-6-15 12:30:00')

obstime2 = Time('2023-5-15 13:00:00')
obstime12 = Time('2023-6-15 13:00:00')

obstime_eleven_thirty = Time('2023-5-15 13:30:00')
obstime1_eleven_thirty = Time('2023-6-15 13:30:00')

obstime3 = Time('2023-5-15 14:00:00')
obstime13 = Time('2023-6-15 14:00:00')

obstime_twelve_thirty = Time('2023-5-15 14:30:00')
obstime1_twelve_thirty = Time('2023-6-15 14:30:00')

obstime4 = Time('2023-5-15 15:00:00')
obstime14 = Time('2023-6-15 15:00:00')

obstime_thir_thirty = Time('2023-5-15 15:30:00')
obstime1_thir_thirty = Time('2023-6-15 15:30:00')

obstime7 = Time('2023-5-15 16:00:00')
obstime17 = Time('2023-6-15 16:00:00')


#Find our observatory's location
obsloc5 = EarthLocation.of_site('SSO')
obsloc15 = EarthLocation.of_site('SSO')

obsloc_six_thirty = EarthLocation.of_site('SSO')
obsloc1_six_thirty = EarthLocation.of_site('SSO')

obsloc6 = EarthLocation.of_site('SSO')
obsloc16 = EarthLocation.of_site('SSO')

obsloc_seven_thirty = EarthLocation.of_site('SSO')
obsloc1_seven_thirty = EarthLocation.of_site('SSO')

obsloc00 = EarthLocation.of_site('SSO')
obsloc001 = EarthLocation.of_site('SSO')

obsloc_eight_thirty = EarthLocation.of_site('SSO')
obsloc1_eight_thirty = EarthLocation.of_site('SSO')

obsloc0 = EarthLocation.of_site('SSO')
obsloc001 = EarthLocation.of_site('SSO')

obsloc_nine_thirty = EarthLocation.of_site('SSO')
obsloc1_nine_thirty = EarthLocation.of_site('SSO')

obsloc = EarthLocation.of_site('SSO')
obsloc1 = EarthLocation.of_site('SSO')

obsloc_ten_thirty = EarthLocation.of_site('SSO')
obsloc1_ten_thirty = EarthLocation.of_site('SSO')

obsloc2 = EarthLocation.of_site('SSO')
obsloc12 = EarthLocation.of_site('SSO')

obsloc_eleven_thirty = EarthLocation.of_site('SSO')
obsloc1_eleven_thirty = EarthLocation.of_site('SSO')

obsloc3 = EarthLocation.of_site('SSO')
obsloc13 = EarthLocation.of_site('SSO')

obsloc_twelve_thirty = EarthLocation.of_site('SSO')
obsloc1_twelve_thirty = EarthLocation.of_site('SSO')

obsloc4 = EarthLocation.of_site('SSO')
obsloc14 = EarthLocation.of_site('SSO')

obsloc_thir_thirty = EarthLocation.of_site('SSO')
obsloc1_thir_thirty = EarthLocation.of_site('SSO')

obsloc7 = EarthLocation.of_site('SSO')
obsloc17 = EarthLocation.of_site('SSO')


#Let's convert to Alt-Az coords. Note that these details can be found at:
#https://docs.astropy.org/en/stable/generated/examples/coordinates/plot_obs-planning.html
c_altaz5 = c.transform_to(AltAz(obstime=obstime5,location=obsloc))
c_altaz15 = c.transform_to(AltAz(obstime=obstime15,location=obsloc1))

c_altaz_six_thirty = c.transform_to(AltAz(obstime=obstime_six_thirty,location=obsloc))
c_altaz1_six_thirty = c.transform_to(AltAz(obstime=obstime1_six_thirty,location=obsloc1))

c_altaz6 = c.transform_to(AltAz(obstime=obstime6,location=obsloc))
c_altaz16 = c.transform_to(AltAz(obstime=obstime16,location=obsloc1))

c_altaz_seven_thirty = c.transform_to(AltAz(obstime=obstime_seven_thirty,location=obsloc))
c_altaz1_seven_thirty = c.transform_to(AltAz(obstime=obstime1_seven_thirty,location=obsloc1))

c_altaz00 = c.transform_to(AltAz(obstime=obstime00,location=obsloc))
c_altaz001 = c.transform_to(AltAz(obstime=obstime001,location=obsloc1))

c_altaz_eight_thirty = c.transform_to(AltAz(obstime=obstime_eight_thirty,location=obsloc))
c_altaz1_eight_thirty = c.transform_to(AltAz(obstime=obstime1_eight_thirty,location=obsloc1))

c_altaz0 = c.transform_to(AltAz(obstime=obstime0,location=obsloc))
c_altaz01 = c.transform_to(AltAz(obstime=obstime01,location=obsloc1))

c_altaz_nine_thirty = c.transform_to(AltAz(obstime=obstime_nine_thirty,location=obsloc))
c_altaz1_nine_thirty = c.transform_to(AltAz(obstime=obstime1_nine_thirty,location=obsloc1))

c_altaz = c.transform_to(AltAz(obstime=obstime,location=obsloc))
c_altaz1 = c.transform_to(AltAz(obstime=obstime1,location=obsloc1))

c_altaz_ten_thirty = c.transform_to(AltAz(obstime=obstime_ten_thirty,location=obsloc))
c_altaz1_ten_thirty = c.transform_to(AltAz(obstime=obstime1_ten_thirty,location=obsloc1))

c_altaz2 = c.transform_to(AltAz(obstime=obstime2,location=obsloc))
c_altaz12 = c.transform_to(AltAz(obstime=obstime12,location=obsloc1))

c_altaz_eleven_thirty = c.transform_to(AltAz(obstime=obstime_eleven_thirty,location=obsloc))
c_altaz1_eleven_thirty = c.transform_to(AltAz(obstime=obstime1_eleven_thirty,location=obsloc1))

c_altaz3 = c.transform_to(AltAz(obstime=obstime3,location=obsloc))
c_altaz13 = c.transform_to(AltAz(obstime=obstime13,location=obsloc1))

c_altaz_twelve_thirty = c.transform_to(AltAz(obstime=obstime_twelve_thirty,location=obsloc))
c_altaz1_twelve_thirty = c.transform_to(AltAz(obstime=obstime1_twelve_thirty,location=obsloc1))

c_altaz4 = c.transform_to(AltAz(obstime=obstime4,location=obsloc))
c_altaz14 = c.transform_to(AltAz(obstime=obstime14,location=obsloc1))

c_altaz_thir_thirty = c.transform_to(AltAz(obstime=obstime_thir_thirty,location=obsloc))
c_altaz1_thir_thirty = c.transform_to(AltAz(obstime=obstime1_thir_thirty,location=obsloc1))

c_altaz7 = c.transform_to(AltAz(obstime=obstime7,location=obsloc))
c_altaz17 = c.transform_to(AltAz(obstime=obstime17,location=obsloc1))


table = [['Month', 'Time', 'Altitude (degs)', 'Azimuth (degs)'], 
         ['May', '6pm','{:.2f}'.format(c_altaz5.alt),'{:.2f}'.format(c_altaz5.az) ], 
         ['June', '6pm', '{:.2f}'.format(c_altaz15.alt),'{:.2f}'.format(c_altaz15.az)], 
         ['May', '7pm','{:.2f}'.format(c_altaz6.alt),'{:.2f}'.format(c_altaz6.az) ], 
         ['June', '7pm', '{:.2f}'.format(c_altaz16.alt),'{:.2f}'.format(c_altaz16.az)], 
         ['May', '8pm', '{:.2f}'.format(c_altaz00.alt),'{:.2f}'.format(c_altaz00.az) ], 
         ['June', '8pm', '{:.2f}'.format(c_altaz001.alt),'{:.2f}'.format(c_altaz001.az)],
         ['May', '9pm', '{:.2f}'.format(c_altaz0.alt),'{:.2f}'.format(c_altaz0.az) ], 
         ['June', '9pm', '{:.2f}'.format(c_altaz01.alt),'{:.2f}'.format(c_altaz01.az)],
         ['May', '10pm', '{:.2f}'.format(c_altaz.alt),'{:.2f}'.format(c_altaz.az) ], 
         ['June', '10pm', '{:.2f}'.format(c_altaz1.alt),'{:.2f}'.format(c_altaz1.az)],  
         ['May', '11pm', '{:.2f}'.format(c_altaz2.alt),'{:.2f}'.format(c_altaz2.az)], 
         ['June', '11pm', '{:.2f}'.format(c_altaz12.alt),'{:.2f}'.format(c_altaz12.az)],
         ['May', '12am','{:.2f}'.format(c_altaz3.alt),'{:.2f}'.format(c_altaz3.az)], 
         ['June', '12am', '{:.2f}'.format(c_altaz13.alt),'{:.2f}'.format(c_altaz13.az)],
         ['May', '1am','{:.2f}'.format(c_altaz4.alt),'{:.2f}'.format(c_altaz4.az) ], 
         ['June', '1am', '{:.2f}'.format(c_altaz14.alt),'{:.2f}'.format(c_altaz14.az)], 
         ['May', '2am','{:.2f}'.format(c_altaz7.alt),'{:.2f}'.format(c_altaz7.az) ], 
         ['June', '2am', '{:.2f}'.format(c_altaz17.alt),'{:.2f}'.format(c_altaz17.az)], 
         ]
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

#12 47 43.26877 -59 41 19.5792 betcru
#06 45 08.91728 -16 42 58.0171 sirius
#06 23 57.10988 -52 41 44.3810 canopus
#01 37 42.84548 -57 14 12.3101 a
#22 57 39.04625 -29 37 20.0533 formalhaut
#05 14 32.27210 -08 12 05.8981 rigel
#18 24 10.31840 -34 23 04.6193 esgr
#17 37 19.12985 -42 59 52.1808 sargas
#20 21 42.27678 -56 53 50.1058 apav
#02 19 20.79210 -02 58 39.4956 omicron ceti
#09 47 33.4839808805 +11 25 43.823283729 R Leonis
#13 49 02.0018313132 -28 22 03.532006894 W Hydrae
#04 36 45.59127 -62 04 37.7974 R Doradus

#plot velocity vs time with 30min difference

azimuths_m=[c_altaz5.az.degree,c_altaz_six_thirty.az.degree,c_altaz6.az.degree, c_altaz_seven_thirty.az.degree,c_altaz00.az.degree,  c_altaz_eight_thirty.az.degree,c_altaz0.az.degree,  c_altaz_nine_thirty.az.degree,c_altaz.az.degree,  c_altaz_ten_thirty.az.degree,c_altaz2.az.degree,  c_altaz_eleven_thirty.az.degree,c_altaz3.az.degree,  c_altaz_twelve_thirty.az.degree,c_altaz4.az.degree,  c_altaz_thir_thirty.az.degree,c_altaz7.az.degree]

azimuths_j=[c_altaz15.az.degree,c_altaz1_six_thirty.az.degree, c_altaz16.az.degree,c_altaz1_seven_thirty.az.degree,  c_altaz001.az.degree,c_altaz1_eight_thirty.az.degree,c_altaz01.az.degree,c_altaz1_nine_thirty.az.degree,  c_altaz1.az.degree,c_altaz1_ten_thirty.az.degree,  c_altaz12.az.degree, c_altaz1_eleven_thirty.az.degree, c_altaz13.az.degree,c_altaz1_twelve_thirty.az.degree,  c_altaz14.az.degree,c_altaz1_thir_thirty.az.degree, c_altaz17.az.degree]

#get azimuth differences and do velocity calculations for may

dt=1800 #30min is 1800 seconds
b=10 #baseline

import math
import numpy as np

daz_f=[]

for i in range(len(azimuths_m)-1):
    daz=abs(azimuths_m[i+1] - azimuths_m[i])
    daz_f=np.append(daz_f,math.radians(daz))    

v=daz_f/dt * b/2


#get azimuth differences and do velocity calculations for june

import math
import numpy as np

daz_f_j=[]

for i in range(len(azimuths_j)-1):
    daz_j=abs(azimuths_j[i+1] - azimuths_j[i])
    daz_f_j=np.append(daz_f_j,math.radians(daz_j))    

v_2=daz_f_j/dt * b/2



#plot azimuth vs time

import numpy as np
import matplotlib.pyplot as plt


time = np.array([ 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5])

plt.xlabel('Time [6pm to 2am]')
plt.ylabel('Velocity Deputy [m/s]')
plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))


plt.plot(time,v, '-o', label='Beta Crucis May',  color='yellowgreen')
plt.plot(time,v_2, '-o', label='Beta Crucis June',  color='olivedrab')


plt.legend()


#may
#betcru
# azi = np.array([145.91,151.04 ,160.52, 174.46,  190.02, 202.78, 210.88, 214.93, 216.03])
# #w hydrae
# azi1=np.array([105.36 , 99.89 ,94.12 ,86.41,  61.43, 286.35,271.18, 264.30, 258.69])
# #sirius
# azi2=np.array([282.10 , 272.65  ,264.97,257.78,  250.33 , 241.96,231.95, 219.50, 203.93])
# #canopus
# azi3=np.array([223.30  , 225.12  ,224.25,221.50,   217.25 ,  211.69,204.91, 197.08 , 188.42])


# ax = plt.subplot(111, projection='polar')
# #ax.set_rticks([1,2,3,4,5,6,7,8,9,10,11,12])
# ax.set_rticks([6,7,8,9,10,11,12,13,14,15,16,17])
# #plt.yticks(size=6)
# ax.set_rorigin(5)
# ax.plot(azi*np.pi/180, time, color='black', marker='D', markerfacecolor='yellowgreen', label='Beta Crucis')
# ax.plot(azi1*np.pi/180, time, color='black', marker='D', markerfacecolor='cyan', label='W Hydrae')
# ax.plot(azi2*np.pi/180, time, color='black', marker='D', markerfacecolor='yellow', label='Sirius')
# ax.plot(azi3*np.pi/180, time, color='black', marker='D', markerfacecolor='pink', label='Canopus')
# ax.set_theta_zero_location('N')
# ax.legend(fontsize=7, loc='lower left', bbox_to_anchor=(0.9, 0.9))
# ax.set_theta_direction(-1) # clockwise
# ax.grid(True)

#june
#beta crucis
# azi = np.array([ 160.90 , 174.46,  190.02,203.10 , 211.06, 215.00, 216.02,214.91, 212.16 ])
# #w hydrae
# azi1=np.array([93.92, 86.08 ,59.06 ,285.39,  270.92, 264.12,258.52, 253.02,  247.15])

# ax = plt.subplot(111, projection='polar')
# #ax.set_rticks([1,2,3,4,5,6,7,8,9,10,11,12])
# ax.set_rticks([6,7,8,9,10,11,12,13,14,15,16,17])
# #plt.yticks(size=6)
# ax.set_rorigin(5)
# ax.plot(azi*np.pi/180, time, color='black', marker='D', markerfacecolor='yellowgreen', label='Beta Crucis')
# ax.plot(azi1*np.pi/180, time, color='black', marker='D', markerfacecolor='cyan', label='W Hydrae')
# ax.set_theta_zero_location('N')
# ax.legend(fontsize=7, loc='lower left', bbox_to_anchor=(0.9, 0.9))
# ax.set_theta_direction(-1) # clockwise
# ax.grid(True)
# plt.savefig('fig_az_j')

# # ax.set_ylabel('Time', color='crimson')
# ax.tick_params(axis='y', colors='crimson')

# plt.show()

#altitude plots

# import numpy as np
# import matplotlib.pyplot as plt

# fig,ax = plt.subplots(1)

# # create some x data and some integers for the y axis
# #w hydrae may
# plt.plot([6,7,8,9,10,11,12,13,14],[33.80,46.34, 59.092, 71.94, 84.42,81.33,  68.61, 55.77, 43.07], label='W Hydare May' , color='cyan')
# #w hydare june
# plt.plot([6,7,8,9,10,11,12,13,14],[ 59.50,72.34, 84.77, 80.94, 68.21,55.37,  42.67,  30.21, 18.13], label='W Hydare June',  color='lightseagreen' )
# #bet cru may
# plt.plot([6,7,8,9,10,11,12,13,14],[  46.26,53.04,  58.39, 61.23, 60.72, 57.02,   51.15,  44.11 ,  36.61], label='Beta Crucis May',  color='yellowgreen' )
# #bet cru june
# plt.plot([6,7,8,9,10,11,12,13,14],[  58.52, 61.27,  60.65 ,  56.86, 50.94,  43.88 ,   36.37,  28.88  ,  21.76], label='Beta Crucis June',  color='olivedrab' )
# #sirius may
# plt.plot([6,7,8,9],[   50.68,  37.94,   25.10  ,  12.40], label='Sirius May',  color='yellow' )
# # canopus may
# plt.plot([6,7,8,9,10,11,12],[  50.75 ,41.74, 32.67 ,  23.90,  15.73,  8.44  ,    2.33], label='Canopus May',  color='pink' )

# plt.xlabel('Time starting at 5pm until 3am')
# plt.ylabel('Altitude [°]')
# ax.legend(fontsize=7, loc='lower left')

# # tell matplotlib which yticks to plot 


# # labelling the yticks according to your list
# ax.set_xticklabels(['5','6','7','8','9','10','11', '12', '1', '2','3'])

# plt.savefig('fig_al')








