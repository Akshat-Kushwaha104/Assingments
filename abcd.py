def print_pattern():
    rows = 5
    for i in range(rows):
        
        for j in range(rows - i):
            print(chr(65 + j), end=' ')
        
        
        spaces = 2 * i - 1
        print('  ' * spaces, end='')

        
        for j in reversed(range(rows - i)):
            if not (i == 0 and j == rows - i - 1):  
                print(chr(65 + j), end=' ')
        
        print()

print_pattern()
