'''
Create your main.py Python file.
Take the input from the user and assign it to a variable called radius.
Create variables called circumference and area and assign them their appropriate values.
Print the two variables.
'''
radius = input("Enter the radius: ")
circumference = 2 * 3.14159 * float(radius)
area = 3.14159 * float(radius) ** 2
print("Circumference:", circumference)
print("Area:", area)