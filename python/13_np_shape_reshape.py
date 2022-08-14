"""
@prob_name
NumPy Shape Reshape

@prob_qs
You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.

@prob_link
https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true

@example1
INPUT:
1 2 3 4 5 6 7 8 9

OUTPUT:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

@constraint
2 <= N <= 10
0 <= marks[i] <= 100
length of marks arrays = 3
"""

import numpy as np

arr = np.array(list(map(int, input().split())))
print(np.reshape(arr, (3,3)))