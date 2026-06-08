file = open("file1.txt", mode = "r")
text = file.read()
file.close()
text = text.lower()
words = text.split()
freq = {}
for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word] = 1

sorted_freq = sorted(freq.items(),key = lambda x: x[1],reverse=True)
print("top 10 most frequenty words")
for i in range(10):
    print(f"{sorted_freq[i][0]}:{sorted_freq[0][1]}")
