import math
import pandas as pd
import numpy as np

def calculation(num):
    return math.log(num/(10-1/2))

N = 20
nums = [16,17,10,26,13,14,28,45,10,12,12,10,136,16,25,36,12,14,22,10]

tot = 0
for num in nums:
    tot += calculation(num)

alpha = 1 + N * tot^(-1)

sigma = (alpha - 1)/ math.sqrt(N)