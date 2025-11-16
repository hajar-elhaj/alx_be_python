num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation_type = input("Choose the operation (+, -, *, /):")
match operation_type:
    case "+":
        print(f"The sum is: {num1 + num2}")
    case "-":
        print(f"The difference is: {num1 - num2}")
    case "*":
        print(f"The product is: {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"The quotient is: {num1 / num2}")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation selected.")
print("Thank you for using the calculator!")