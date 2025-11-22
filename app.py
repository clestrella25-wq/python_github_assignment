# Study Hour Tracker Program
print("Welcome to my Python program!")

try:
    # Ask user for input
    hours = input("How many hours did you study today? ")
    
    # Convert input to float for calculation
    hours = float(hours)
    
    # Calculate weekly estimate
    weekly_hours = hours * 7
    
    # Output result
    print(f"You are on track to study {weekly_hours} hours this week.")
    
except ValueError:
    # Handle non-numeric errors
    print("Please enter a valid number.")
    exit()