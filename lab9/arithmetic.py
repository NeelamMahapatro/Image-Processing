# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:18:52 2019

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from numpy import linalg
import operator
import math

prob = dict()
prob['a'] = 0.4
prob['b'] = 0.2
prob['c'] = 0.1
prob['d'] = 0.3

low_actual = dict()
high_actual = dict()
low_val = dict()
high_val = dict()

low_actual['a'] = [0, prob['a']]
low_val['a'] = [0, prob['a']]

x = prob['a']
for i in prob:
    if(i == 'a'):
        continue;
    low_actual[i] = [x, x+prob[i]]
    low_val[i] = [x, x+prob[i]]
    x = low_actual[i][1]
print(low_val)
print(high_val)

#for encoding
seq = "dad"
low = 0
high = 0
for i in range(len(seq)-1):
    low = low_val[seq[i]][0]
    high = low_val[seq[i]][1]
    rang = high-low
    for j in low_val:
        #print(low_val[j][0], low_val[j][1])
        low_val[j] = [low + rang*low_actual[j][0], low + rang*low_actual[j][1]]
        print(low_val[j][0], low_val[j][1])
        
        
low = low_val[seq[len(seq)-1]][0]
high = low_val[seq[len(seq)-1]][1]
encoded_ans = (low+high)/2
print("Encoded output: ")
print(encoded_ans)


#for decoding

length = len(seq)
encoded = 0.802
ans = ""

tag = encoded
tag_new = 0
key = 'a'
for i in range(length):
    for j in prob:
        if(tag>=low_actual[j][0] and tag<=low_actual[j][1]):
            ans = ans+j
            key = j
            break
    tag = (tag-low_actual[key][0])/(low_actual[key][1]-low_actual[key][0])
    
print("Decoded output :")
print(ans)

