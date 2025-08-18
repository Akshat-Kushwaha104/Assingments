n = 5  # Number of rows
for i in range(n):
    # Left side letters
    for j in range(n - i):
        print(chr(65 + j), end=" ")
    
    # Spaces in the middle
    print("  " * (2 * i - 1), end="")
    
    # Right side letters (avoid repeating middle letter when spaces > 0)
    for j in range(n - i - 1, -1, -1):
        if not (i > 0 and j == n - i - 1):
            print(chr(65 + j), end=" ")
    
    print()
