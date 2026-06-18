def solve(s):
    words = s.split()
    capital = []
    for word in words:
        if words.index(word) == 0:
            capital.append(word.capitalize())
        
        elif words.index(word) == 6:
            capital.append(word.capitalize())
        else:
            capital.append(word)  
    return capital
if __name__ == '__main__':  
    s = input()
    result = solve(s)
    print(result)