'''
Take the first input from the user and call it first_number.
Take the second input from the user and call it second_number.
Create the variables sum, subtraction, multiplication and division and assign them their values based on the two inputs.
Print the four variables.
'''
first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
sum = int(first_number) + int(second_number)
subtraction = int(first_number) - int(second_number)
multiplication = int(first_number) * int(second_number)
division = int(first_number) / int(second_number)
print("Sum:", sum)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
