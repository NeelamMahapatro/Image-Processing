# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 13:35:06 2019

@author: STUDENT
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import numpy.fft as fft
from PIL import Image
from numpy import linalg
import operator
import math
c=0
enc={}

def call(x):
    if len(x)==2:
        enc[x[1][0]]='0'
        enc[x[0][0]]='1'
        
        0
        return
    
    y=[]
    z=x[0][0]+'-'+x[1][0]
    
    y.append((z,x[0][1]+x[1][1]))
    
    for i in range(2,len(x)):
        y.append(x[i])
        
    y.sort(key = lambda x: x[1])
    
    call(y)
    enc[x[1][0]]= enc[z]+'0'
    enc[x[0][0]]= enc[z]+'1'

ar = Image.open('cameraman.tif').convert('L')
img = np.array(ar, dtype = np.float)
M,N = img.shape
arr=np.zeros((M*N,1),dtype=np.float)

dic={}

s="COMMITTEE"
for i in range(len(s)):
    if s[i] not in dic:
        dic[s[i]]=1
            
    else:
        dic[s[i]]=dic[s[i]]+1  
                 
arr=[]
arr1=[]

l=len(dic)
x=M*N

for i in dic:
    arr.append((i,dic[i]))

arr.sort(key = lambda x: x[1]) 
mp={}

for i in range(len(arr)):
    arr1.append((str(i),arr[i][1]))
    
for i in range(len(arr1)):
    mp[int(arr1[i][0])]=arr[i][0]
    

call(arr1)
ans=[]

for i in enc:
    if i.isnumeric()==1:
        ans.append((int(i),enc[i]))
final_ans=[]

for i in range(len(ans)):
    final_ans.append((mp[ans[i][0]],ans[i][1]))
print("Hufmann Encoding output is: ")
for i in range(len(ans)):
    print(str(final_ans[i][0])+"   "+str(final_ans[i][1]))

entropy = 0
for i in dic:
    entropy= entropy-(dic[i]/len(s))*math.log2((dic[i]/len(s)))

print("Entropy of the encoding is :")
print(entropy)

Lavg = 0
for i in range(len(final_ans)):
    Lavg = Lavg+(dic[final_ans[i][0]]/len(s))*len(final_ans[i][1])

print("Average number of bits :", str(Lavg))
print("Efficiency of the encoding is :", str(entropy/Lavg))




    

  
   
            

           
            
        