# Remaining Que - 5, 6, 7, 8, 9, 10, 11

N = int(input())
for i in range(1, N + 1):
    for j in range(N - i):
        print(" ", end = ' ')
    for k in range(i):
        print("*", end = ' ')
    print()