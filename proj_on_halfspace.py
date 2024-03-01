# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 09:49:28 2024

@author: dkorley
"""

import proj_on_hyperplane as ph
import numpy as np

def proj_on_halfspace(C, d, v):
    m = C.shape[0]
    flag = 0
    for i in range(1, m+1):
        if C[i, :]@v > d[i]:
            flag = 1
            break
    if flag == 0:
        x = v
    else:
        x = ph.Proj_on_hyperplane(C, d, v)
    return x

