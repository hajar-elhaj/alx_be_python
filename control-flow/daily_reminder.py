# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Determine the base message using match case
match priority:
    case "high":
        message = f"{task}' is a high priority task"
    case "medium":
        message = f"{task}' is a medium priority task"
    case "low":
        message = f"{task}' is a low priority task"
    case _:
        message = f"{task}' has an unknown priority"

# Add time-sensitive info
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Print the reminder in the expected format
print(f"Reminder: {message}")