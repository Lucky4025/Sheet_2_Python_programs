rows = 5
for i in range(rows):
    stars_count = rows - i          
    spaces_count = i * 2            
    left_stars = "*" * stars_count
    middle_spaces = " " * spaces_count
    right_stars = "*" * stars_count
    print(left_stars + middle_spaces + right_stars)

