# You are given an integer array C of size A.
# Now you need to find a subarray (contiguous elements) so that the sum of contiguous elements is maximum.
# But the sum must not exceed B.
# ---------------------------------------------------------------------------------------------------------

A = 5
B = 12
C = [2, 1, 3, 4, 5]

count = 0

for i in range(A):
    t_sum = 0
    for j in range(i, A):
        t_sum += C[j]
        if t_sum <= B and t_sum > count:
            count = t_sum
            sub_arr = C[i : j + 1]

print(sub_arr)
