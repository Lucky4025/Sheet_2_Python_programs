# Given an array of integers A, a subarray of an array is said to be good if it fulfils any 
#   one of the criteria:
# 1. Length of the subarray is be even, and the sum of all elements of the subarray must be less than B.
# 2. Length of the subarray is be odd, and the sum of all elements of the subarray must be greater than B
#   your task is to find the count of the good subarrays in A.
# -------------------------------------------------------------------------------------------------------

def solve(self, A, B):
    N = len(A)
    count = 0
    for i in range(N):
        sum1 = 0
        for j in range(i.N):
            sum1 += A[j]
            if sum1 < B:
                count += 1
    return count
solve(2, 5, 6)
