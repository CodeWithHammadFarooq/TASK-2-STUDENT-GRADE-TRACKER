# Student Grade Tracker

# Function to calculate average grade
def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

# Main program
def main():
    student_name = input("Enter the student's name: ")
    grades = []

    while True:
        try:
            grade = float(input(f"Enter a grade for {student_name} (or type 'done' to finish): "))
            grades.append(grade)
        except ValueError:
            break  # Exit loop when user types 'done' or anything that isn't a number

    average_grade = calculate_average(grades)

    print(f"\n{student_name}'s Grade Report:")
    print(f"Total Grades: {grades}")
    print(f"Average Grade: {average_grade:.2f}")

if __name__ == "__main__":
    main()
