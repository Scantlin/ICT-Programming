
class bag_words:
    def __init__(self, num_sentence):
        self.num_sentence = num_sentence
    
    def storage(self):
        self.words = []

    def sentence(self):
        self.storage() #Call the method
        for i in range(self.num_sentence):
            self.sentence = input(f"{i+1}: ").split(" ")
            self.sentence = [word.capitalize() for word in self.sentence]

            for self.word in self.sentence:
                if self.word in self.words:
                    pass
                else:
                    self.words.append(self.word)
    def call(self):
        self.sentence()
        self.words.sort()
        return self.words

if __name__ == "__main__":
    user_input_num = int(input("Enter the number of sentence: "))
    start = bag_words(user_input_num).call()
    print(start)

'''
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

print(words)'''