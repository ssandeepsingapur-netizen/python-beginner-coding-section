text = input("enter the paragraph")
text_lower = text.lower()
words = text.split()
words_count = len(words)
char_count =len(text)
sentence_count = text.count(".")+text.count("!")+text.count("?")

longest_word = max(words , key = len)
frequency = {}
for word in words:
    word= word.strip(", !  ?")
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word] = 1

print("text analysis")
print("words count",words_count)
print("char count",char_count)
print("sentence count",sentence_count)
print("longest word",longest_word)
print("\n frequency of word")
for word,count in frequency.items():
    print(word,":",count)