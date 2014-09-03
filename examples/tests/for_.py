#-*- coding: utf-8 -*-

sps = [0, 10, 20, 30, 55]

i = 0
for nm in sps:
    
    print nm
    sps[i] = nm +13
    print sps[i],'- '
    
    i += 1
    """
    i = sps.index(nm)
    sps[i] = nm + 2
    """
    
    
    
