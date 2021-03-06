def convert(unit_from, unit_to, amount):
    if unit_from == "m":
        if unit_to == "cm":
            return amount * 100
        elif unit_to == "mm":
            return amount * 1000
        elif unit_to == "km":
            return amount / 1000
        elif unit_to == "mi":
            return amount / 1609.34
        elif unit_to == "in":
            return amount * 39.3701
        elif unit_to == "ft":
            return amount * 3.28084
        elif unit_to == "yd":
            return amount * 1.09361
        elif unit_to == "miles":
            return amount / 1609.34
    elif unit_from == "cm":
        if unit_to == "m":
            return amount / 100
        elif unit_to == "mm":
            return amount * 10
        elif unit_to == "km":
            return amount / 100000
        elif unit_to == "mi":
            return amount / 160934
        elif unit_to == "in":
            return amount * 0.393701
        elif unit_to == "ft":
            return amount * 0.0328084
        elif unit_to == "yd":
            return amount * 0.0109361
        elif unit_to == "miles":
            return amount / 160934
    elif unit_from == "mm":
        if unit_to == "m":
            return amount / 1000
        elif unit_to == "cm":
            return amount / 10
        elif unit_to == "km":
            return amount / 1000000
        elif unit_to == "mi":
            return amount / 1609000
        elif unit_to == "in":
            return amount * 0.0393701
        elif unit_to == "ft":
            return amount * 0.00328084
        elif unit_to == "yd":
            return amount * 0.00109361
        elif unit_to == "miles":
            return amount / 1609000
    elif unit_from == "km":
        if unit_to == "m":
            return amount * 1000
        elif unit_to == "cm":
            return amount * 100000
        elif unit_to == "mm":
            return amount * 1000000
        elif unit_to == "mi":
            return amount / 1.60934
        elif unit_to == "in":
            return amount * 39370.1
        elif unit_to == "ft":
            return amount * 3280.84
        elif unit_to == "yd":
            return amount * 1093.61
        elif unit_to == "miles":
            return amount / 1.60934
    elif unit_from == "mi":
        if unit_to == "m":
            return amount * 1609.34
        elif unit_to == "cm":
            return amount * 1609000
        elif unit_to == "mm":
            return amount * 1609000
        elif unit_to == "km":
            return amount * 1.60934
        elif unit_to == "in":
            return amount * 63360
        elif unit_to == "ft":
            return amount * 5280
        elif unit_to == "yd":
            return amount * 1760
        elif unit_to == "miles":
            return amount
    elif unit_from == "in":
        if unit_to == "m":
            return amount * 0.0254
        elif unit_to == "cm":
            return amount * 2.54
        elif unit_to == "mm":
            return amount * 25.4
        elif unit_to == "km":
            return amount * 0.0000254
        elif unit_to == "mi":
            return amount * 0.0000157828
        elif unit_to == "ft":
            return amount * 0.0833333
        elif unit_to == "yd":
            return amount * 0.0277778
        elif unit_to == "miles":
            return amount * 0.0000157828
    elif unit_from == "ft":
        if unit_to == "m":
            return amount * 0.3048
        elif unit_to == "cm":
            return amount * 30.48
        elif unit_to == "mm":
            return amount * 304.8
        elif unit_to == "km":
            return amount * 0.0003048
        elif unit_to == "mi":
            return amount * 0.000189394
        elif unit_to == "in":
            return amount * 12
        elif unit_to == "yd":
            return amount * 0.333333
        elif unit_to == "miles":
            return amount * 0.000189394
    elif unit_from == "yd":
        if unit_to == "m":
            return amount * 0.9144
        elif unit_to == "cm":
            return amount * 91.44
        elif unit_to == "mm":
            return amount * 914.4
        elif unit_to == "km":
            return amount * 0.0009144
        elif unit_to == "mi":
            return amount * 0.000568182
        elif unit_to == "in":
            return amount * 36
        elif unit_to == "ft":
            return amount * 3
        elif unit_to == "miles":
            return amount * 0.000568182
    elif unit_from == "miles":
        if unit_to == "m":
            return amount * 1609.34
        elif unit_to == "cm":
            return amount * 1609000
        elif unit_to == "mm":
            return amount * 1609000
        elif unit_to == "km":
            return amount * 1.60934
        elif unit_to == "mi":
            return amount
        elif unit_to == "in":
            return amount * 63360
        elif unit_to == "ft":
            return amount * 5280
        elif unit_to == "yd":
            return amount * 1760

def get_input():
    # Get the user input
    unit_from = input('From unit: ')
    unit_to = input('To unit: ')
    amount = input('Amount: ')
    return unit_from, unit_to, amount