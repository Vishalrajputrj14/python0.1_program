'''
Snake Water Gun 


sanke water and gun is a variation of the children's game "rock-peper-scissors" where players use hand gestures to represnt a snake, water, or a gun the gun beats the snake 
the water beats the gun and the snale neats tje water Write a python program to create a snake water gun game in python using if-else statements do not create any fancy gui use proper funtions check fo win.
'''



import random

def check_win(player, computer):
    if player == computer:
        return "It's a draw!"

    # Rules: Gun > Snake, Water > Gun, Snake > Water
    if (player == "gun" and computer == "snake") \
       or (player == "water" and computer == "gun") \
       or (player == "snake" and computer == "water"):
        return "You win!"
    else:
        return "Computer wins!"

def snake_water_gun():
    choices = ["snake", "water", "gun"]

    print("Welcome to Snake-Water-Gun Game!")
    print("Choices: snake / water / gun")

    player = input("Enter your choice: ").lower()
    
    if player not in choices:
        print("Invalid choice! Please choose snake, water, or gun.")
        return
    
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    result = check_win(player, computer)
    print(result)

# Run the game
snake_water_gun()

