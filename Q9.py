# 9. Take an integer N as input. Your task is to calculate 
# and print the sum of the digits of the given number N.
# Input:- N = 1589
# Output:- 23
# Explaination:- For the number 1589, the digits are 1,5,8,9. The Sum(1589) = 1+5+8+9 = 23.

N = int(input("Enter any number: "))
count = 0
while N > 0:
    digit = N % 10 
    count += digit
    N //= 10

print(count)
