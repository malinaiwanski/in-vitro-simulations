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
nstep = 100000

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


def gillespie(X, affinity, t, m): #update time and state vectors (mt and affinity at site m)
   
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
    X[m] += nu[j] #update state
    if m < mt_length-1 and X[m+1] == 0 and j == 0:
        X[m+1] -= nu[j] #update state of +1 site for forward step
    if m >  0 and X[m-1] == 0 and j == 1:
         X[m+1] -= nu[j] #update state of -1 site for back step
    
    #call update affinity here
    return X, affinity, t

def affinity_update(aff, X): #update affinity based on motor positions
    aff[X==1] = alpha_max #update affinity
    motor_loc = np.where(X==1)
    for j in range(0,mt_length):
        while motor_loc+j<mt_length-1:
            aff[motor_loc+j] = alpha_max*np.exp(-j)
        while motor_loc-j>=0:
            aff[motor_loc-j] = alpha_max*np.exp(-j)
    #add to update of surrounding sites
    aff[aff<0] = k_on
    return aff
    
#initialize
mt = np.zeros((nstep,mt_length))
affinity = np.zeros((nstep,mt_length))
affinity[:] = k_on
t = np.zeros(nstep)

for i in range(0,nstep-2):
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
    mt[i+1,:],affinity[i+1,:],t[i+1] = gillespie(mt[i,:],affinity[i,:],t[i],m)