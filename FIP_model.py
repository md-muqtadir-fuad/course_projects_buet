# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 00:49:43 2024

@author: Md Muqtadir Fuad
"""

def func_g(a):
    #define a function
    result = a*10-1
    return result

#%%
def fixpit( x0, es, imax, iter_, ea):
    i = 0
    xr = x0
    for i in range(imax):
        xrold = xr 
        xr = func_g(xrold)
        iter_ = iter_ + 1
        if xr != 0:
            ea = abs((xr-xrold)/xr)*100
            print('iteration:', iter_,'Error ', ea)
        if ea < es or iter_ >= imax:
            break
        
    fixpt = xr
    print('Answer',fixpt)
        
        