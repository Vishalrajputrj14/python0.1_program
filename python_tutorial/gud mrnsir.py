import time

current_hour = time.localtime().tm_hour

if 5 <= current_hour < 12:
    greeting = "Good Morning!"
elif 12 <= current_hour < 17:
    greeting = "Good Afternoon!"
elif 17 <= current_hour < 21:
    greeting = "Good Evening!"
elif 21 <= current_hour < 24 :
    greeting = "Good Night!"
else:
    greeting = "Hello! It's late, take rest."

print(greeting)


