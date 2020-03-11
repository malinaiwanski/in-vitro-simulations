# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:24:55 2020

@author: 6182658
"""

#import math
#import matplotlib.pyplot as plt
import numpy as np
#import scipy as sp

#parameters
mt_length = 1000
nstep = 1000

#rates of reactions
k_fwd = 0.01 #steps per sec
k_bck = 0 #steps per sec
k_on = 0.0002 #per dimer per sec
k_off = 0.3 #per sec

#update vectors for each reaction
nu_fwd = -1
nu_bck = -1
nu_on = 1
nu_off = -1

#update affinities of mt sites
alpha_max = 0.0001 #change in k_on at site of motor
#assume this drops exponentially with number of sites away from motor and with time


def gillespie(mt, affinity, t, m): #update time and state vectors (mt and affinity at site m)
   
    #generate random numbers
    rt = np.random.random()
    rr = np.random.random()
    
    #time to next reaction
    tau = np.log(1/rt)/k_tot
    
    #determine which reaction
    j = 0
    test = k[0]/k_tot						
    while test < rr and j < len(k)-1:
        t += k[j]/k_tot
        j += 1
		
    t += tau #update time
    mt[i,m] += nu[j] #update state
    if m < mt_length-1 and mt[m+1] == 0 and j == 0:
        mt[m+1] -= nu[j] #update state of +1 site for forward step
    if m >  0 and mt[m-1] == 0 and j == 1:
         mt[m+1] -= nu[j] #update state of -1 site for back step
    
    affinity[m] += alpha_max #update affinity
    #add to update of surrounding sites
    affinity[affinity<0] = k_on

    
#initialize
mt = np.zeros((nstep,mt_length))
affinity = np.zeros((nstep,mt_length))
affinity[:] = k_on
t = np.zeros(nstep)


for i in range(0,nstep-1):
    #choose MT lattice site
    m = np.random.randint(0,mt_length-1)
    #check current possible reactions
    if mt[i,m] == 1: #site is occupied
        k = [k_fwd, k_bck, 0, k_off]
        k_tot = np.sum(k)
        nu = [nu_fwd, nu_bck, 0, nu_off]
    else: #site is empty
        k = [0, 0, k_on, k_off]
        k_tot = np.sum(k)
        nu = [0, 0, nu_on, 0]
    #run Gillespie
    mt[i+1,m],affinity[i+1,m],t[i+1] = gillespie(mt[i,m],affinity[i,m],t[i],m)