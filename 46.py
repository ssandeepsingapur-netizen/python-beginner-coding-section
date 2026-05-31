num = input("enter a multiple digit number")
frequency = {}

for digit in num:
    if digit.isdigit():
        frequency[digit] = frequency.get(digit, 0) + 1

print("\n --digit frequency--")
for digit, count in frequency.items():
    print("Digit " + digit + " occurs " + str(count) + " items")

