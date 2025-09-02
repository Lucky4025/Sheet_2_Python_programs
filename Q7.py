# 7. Take an integer A as input. You have to print the sum of all odd numbers 
# in the range [1, A].
# Input:- A= 4
# Output:- 4
# Explanation:- For A = 4, Odd numbers 1 and 3 lie in the range [1, 4]. Sum = 1 + 3 = 4.

A = int(input("Enter any number: "))
count = 0
for i in range(1, A + 1):
    if i % 2 != 0:
        count += i
        
print(count)
