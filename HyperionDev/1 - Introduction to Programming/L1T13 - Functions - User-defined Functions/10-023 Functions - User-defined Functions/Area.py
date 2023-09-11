# Functions to calculate the area of various shapes
def square(length):
    return length * length

def rectangle(width , height):
    return width * height

def circle(radius):
    return 3.14 * radius ** 2

# Function for menu
def options():
    print("Options:")
    print("s = calculate the area of a square.")
    print("c = calculate the area of a circle.")
    print("r = calculate the area of a rectangle.")
    print("q = quit")
    
# Get input from user and calculate chosen shape
print("This program will calculate the area of a square, circle or rectangle.")
choice = "x"
options()
while choice != "q":
    choice = input("Please enter your choice: ")
    if choice == "s":
        length = float(input("Length of square: "))
        print("The area of this square is", square(length))
        options()
    elif choice == "c":
        radius = float(input("Radius of the circle: "))
        print("The area of the circle is", circle(radius))
        options()
    elif choice == "r":
        width = float(input("Width of the rectangle: "))
        height = float(input("Height of the rectangle: "))
        print("The area of the rectangle is", rectangle(width, height))
        options()
    elif choice == "q":
        print("")
    else:
        print("Unrecognized option.")
        options()
