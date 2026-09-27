import csv
import os


FILE_NAME = "students.csv"
REPORT_FILE = "report.txt"


# ---------------------------------------------------------
# Create CSV file if it does not exist
# ---------------------------------------------------------

def initialize_file():

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Roll No",
                "Name",
                "Python",
                "Mathematics",
                "AI",
                "Database",
                "English"
            ])


# ---------------------------------------------------------
# Calculate percentage
# ---------------------------------------------------------

def calculate_percentage(marks):

    total = sum(marks)

    percentage = total / len(marks)

    return percentage


# ---------------------------------------------------------
# Calculate grade
# ---------------------------------------------------------

def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    elif percentage >= 40:
        return "E"

    else:
        return "F"


# ---------------------------------------------------------
# Get valid marks
# ---------------------------------------------------------

def get_marks(subject):

    while True:

        try:

            marks = float(
                input(f"Enter marks in {subject} (0-100): ")
            )

            if 0 <= marks <= 100:

                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:

            print("Please enter a valid number.")


# ---------------------------------------------------------
# Add student
# ---------------------------------------------------------

def add_student():

    print("\n")
    print("=" * 50)
    print("ADD STUDENT")
    print("=" * 50)

    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    python = get_marks("Python")
    mathematics = get_marks("Mathematics")
    ai = get_marks("Artificial Intelligence")
    database = get_marks("Database")
    english = get_marks("English")

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            roll_no,
            name,
            python,
            mathematics,
            ai,
            database,
            english
        ])

    print("\nStudent added successfully!")


# ---------------------------------------------------------
# Read all students
# ---------------------------------------------------------

def read_students():

    students = []

    try:

        with open(FILE_NAME, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                students.append(row)

    except FileNotFoundError:

        pass

    return students


# ---------------------------------------------------------
# Display all students
# ---------------------------------------------------------

def display_students():

    students = read_students()

    if not students:

        print("\nNo student records found.")

        return

    print("\n")
    print("=" * 90)
    print("STUDENT RECORDS")
    print("=" * 90)

    print(
        f"{'Roll':<8}"
        f"{'Name':<20}"
        f"{'Python':<10}"
        f"{'Math':<10}"
        f"{'AI':<10}"
        f"{'DB':<10}"
        f"{'English':<10}"
    )

    print("-" * 90)

    for student in students:

        print(
            f"{student['Roll No']:<8}"
            f"{student['Name']:<20}"
            f"{student['Python']:<10}"
            f"{student['Mathematics']:<10}"
            f"{student['AI']:<10}"
            f"{student['Database']:<10}"
            f"{student['English']:<10}"
        )


# ---------------------------------------------------------
# Analyze student
# ---------------------------------------------------------

def analyze_student():

    students = read_students()

    if not students:

        print("\nNo student records available.")

        return

    roll_no = input("\nEnter Roll Number: ")

    student_found = None

    for student in students:

        if student["Roll No"] == roll_no:

            student_found = student

            break

    if student_found is None:

        print("Student not found.")

        return

    marks = [
        float(student_found["Python"]),
        float(student_found["Mathematics"]),
        float(student_found["AI"]),
        float(student_found["Database"]),
        float(student_found["English"])
    ]

    percentage = calculate_percentage(marks)

    grade = calculate_grade(percentage)

    print("\n")
    print("=" * 50)
    print("STUDENT ANALYSIS")
    print("=" * 50)

    print("Roll Number :", student_found["Roll No"])
    print("Name        :", student_found["Name"])

    print("\nSubject Marks:")

    print("Python       :", marks[0])
    print("Mathematics  :", marks[1])
    print("AI           :", marks[2])
    print("Database     :", marks[3])
    print("English      :", marks[4])

    print("\nPercentage :", round(percentage, 2), "%")
    print("Grade      :", grade)

    # Weak subjects

    subjects = [
        "Python",
        "Mathematics",
        "AI",
        "Database",
        "English"
    ]

    weak_subjects = []

    for i in range(len(marks)):

        if marks[i] < 40:

            weak_subjects.append(subjects[i])

    if weak_subjects:

        print("\nWeak Subjects:")

        for subject in weak_subjects:

            print("-", subject)

    else:

        print("\nNo failed subjects.")


# ---------------------------------------------------------
# Class statistics
# ---------------------------------------------------------

def class_statistics():

    students = read_students()

    if not students:

        print("\nNo student records available.")

        return

    total_percentage = 0

    topper = None
    topper_percentage = -1

    passed = 0
    failed = 0

    for student in students:

        marks = [
            float(student["Python"]),
            float(student["Mathematics"]),
            float(student["AI"]),
            float(student["Database"]),
            float(student["English"])
        ]

        percentage = calculate_percentage(marks)

        total_percentage += percentage

        if percentage > topper_percentage:

            topper_percentage = percentage

            topper = student

        # Student passes only if every subject >= 40

        if min(marks) >= 40:

            passed += 1

        else:

            failed += 1

    average = total_percentage / len(students)

    print("\n")
    print("=" * 50)
    print("CLASS STATISTICS")
    print("=" * 50)

    print("Number of Students :", len(students))

    print("Class Average      :", round(average, 2), "%")

    print("Passed Students    :", passed)

    print("Failed Students    :", failed)

    print(
        "Pass Percentage    :",
        round((passed / len(students)) * 100, 2),
        "%"
    )

    if topper:

        print("\nClass Topper")

        print("Name       :", topper["Name"])

        print("Roll Number:", topper["Roll No"])

        print(
            "Percentage :",
            round(topper_percentage, 2),
            "%"
        )


# ---------------------------------------------------------
# AI-style performance prediction
# ---------------------------------------------------------

def performance_prediction():

    students = read_students()

    if not students:

        print("\nNo student records available.")

        return

    roll_no = input("\nEnter Roll Number: ")

    student = None

    for s in students:

        if s["Roll No"] == roll_no:

            student = s

            break

    if student is None:

        print("Student not found.")

        return

    marks = [
        float(student["Python"]),
        float(student["Mathematics"]),
        float(student["AI"]),
        float(student["Database"]),
        float(student["English"])
    ]

    average = calculate_percentage(marks)

    failed_subjects = 0

    for mark in marks:

        if mark < 40:

            failed_subjects += 1

    print("\n")
    print("=" * 50)
    print("PERFORMANCE PREDICTION")
    print("=" * 50)

    print("Student:", student["Name"])

    print("Current Average:", round(average, 2), "%")

    # Simple rule-based prediction

    if average >= 75 and failed_subjects == 0:

        prediction = "HIGH PERFORMER"

        recommendation = (
            "Student is performing very well. "
            "Maintain the current study pattern."
        )

    elif average >= 60 and failed_subjects == 0:

        prediction = "GOOD PERFORMANCE"

        recommendation = (
            "Performance is good. "
            "Additional practice can improve the score."
        )

    elif average >= 40 and failed_subjects <= 1:

        prediction = "MODERATE RISK"

        recommendation = (
            "Student should focus on weak subjects "
            "and increase practice time."
        )

    else:

        prediction = "HIGH RISK"

        recommendation = (
            "Student requires immediate academic support "
            "and additional practice."
        )

    print("\nPrediction :", prediction)

    print("Recommendation:")
    print(recommendation)


# ---------------------------------------------------------
# Generate report
# ---------------------------------------------------------

def generate_report():

    students = read_students()

    if not students:

        print("\nNo data available.")

        return

    with open(REPORT_FILE, "w") as file:

        file.write("=" * 60 + "\n")

        file.write(
            "       STUDENT PERFORMANCE ANALYSIS REPORT\n"
        )

        file.write("=" * 60 + "\n\n")

        file.write(
            "Total Students: "
            + str(len(students))
            + "\n\n"
        )

        total_average = 0

        topper_name = ""
        topper_percentage = -1

        for student in students:

            marks = [
                float(student["Python"]),
                float(student["Mathematics"]),
                float(student["AI"]),
                float(student["Database"]),
                float(student["English"])
            ]

            percentage = calculate_percentage(marks)

            grade = calculate_grade(percentage)

            total_average += percentage

            if percentage > topper_percentage:

                topper_percentage = percentage

                topper_name = student["Name"]

            file.write("-" * 60 + "\n")

            file.write(
                "Roll Number: "
                + student["Roll No"]
                + "\n"
            )

            file.write(
                "Name: "
                + student["Name"]
                + "\n"
            )

            file.write(
                "Percentage: "
                + str(round(percentage, 2))
                + "%\n"
            )

            file.write(
                "Grade: "
                + grade
                + "\n"
            )

        class_average = total_average / len(students)

        file.write("\n")
        file.write("=" * 60 + "\n")

        file.write(
            "Class Average: "
            + str(round(class_average, 2))
            + "%\n"
        )

        file.write(
            "Class Topper: "
            + topper_name
            + "\n"
        )

        file.write(
            "Topper Percentage: "
            + str(round(topper_percentage, 2))
            + "%\n"
        )

    print("\nReport generated successfully!")

    print("File:", REPORT_FILE)


# ---------------------------------------------------------
# Main menu
# ---------------------------------------------------------

def main():

    initialize_file()

    while True:

        print("\n")
        print("=" * 50)
        print("       STUDENT PERFORMANCE ANALYZER")
        print("=" * 50)

        print("1. Add Student")
        print("2. Display Students")
        print("3. Analyze Student")
        print("4. Class Statistics")
        print("5. Performance Prediction")
        print("6. Generate Report")
        print("7. Exit")

        print("=" * 50)

        choice = input("Enter your choice: ")

        if choice == "1":

            add_student()

        elif choice == "2":

            display_students()

        elif choice == "3":

            analyze_student()

        elif choice == "4":

            class_statistics()

        elif choice == "5":

            performance_prediction()

        elif choice == "6":

            generate_report()

        elif choice == "7":

            print("\nThank you for using Student Performance Analyzer!")

            break

        else:

            print("\nInvalid choice. Please try again.")


# ---------------------------------------------------------
# Start program
# ---------------------------------------------------------

if __name__ == "__main__":

    main()
