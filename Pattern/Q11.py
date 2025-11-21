rows = 5 
for i in range(rows):
    stars = "*" * (rows - i)          
    spaces = " " * (2 * i)            
    print(stars + spaces + stars)
for i in range(rows):
    stars = "*" * (i + 1)            
    spaces = " " * (2 * (rows - i - 1)) 
    print(stars + spaces + stars)
