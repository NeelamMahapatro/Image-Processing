import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

intensity_array=np.array([[1,2,3,4],[5,6,7,8],[1,2,2,1],[1,2,1,2]])

r = intensity_array.shape[0];
c = intensity_array.shape[1];

int_string = np.zeros((r*c));
idx = 0;

for i in range(r): 
    for j in range(c):
        int_string[idx] = intensity_array[i,j];
        idx = idx+1
        

currentString = "" ; 
current = "" ; 

ans = {}
outputIndex = 0;

dictVal = {};
dict_idx = 0;

for i in range(0,255) :
    dictVal[str(i)] = i;
        
dict_idx = 256;

current = int_string[0];

currentString = str(int(current));

for i in range(1,idx) :
    current = int_string[i];
    
    t_str = currentString + "-" + str(int(current))
        
    if t_str in dictVal :
        currentString = t_str;
    else:
        ans[outputIndex] = dictVal[currentString]
        outputIndex = outputIndex + 1;
        currentString = str(int(current));
        
        dictVal[t_str] = dict_idx;
        dict_idx = dict_idx + 1
    
if currentString in dictVal : 
    ans[outputIndex] = dictVal[currentString]
    outputIndex = outputIndex + 1;
    
codes=list(ans.values());
print("Encoded ans:")
print(codes)

decodeAns=""
for i in codes:
    decodeAns=decodeAns+" "+list(dictVal.keys())[list(dictVal.values()).index(i)]

print("Decoded ans:")
print(decodeAns)
