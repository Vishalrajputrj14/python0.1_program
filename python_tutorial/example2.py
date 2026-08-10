import time
from datetime import datetime

# --- Option 1: Current System Time ---
t = time.localtime()
hour = t.tm_hour
print("System Time:", time.strftime("%H:%M:%S", t))
print("Hour from system:", hour)

# --- Option 2: Manual Input (for testing) ---
choice = input("Do you want to enter hour manually? (y/n): ")
if choice.lower() == "y":
    hour = int(input("Enter hour (0-23): "))
    print("Manual Hour:", hour)

# --- Greeting Logic ---
if 0 <= hour < 12:
    print("Good Morning sir!")
elif 12 <= hour < 17:
    print("Good Afternoon sir!")
elif 17 <= hour <= 23:
    print("Good Night sir!")
else:
    print("Invalid hour! Please enter between 0-23")
