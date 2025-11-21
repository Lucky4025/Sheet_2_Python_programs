# How many subarray index 3 is present.
# [3, -2, 4, -1, 2, 6]

A = [3, -2, 4, -1, 2, 6]
n = 6
i = 3
count = (i + 1) * (n - i)
print(count)
