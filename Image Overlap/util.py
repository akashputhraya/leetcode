import numpy as np
from scipy.ndimage import convolve

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        return np.max(convolve(np.pad(B,len(A),mode='constant'),np.flip(A),mode='constant'))