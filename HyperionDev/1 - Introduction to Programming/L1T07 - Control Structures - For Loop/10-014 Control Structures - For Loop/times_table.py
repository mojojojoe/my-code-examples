# This program uses nested for loops to print the first 5 elements of the first 5 times tables
# Try creating a Trace Table (detailed in the task document) to track exactly what is happening as the program runs

for x in range(1, 6):
    for y in range(1, 6):
        print('{} * {} = {}'.format(x, y, x * y))
    print("")
