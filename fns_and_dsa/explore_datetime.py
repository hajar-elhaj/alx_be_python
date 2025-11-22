import datetime

def display_current_datetime():
    return datetime.datetime.now()

def calculate_future_date(days):
    return datetime.datetime.now() + datetime.timedelta(days=days)

# Show current date
print("Current date and time: ", end="")
print(display_current_datetime())

# Ask user for days
number_of_days = int(input("Enter number of days to add to the current date: "))

# Show future date
print("Future date: ", end="")
print(calculate_future_date(number_of_days))