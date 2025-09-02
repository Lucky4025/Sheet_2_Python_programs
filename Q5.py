# 5. Write a program to find the sum of all Natural numbers from 1 to N, 
# where you have to take N as input from user
# Input:- N = 10
# Output:- 55

N = int(input("Enter any number:"))
count = 0
for i in range(1, N + 1):
    count += i
print(count, end = ' ')