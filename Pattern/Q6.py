# *_ _ _ _ _* 5 space
# *_ _ _ _*   4 space
# *_ _ _*     3 space
# *_ _*       2 space
# *_*         1 space


N = 5
for i in range(1, N + 1):
    print("*", end = " ")
    for j in range(N + 1 - i):
        print("_", end = " ")
    print("*", end = " ")
    print()