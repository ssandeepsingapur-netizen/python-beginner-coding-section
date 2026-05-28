text = input("Enter the a paragraph")
lower_text = text.lower()
words = lower_text.split()
word_count = len(words)
char_count = len(text)
sentence_count  = text.count('.')+text.count('!')+text.count('?')

longest_word = max(words,key = len)
frequency = {}

for word in words:
    word = word.strip(", ! ?")
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word] = 1

print("\n ---Text analysis result ---")
print("number of words:",word_count)
print("Number of charcters",char_count)
print("Number of sentence:",sentence_count)
print("Longest word",longest_word)
print("\n word frequency")
for word,count in frequency.items():
    print("word :",word,"count :",count)
