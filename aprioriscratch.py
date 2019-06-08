#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 09:16:12 2018

@author: ayush
"""

from itertools import combinations
import pandas as pd
import numpy as np

trans=pd.read_csv('', header=None,index_col=0)

def apriori(trans, support=0.01, minlen=1):
    ts=pd.get_dummies(trans.unstack().dropna()).groupby(level=1).sum()

    collen, rowlen  =ts.shape
    pattern = []
    for cnum in range(minlen, rowlen+1):
        for cols in combinations(ts, cnum):
            patsup = ts[list(cols)].all(axis=1).sum()
            patsup=float(patsup)/collen
            pattern.append([",".join(cols), patsup])
    sdf = pd.DataFrame(pattern, columns=["Pattern", "Support"])
    results=sdf[sdf.Support >= support]

    return results
