def merge_the_tools(string, k):
    # your code goes here
    words = string.split()
    for word in words:
        if word in words:
            unique_word = set(word)
        else:
            unique_word = word
    for i in range(k):
        print(unique_word[ : :2])

        
if __name__ == '__main__':
    string = input()
    k = int(input())
    merge_the_tools(string, k)