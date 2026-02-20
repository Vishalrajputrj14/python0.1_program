from datetime import datetime

current_hour = datetime.now().hour

if 0 <= current_hour < 12:
    print("Good Morning 🌅")
elif 12 <= current_hour < 18:
    print("Good Afternoon ☀️")
else:
    print("Good Evening 🌙")

print("Current Hour:", current_hour)