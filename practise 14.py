a = 50
b = 20

# Arithmetic Operators
print("Arithmetic Operators")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")   # Float division for clarity
print(f"{a} % {b} = {a % b}\n")

# Relational Operators
print("Relational Operators")
print(f"{a} < {b} = {a < b}")
print(f"{a} > {b} = {a > b}")
print(f"{a} == {b} = {a == b}")
print(f"{a} != {b} = {a != b}\n")

# Logical Operators
print("Logical Operators")
print(f"AND {a} and {b} = {bool(a and b)}")
print(f"OR {a} or {b} = {bool(a or b)}")
print(f"NOT {a} = {not a}\n")

# Bitwise Operators
print("Bitwise Operators")
print(f"{a} & {b} = {a & b}")
print(f"{a} | {b} = {a | b}")
print(f"Bitwise XOR {a} ^ {b} = {a ^ b}")
print(f"Left Shift {a} << 2 = {a << 2}")
print(f"Right Shift {a} >> 2 = {a >> 2}")

# Conditional (Ternary) Operator
print("\n" + ("a is greater than b" if a > b else "b is less than a"))

output:-
Arithmetic Operators
50 + 20 = 70
50 - 20 = 30
50 * 20 = 1000
50 / 20 = 2.50
50 % 20 = 10

Relational Operators
50 < 20 = False
50 > 20 = True
50 == 20 = False
50 != 20 = True

Logical Operators
AND 50 and 20 = True
OR 50 or 20 = True
NOT 50 = False

Bitwise Operators
50 & 20 = 16
50 | 20 = 54
Bitwise XOR 50 ^ 20 = 38
Left Shift 50 << 2 = 200
Right Shift 50 >> 2 = 12

a is greater than b

=== Code Execution Successful ===
