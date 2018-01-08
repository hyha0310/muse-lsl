#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 21:08:40 2017

@author: HYHa
"""

from __future__ import division
import numpy as np


#This takes the timestamps from the data and then linearly interpolates from the
#end.


def ts_linear (timestamps):
    '''Linearly interpolates the timestamps from Muse 2014 headset.
    Assumes that the recorded timestamps belong to the last sample of the 
    packet.
    '''
    
#    timestamps = np.array(data.iloc[:,0])
        
    first_ts = np.unique(timestamps)[0]
    first_index = np.where(timestamps==first_ts)[0][-1]
    trial_duration = timestamps[-1]-first_ts
    n_samples= len(timestamps)- first_index
    srate = n_samples/trial_duration
    
    true_first = first_ts-first_index/srate
    true_nsample = len(timestamps)
    end_ts = true_first+(true_nsample+1)/srate
    
    new_timestamps = np.linspace(true_first,end_ts,num=true_nsample,
                                   endpoint = True,retstep = False,
                                   dtype = None)
    
    return new_timestamps
        
#def timelim (markers):
#    tf = markers[-1][1]
#    ti = markers[0][1]
    
