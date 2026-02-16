# Improved Student Marks Management System

while True:
    print("\n----- Student Marks Management System -----")

    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")

    marks = []
    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Enter marks for Subject {i}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter numeric value.")

    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print("\n----- Result -----")
    print("Student Name:", name)
    print("Roll Number:", roll_no)
    print("Total Marks:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)

    again = input("\nDo you want to enter another student? (yes/no): ")
    if again.lower() != "yes":
        print("Program Ended.")
        break
