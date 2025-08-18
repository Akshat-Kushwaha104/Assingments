n = 5 
for i in range(n):
    
    for j in range(n - i):
        print(chr(65 + j), end=" ")
    
    print("  " * (2 * i - 1), end="")
    
    
    for j in range(n - i - 1, -1, -1):
        if not (i > 0 and j == n - i - 1):
            print(chr(65 + j), end=" ")
    
    print()

