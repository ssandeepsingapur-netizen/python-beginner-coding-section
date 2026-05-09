students = int(input("enter number of students"))
hungry = bool(False)

if students>= 90:
    print('Today we make biryani')
elif students>= 80:
    if hungry== True:
        print("today also make biryani")
    else: 
        print("today making uppito")

elif students>=60:
    print("today number of student less so we make rice and sambar")
elif students>=50:
    print("today we not make food so please eat outside")