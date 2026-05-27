students = []
n = int(input("Enter the number of students: "))
for i in range(n):
    name = input("enter the name of student: ")
    marks = int(input("enter the marks of student: "))
    student = {"name": name, "marks": marks}
    students.append(student)

print("\n--students details--")
for student in students:
    print(f"Name: {student['name']}, Marks: {student['marks']}")

total = sum(student['marks'] for student in students)
averge = total/n
topper = max(students, key=lambda x: x['marks'])
lowest = min(students, key=lambda x: x['marks'])
print("\n--summary report--")
print(f"Averge marks: {averge:2f}")
print(f"Topper: {topper['name']} with marks {topper['marks']}")
print(f"lowest scorer :{lowest['name']} with marks {lowest['marks']}")
