# Task 1 : Check if a number is Even or Odd

try:
    num = int(input("Enter the number : "))
    if num % 2 == 0:
        print(num, "is an Even number.")
    else:
        print(num, "is an Odd number")
except (ValueError, TypeError, NameError):
    print("Invalid user input. Please enter a valid integer.")

print ("Thank you")