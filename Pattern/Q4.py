# 1
# 1 *
# 1 * 3
# 1 * 3 *
# 1 * 3 * 5
N = 5
for i in range(1, N+1):
    for j in range(1, i + 1):
        if j % 2 == 1:
            print(j, end = ' ')
        else: 
            print("*", end = ' ')
    print()