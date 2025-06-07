task = input("Enter your task:")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no):")

match priority :
    
    case  "high":
        reminder = f" HIGH PRIORITY {task}"
    
    case "medium":
        reminder = f"medium priority {task}"
        
    case "low":
        reminder = f"low priority {task}"
        
        
    case _:
        reminder = f"invalid{task}(unknown priority)"
        
if time_bound == "yes":
    reminder += "_ is a high priority task that requires immediate attention today!"
    
print("\nReminder")
print("Reminder:", reminder)
    
    
        
