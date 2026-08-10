# X = 4
# # X is the variable to match 
# match X:
#     # if X is 0
#     case 0:
#         print("X is zero")
#         #case with if condition
#     case 4: 
#         print("X is four")
#     case _:
#         print("X is something else")
        


# print("hello world")

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# print("\nSelect the operation:")
# print("1. Addition (+)")
# print("2. Subtraction (-)")
# print("3. Multiplication (*)")
# print("4. Division (/)")

# choice = input("Enter your choice (1/2/3/4): ")

# match choice:
#     case "1":
#         print("Result:", num1 + num2)
#     case "2":
#         print("Result:", num1 - num2)
#     case "3":
#         print("Result:", num1 * num2)
#     case "4":
#         if num2 != 0:
#             print("Result:", num1 / num2)
#         else:
#             print("Error: Division by zero is not allowed")
#     case _:
#         print("Invalid Choice")

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# print("\nSelect the operation:")
# print("1. Addition (+)")
# print("2. Subtraction (-)")
# print("3. Multiplication (*)")
# print("4. Division (/)")

# choice = input("Enter your choice (1/2/3/4): ")

# match choice:
#     case "1": 
#         result = num1 + num2
#         print("Result:", result)
#     case "2": 
#         result = num1 - num2
#         print("Result:", result)
#     case "3": 
#         result = num1 * num2
#         print("Result:", result)
#     case "4": 
#         if num2 != 0:
#             result = num1 / num2
#             print("Result:", result)
#         else:
#             print("Error: Division by zero is not allowed")
#     case _: 
#         print("Invalid Choice")

# chat gtp ka program 
# Restaurant Order Program

# # 🧾 Menu Card (print)
# print("🍽️ Welcome to Vishal Restaurant")
# print("Here is the Menu:\n")

# print("1. Pizza 🍕")
# print("2. Burger 🍔")
# print("3. Pasta 🍝")
# print("4. Coffee ☕")

# # 🧍 Waiter taking order (input)
# choice = input("\nWaiter: Sir, what would you like to order? (1/2/3/4): ")

# # 👨‍🍳 Kitchen Decision (match-case)
# match choice:
#     case "1":
#         print("Kitchen: Preparing your Pizza 🍕")
#     case "2":
#         print("Kitchen: Preparing your Burger 🍔")
#     case "3":
#         print("Kitchen: Preparing your Pasta 🍝")
#     case "4":
#         print("Kitchen: Preparing your Coffee ☕")
#     case _:
#         print("Kitchen: Sorry Sir, invalid order 😅")
