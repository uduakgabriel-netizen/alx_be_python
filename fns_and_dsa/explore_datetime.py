# Import the components.........
from datetime import datetime, timedelta

# Get current date and time
def display_current_datetime():
  current_date = datetime.now()
  formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current date and time: {formatted}")

display_current_datetime()

# Get user input............
def calculate_future_date():
  current_date = datetime.now()

  days_to_add = int(input("Enter the number of days to add to the current date: "))

  future_date = current_date + timedelta(days=days_to_add)

  print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
  
calculate_future_date()