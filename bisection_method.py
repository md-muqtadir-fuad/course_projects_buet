def func(a):
    #define a function
    result = a*10-1
    return result
    
#%%
def bisection_method(xl, xu, es, imax, iter_, ea):
    iter_= 0
    xr = ( xl+ xu)/2
    for iter_ in range( imax ):
        xrold = xr
        xr = ( xl+ xu)/2
        iter_=iter_+1
        if xr != 0:
            ea = abs((xr-xrold)/xr)*100
        
        test = func(xl)*func(xr)
        
        if test < 0 :
            xu = xr
        elif test > 0:
            xl = xr
        else:
            ea = 0
            
        if ea < es or iter_ > imax:
            break
        
    bisect_ans = xr
    print( 'the answer is', bisect_ans)
    
        