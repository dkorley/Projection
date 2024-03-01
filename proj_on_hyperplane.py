# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 09:46:48 2024

@author: dkorley
"""

import numpy as np
import proj_on_origin as po

def Proj_on_hyperplane(C, d, v):
    x = po.min_norm(C, d - (C@v))
    return x  + v

def main():
    C = np.array([[2, 1, 1, 4], [1, 1, 2, 1]])
    d = np.array([[7, 6]]).T
    v = np.array([[1, 1, 1, 1]]).T
    
    x = Proj_on_hyperplane(C, d, v)
    print(x)
    
if __name__ == '__main__':
    main()
