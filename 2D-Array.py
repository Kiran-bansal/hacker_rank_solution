import math
import os
import random
import re
import sys

if __name__ == '__main__':
    
    arr = []
    
    for i in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    sum_array=[]
    
    for i in range(4):
        for j in range(4):
            sum_array.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
    
    print(max(sum_array))
