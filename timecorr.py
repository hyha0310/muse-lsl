#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 21:08:40 2017

@author: HYHa
"""

from __future__ import division
import pandas as pd
import numpy as np


#This takes the timestamps from the data and then linearly interpolates from the
#end.
def ts_linear (timestamps):
#    timestamps = np.array(data.iloc[:,0])
    first_ts = np.unique(timestamps)[0]
    trial_duration = timestamps[-1]-first_ts
    n_samples= len(timestamps)- np.where(timestamps==first_ts)[0][-1]
    srate = n_samples/trial_duration
    new_timestamps = np.arange(first_ts,timestamps[-1],1/srate)             
    
    return new_timestamps

#def timelim (markers):
#    tf = markers[-1][1]
#    ti = markers[0][1]
    