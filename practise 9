def find_grade(marks):
    
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 50:
        return 'D'
    else:
        return 'Fail'


try:

    student_marks = float(input("Enter the student's marks (0-100): "))

    if 0 <= student_marks <= 100:
        grade = find_grade(student_marks)
        print(f"The student's grade is: {grade}")
    else:
        print("Error: Marks must be between 0 and 100.")

except ValueError:
    print("Error: Invalid input. Please enter a numerical value.")
output:Enter the student's marks (0-100): 95
The student's grade is: A+
