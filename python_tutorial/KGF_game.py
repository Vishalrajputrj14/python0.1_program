# KBC Program using List

questions = [
    "Which planet is known as the Red Planet?",
    "Who is known as the Father of the Nation in India?",
    "Which is the national animal of India?",
    "What is the capital of Rajasthan?"
]

options = [
    ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
    ["A. Jawaharlal Nehru", "B. Subhash Chandra Bose", "C. Mahatma Gandhi", "D. Bhagat Singh"],
    ["A. Lion", "B. Tiger", "C. Elephant", "D. Leopard"],
    ["A. Jaipur", "B. Udaipur", "C. Jodhpur", "D. Kota"]
]

answers = ["B", "C", "B", "A"]   # Correct answers list
prize_money = [1000, 2000, 5000, 10000]  # Prize money for each question

total = 0
print("💰 Welcome to Kaun Banega Crorepati (KBC) 💰\n")
print("Answer carefully and win money!\n")

for i in range(len(questions)):
    print(f"Q{i+1}: {questions[i]}")
    for opt in options[i]:
        print(opt)
    
    ans = input("👉 Your answer (A/B/C/D): ").strip().upper()
    
    if ans == answers[i]:
        print("✅ Correct Answer!\n")
        total = prize_money[i]
    else:
        print(f"❌ Wrong Answer! The correct answer is {answers[i]}")
        break

print("---------------------------------------------------")
print(f"🎉 You are taking home ₹{total}")
