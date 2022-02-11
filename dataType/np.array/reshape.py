#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:01:05 2020

@author: yuan
"""

import numpy as np


nd1=np.arange(12);nd1

#reshape()
nd2=nd1.reshape((3,4));nd2
nd2.reshape((2,6))

#trasnpose()
np.transpose(nd2)
