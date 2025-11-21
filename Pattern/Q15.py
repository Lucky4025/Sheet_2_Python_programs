# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * *
# *

N = 5
for i in range(1, N + 1):
    for j in range(N - i):
        print(" ", end = " ")
    for j in range(i):
        print("*", end = " ")
    print()
N = 4
for i in range(N, 0, -1):
    for j in range(N - i):
        print(" ", end = ' ')
    for j in range(i):
        print("*", end = ' ')
    print()