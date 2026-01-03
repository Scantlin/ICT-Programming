print("Bag of words")

num_sentence = int(input("Enter the number of sentences: "))
words = []

print("Enter sentence: ")
for i in range(num_sentence):
    sentence = input(f"{i + 1}: ").lower().split(" ")
    for word in sentence:
        if word in words:
            pass
        else:
            words.append(word)

print(words)