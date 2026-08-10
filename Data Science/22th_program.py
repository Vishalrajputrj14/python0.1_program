# KBC Game Program

questions = [
    ("What is the capital of India?",
     ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
     "B", 1000),

    ("Which language is used for Data Science?",
     ["A. HTML", "B. CSS", "C. Python", "D. PHP"],
     "C", 2000),

    ("Who is known as the Father of Computer?",
     ["A. Charles Babbage", "B. Elon Musk", "C. Bill Gates", "D. Steve Jobs"],
     "A", 5000),

    ("Which planet is known as the Red Planet?",
     ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
     "B", 10000)
]

money_won = 0

print("🎉 Welcome to KBC Game 🎉\n")

for question in questions:
    print("\nQuestion:")
    print(question[0])

    for option in question[1]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == question[2]:
        money_won = question[3]
        print("✅ Correct Answer!")
        print("You won ₹", money_won)
    else:
        print("❌ Wrong Answer!")
        break

print("\nGame Over!")
print("🏆 Final Amount You Are Taking Home: ₹", money_won)