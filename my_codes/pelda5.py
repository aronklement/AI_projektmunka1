# Write a function that performs Celsius ↔ Fahrenheit conversion.

def CF_converter(temp_number, temp_type):
    if temp_type.upper() == 'C':
        print(f"{temp_number}°C => {(int(temp_number * 9 / 5) + 32)}°F")
        return (int(temp_number * 9 / 5) + 32)
    elif temp_type.upper() == 'F':
        print(f"{temp_number}°F => {(int(temp_number - 32) / 9 * 5)}°C")
        return (int(temp_number - 32) / 9 * 5)
    else:
        print(f"Wrong temp_type({temp_type})!")

print(CF_converter(100, 'C'))