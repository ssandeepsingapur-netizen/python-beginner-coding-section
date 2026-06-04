import csv

def read_csv(filename):
    data = []
    with open(filename, mode= 'r')as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
        return data

def get_column_values(data, column):
    values = []
    for row in data:
        try:
            values.append(float(row[column]))
        except:
            pass
    return values

filename = input("Enter the CSV file name:")
try:
    data = read_csv(filename)
    print(data)
    print("\nAvailable columns:")
    if data:
        print(data[0].keys())
    else:
        print("No data found in the CSV file.")
    while True:
        print("\n--summary Menu--")
        print("1.Maximum")
        print("2.minimum")
        print("3.Averge")
        print("4.Exit")
        choice = input("Enter your choice")
        if choice == '4':
            print("Program ended")
            break
        column = input("Enter the column name:")
        values = get_column_values(data, column)
        if not values:
            print("Invalid column or non-numeric data.")
            continue
        if choice == '1':
            print(f"Maximum value in {column}: {max(values)}")
        elif choice == '2':
            print(f"Minimum value in {column}: {min(values)}")
        elif choice == '3':
            averge = sum(values)/len(values)
            print(f"Averge value in:",averge)
        else:
            print("Invalid choice. Please try again.")
except FileNotFoundError:
    print("CSV file not found!")
    