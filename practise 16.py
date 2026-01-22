number_of_terms = int(input("Enter the number of terms (greater than 2): "))

fibonacci_1 = 0
fibonacci_2 = 1

fibonacci_3 = fibonacci_1 + fibonacci_2

print("Fibonacci Series:")
print(fibonacci_1)
print(fibonacci_2)

i = 3
while True:
    print(fibonacci_3)
    fibonacci_1 = fibonacci_2
    fibonacci_2 = fibonacci_3
    fibonacci_3 = fibonacci_1 + fibonacci_2
    i += 1
    if i > number_of_terms:
        break
output:-
Enter the number of terms (greater than 2): 20
Fibonacci Series:
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181

=== Code Execution Successful ===
