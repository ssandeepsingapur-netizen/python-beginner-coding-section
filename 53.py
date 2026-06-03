text = input("enter the text")
lower_text = text.lower()
words = lower_text.split()
words_count = len(words)
char_count = len(text)
sentence_count = text.count('.')+text.count('!')+text.count('?')

longest_word = max(words,key = len)
frequency = {}
for word in words:
    word = word.strip(", ! ?")
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word]=1

print("\n--Text analysis Result---")
print("number of words:",words_count)
print("number of charcter:",char_count)
print("number of sentence:",sentence_count)
print("\n word frequency")
for word,count in frequency.items():
    print(f"{word}:{count}")