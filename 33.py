name = input("enter name of student")
marks = input("Enter numbers separated by space: ")

marks_list = marks.split() 
print(marks_list)   # splits string into list

total = sum(map(int, marks_list))   # convert to int + sum

print("Total =", total)
