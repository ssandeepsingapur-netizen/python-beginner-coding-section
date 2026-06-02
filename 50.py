marks = []
print("enter 6 subject marks")
for i in range(6):
    m = int(input("enter marks of subject"))
    marks.append(m)

n = len(marks)
for i in range(n):
    for j in range(0,n-i-1):
        if marks[j]<marks[j+1]:
            marks[j], marks[j+1] = marks[j+1], marks[j]

print("Marks from highest to lowest")
for mark in marks:
    print(mark)