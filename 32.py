name  =  input("enter your name")
roll_no = int(input("enter roll number"))
subject = int(input("enter number of subjects"))
total = 0
for i in range(subject): 
    subject_name =input(" enter name of subjec")
    Marks = int(input("enter marks of subject"))
    total = total+Marks

print("Name:",name)
print("Roll_no",roll_no)
print("total marks:",total)
if total>=90:
    print("student get schlorship maximum")
elif tptal>=80:
    print("student eligible schlorship minimum")
else:
    print(" student difficult get schlorship")
    


    


