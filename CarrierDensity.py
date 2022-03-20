# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 20:16:53 2017

@author: daned
"""

import numpy as np

#%% Define constants used in the calculation

h = 6.626e-34 #J s, Planck's constant
c = 2.998e8 # m/s, speed of light

#%% Define the parameters of the laser source

wavelength = 470 #nm, wavelength of excitation laser
P = 1 # uW, average power of pulsed laser
Rep_rate = 1e6 # Hz, rep rate of laser
r = 15 * 1e-4 # um --> cm, 1/e^2 radius of Gaussian laser spot

Area = np.pi*r**2 # 1/e^2 area of laser

#%% Define film parameters

OD = 2 # Optical density at laser excitation wavelength
d = 700 #nm, film thickness - assumes carriers rapidly diffuse through film thickness


#%% Laser properties

Energy = P/Rep_rate # uJ, Energy per pulse
Fluence = Energy/Area # uJ/cm^2, fluence

#%% Function to calculate the initial carrier density

def CarrDens(Fluence):
    N0 = Fluence*1e-6*wavelength*1e-9*(1-10**(-OD))/(h*c*d*1e-7) # for one pass through the film, use 2*OD if there are two passes - i.e. back metal contact
    return N0

#%% print the fluence and calculated carrier density
    
print('Fluence:', f'{Fluence:.3}', 'uJ/cm^2/pulse')

N0 = CarrDens(Fluence)
print('Carrier Density:', f'{N0:.3}', 'cm^-3')




 