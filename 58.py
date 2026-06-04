students = []
n = int(input("enter the nmber of students:"))
for i in range(n):
    name = input("enter the name of student:")
    marks = float(input("enter the marks of students"))
    student = {"name":name,"marks":marks}
    students.append(student)

print("\n--Student Details--")
for student in students:
    print(f"Name: {student['name']} ,marks: {student['marks']}")

total = sum(student['marks'] for stuent in students)
averge = total/n

topper = max(students,key = lambda x:x['marks'])
lowest = min(students,key = lambda x:x['marks'])
print("\n--summary Report--")
print(f"averge marks: {averge : .2f}")
print(f"topper: {topper['name']} with marks {topper['marks']}")
print(f"lowest: {lowest['name']} with marks {lowest['marks']}")