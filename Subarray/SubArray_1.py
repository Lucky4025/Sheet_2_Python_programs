# Given an array A of N non-negative numbers and a non-negative number B, you need to find the number 
# of subarrays in A with a sum less than B. We may assume that there is no overflow.

# ----------------------------------------------------------------------------------------
N = 3
A = [2, 5, 6]
B = 10
count = 0
for i in range(N):
    t_sum = 0
    for j in range(i, N):
        t_sum += A[j]
        if t_sum < B:
            count += 1
print(count)