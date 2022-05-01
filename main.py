import sys
from functions import convert, get_input

units = ["m", "cm", "mm", "km", "mi", "in", "ft", "yd", "miles"]

def display_menu():
    # Display a nice and simple menu
    print('Welcome to the unit converter!')
    print('Here are the available units:')
    for unit in units:
        print(f"- {unit}")

def main():
    # Main program
    display_menu()
    unit_from, unit_to, amount = get_input()

    # Check if amount is a number
    try:
        amount = float(amount)
    except ValueError:
        print('Amount must be a number')
        sys.exit()

    # Check if unit_from and unit_to are valid
    if unit_from not in units or unit_to not in units:
        print(f'"{unit_from}" and "{unit_to}" are not valid units')
        sys.exit()

    result = convert(unit_from, unit_to, amount)
    print(f"{amount} {unit_from} is {result} {unit_to}")


if __name__ == '__main__':
    main()