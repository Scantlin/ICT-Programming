print("Bag of words")

num_sentence = int(input("Enter the number of sentences: "))
words = []

print("Enter sentence: ")
for i in range(num_sentence):
    sentence = input(f"{i + 1}: ").split(" ")
    for word in sentence:
        words.append(word)

print(words)