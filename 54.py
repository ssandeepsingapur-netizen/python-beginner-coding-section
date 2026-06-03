import csv as CSV

# ----------------------------
# Read and process CSV
# ----------------------------

def read_csv(filename: str) -> list[dict]:
    """Read a CSV file into a list of dictionaries.

    Each row becomes a dict like: {"column_name": "value_as_string", ...}
    """
    data: list[dict] = []

    # Open the file and let DictReader map header names -> values.
    with open(filename, mode="r") as file:
        reader = CSV.DictReader(file)
        for row in reader:
            data.append(row)

    return data


def get_column_values(data: list[dict], column: str) -> list[float]:
    """Extract numeric values from a specific column.

    - If the column name doesn't exist, or
    - If a cell can't be converted to float,

    then that value is skipped.
    """
    values: list[float] = []

    for row in data:
        try:
            # DictReader returns strings; convert to float.
            values.append(float(row[column]))
        except (KeyError, TypeError, ValueError):
            # Skip invalid/missing data.
            pass

    # BUGFIX: return must be outside the loop.
    return values


# ----------------------------
# User interface (menu)
# ----------------------------

filename = input("enter the CSV filename:")

try:
    data = read_csv(filename)

    print("\n available columns:")

    # Guard against an empty CSV.
    if not data:
        print("CSV is empty")
        raise SystemExit

    # Print column headers.
    print(data[0].keys())

    while True:
        print("\n--summary menu--")
        print("1 maximum")
        print("2 minimum")
        print("3 average")
        print("4 exit")

        choice = int(input("enter your choice"))

        # Exit option.
        if choice == 4:
            print("exiting program")
            break

        # Column name requested from the user.
        column = input("enter the column name:")

        # Convert the chosen column into numeric values.
        values = get_column_values(data, column)

        # If nothing numeric was found, tell the user and restart the menu.
        if not values:
            print("no valid data found in column")
            continue

        # Print summary based on user choice.
        if choice == 1:
            print(f"maximum value in {column} is {max(values)}")
        elif choice == 2:
            print(f"minimum value in {column} is {min(values)}")
        elif choice == 3:
            avg = sum(values) / len(values)
            print(f"average value in {column} is {avg:.2f}")
        else:
            print("invalid choice try again")

except FileNotFoundError:
    print("file not found please check the filename and try again")

