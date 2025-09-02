# 8. Take an integer N as input and print the count of digits of that number.
# Input:- N = 10101
# Output:- 5
# Explanation:- 10101 has 5 digits

N = int(input("Enter any number: "))
count = 0
while N > 0:
    count += 1
    N //= 10
print(count)
