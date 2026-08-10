words = {
    "madad": "help",
    "kursi": "chair",
    "billi": "cat"
}

word = input("Enter the word you want the meaning of: ")

# Check if the word exists in the dictionary
if word in words:
    print(f"The meaning of '{word}' is: {words[word]}")
else:
    print(f"Sorry, the word '{word}' is not in the dictionary.")