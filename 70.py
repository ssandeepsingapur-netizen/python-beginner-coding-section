num = input("enter multi digit number")
frequency = {}
for digit in num:
    if digit.isdigit():
        if digit in frequency:
            frequency[digit]+=1
        else:
            frequency[digit] = 1

print("\n ---frequency analysis---")
for digit,count in frequency.items():
    print("digit"+str(digit)+"occurs"+str(count)+"items")