def convert_to_base(num, base):
    # Handle zero as a special case
    if num == 0:
        return "0"

    digits = []
    temp = num
    while temp > 0:
        digits.append(str(temp % base))
        temp //= base

    # Since digits are collected in reverse, reverse them before joining
    digits.reverse()
    return ''.join(digits)


# Main program
num = int(input("Enter a number: "))
base = int(input("Enter the base: "))

converted = convert_to_base(num, base)
print(f"The number {num} in base {base} is: {converted}")

output: Enter a number: 500
Enter the base: 16
The number 500 in base 16 is: 1154
