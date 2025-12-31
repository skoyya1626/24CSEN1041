def find_length(number):
  

  num_str = str(abs(number))
  return len(num_str)


num1 = 12345
num2 = -678

length1 = find_length(num1)
length2 = find_length(num2)


print(f"The number {num1} has a length of: {length1} digits")
print(f"The number {num2} has a length of: {length2} digits")
output:the no 12345 has a lenght of:5 digits
       the no -678 has a lenght of: 3 digits

