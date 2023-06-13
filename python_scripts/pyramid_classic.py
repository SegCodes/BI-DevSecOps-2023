lines = int(input("Enter number of lines: "))
for i in range(1, (lines + 1)):
    for j in range(1, i + 1):
        print('*', end='')
    print()