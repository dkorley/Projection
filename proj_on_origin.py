# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:13:04 2024

@author: dkorley
"""

import QRd
import forwardSubstitution as fs
import backwardSubstitution as bs

def min_norm(C, d):
    Q, R, rank = QRd.QR(C.T)
    w = fs.forwardSubstitution(R.T, d)
    theta = bs.backwardSubstitution(R, w)
    return C.T @ theta

