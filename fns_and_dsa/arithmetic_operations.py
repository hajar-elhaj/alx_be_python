def perform_operation(num1:float, num2:float, operation:str):
    if operation == "add":
     return float(num1 + num2)
    elif operation == "subtract":
     return float(num1 - num2)
    elif operation == "multiply":
     return num1 * num2
    elif operation == "divide":
     if num2 != 0:
      return float(num1 / num2)
     else:
      return "Error: Division by zero"
    else:
     return "Error: Invalid operation"

