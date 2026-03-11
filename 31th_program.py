message = input("Enter your message: ")

words = message.split()
secret_words = []

for word in words:
    if len(word) < 3:
        secret_words.append(word[::-1])
    else:
        new_word = "xyz" + word[1:] + word[0] + "abc"
        secret_words.append(new_word)

secret_message = " ".join(secret_words)

print("Secret Code:", secret_message)