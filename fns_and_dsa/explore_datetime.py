import datetime 

def display_current_datetime():
 current_date = datetime.datetime.now()
 return print(current_date)

print("Current date and time:", end=" ")
display_current_datetime()

number_of_days = int(input("Enter number of days to add to the current date: "))

def calculate_future_date():
    future_date = datetime.date.today() + datetime.timedelta(days=number_of_days)
    return print(future_date)

print("Future date:", end=" ")
calculate_future_date()