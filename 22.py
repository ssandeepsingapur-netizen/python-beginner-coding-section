def count(string,substring):
    count = 0
    for i in range(len(string)-len(substring)+1):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count

string = input("Enter the string: ")
substring = input("Enter the substring: ")
print(count(string, substring))