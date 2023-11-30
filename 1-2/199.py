import math

def roman_to_int(s):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    result = 0
    prev_value = 0
    
    for symbol in s[::-1]:
        value = roman_values[symbol]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result

def int_to_roman(arabic):
    if not 0 < arabic < 4000:
        raise ValueError()

    roman_numerals = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    roman_numeral = ""
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        while arabic >= value:
            roman_numeral += numeral
            arabic -= value

    return roman_numeral

try:
    f, s = [roman_to_int(r) for r in input().split("/")]
except:
    print("ERROR")
    exit()


nod = math.gcd(f, s)
f, s = f // nod, s // nod
if s == 1:
    print(int_to_roman(f))
else:
    print(int_to_roman(f), "/", int_to_roman(s), sep="")
