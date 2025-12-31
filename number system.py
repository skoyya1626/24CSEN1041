def convert_number(num, base):
    if num == 0:
        return "0"
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    is_negative = num < 0
    num = abs(num)
    
    while num > 0:
        remainder = num % base
        result = digits[remainder] + result
        num //= base
    
    if is_negative:
        result = "-" + result
    
    return result

number = int(input("Enter a decimal number: "))
base = int(input("Enter the base (2–36): "))

if 2 <= base <= 36:
    converted = convert_number(number, base)
    print(f"Number in base {base}: {converted}")
else:
    print("Base must be between 2 and 36.")
  output: Enter a decimal number: 56874
Enter the base (2–36): 2
Number in base 2: 1101111000101010
