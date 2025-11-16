number = int(input("Enter the size of the pattern: "))

i = 1
while i <= number:
    j = 1
    while j <= number:
        print("*", end="")
        j += 1
    print()  # Move to a new line after each row
    i += 1