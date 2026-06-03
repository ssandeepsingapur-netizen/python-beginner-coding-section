num = input("enter multiple number")
numbers = []

for digit in num:
    
    if digit in digit:
        if digit in frequency:
            frequency[digit]+=1
    
    else:
        frequency[digit]= 1
    
for digit,count frequency.items:
    print("number"+str(digit)+"occurs"+str(sount))