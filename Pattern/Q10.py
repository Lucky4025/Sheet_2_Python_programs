rows = 5
for i in range(1, rows + 1):
    stars = "*" * i                 
    spaces = " " * (2 * (rows - i)) 
    right_stars = "*" * i           
    print(stars + spaces + right_stars)
