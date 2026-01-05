
class bag_words:
    def __init__(self, num_sentence):
        self.num_sentence = num_sentence
    
    def storage(self):
        self.sentence_bucket = []
        self.words = []

    def vectors(self):
        self.base_bucket = [[] for i in range(self.num_sentence)]
        self.words.sort()

        for i in range(len(self.base_bucket)):
            for word in (self.words):
                self.base_bucket[i].append(self.sentence_bucket[i].split(" ").count(word))
                #print(word)

    def sentence(self):
        self.storage() #Call the method

        for i in range(self.num_sentence):
            self.sentence = input(f"{i+1}: ").lower().split(" ")
            #self.sentence_bucket.append(self.word_sample)
            self.sentence = [word.lower() for word in self.sentence]
            self.join_again_sentence = " ".join(self.sentence)
            self.sentence_bucket.append(self.join_again_sentence)

            for self.word in self.sentence:
                if self.word in self.words:
                    pass
                else:
                    if len(self.word) > 1:
                        self.words.append(self.word)
                    else:
                        pass
        
        self.vectors()

    def call(self):
        self.sentence()
        self.words.sort()
        return self.words, self.sentence_bucket, self.base_bucket
        
'''if __name__ == "__main__":
    try:
        user_input_num = int(input("Enter the number of sentence: "))
        start = bag_words(user_input_num)
        output, output2, vectors = start.call()
        print(output)
        print(output2)
        print(vectors)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        print("Thank you")'''
    
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

output = []

letters = ['Book', 'Fit', 'Great', 'Is', 'Love', 'Shoes', 'The', 'This']

sentence = "I love the book".split(" ")
sentence = [word.capitalize() for word in sentence]

for word in letters:
    output.append(sentence.count(word))

print(output)

bucket = []

for i in range(3):
    bucket.append([])

bucket[0].append("I am beautiful")
print(bucket)

