students = []
n = int(input("enter number of students"))

for i in range(n):
    name = input("enter the name")
    marks = float(input("enter the marks"))
    student = {"name" : name,"marks": marks}
    students.append(student)

print("---records of students")
for student in students:
    print(f"name: {student['name']},marks :{student['marks']}")

total = sum(student['marks'] for student in students)
averge = total/n
topper = max(students,key = lambda x:x['marks'])
lowest = min(students,key = lambda x:x['marks'])

print('---student report---- ')
print(f"topper {topper['name']}, marks {topper['marks']}")
print(f"lowest{lowest['name']},marks{lowest['marks']}")
print("averge marks:",averge)