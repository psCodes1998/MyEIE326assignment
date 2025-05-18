grade_to_points = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'F': 1
}

def compute_gpa():
    total_weighted_points = 0
    total_units = 0

    print("Enter the course details for 6 courses:")

    for i in range(1, 7):
        print(f"\nCourse {i}:")
        while True:
            try:
                units = int(input("Enter number of units: "))
                if units <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a positive integer for units.")
        
        while True:
            grade = input("Enter grade (A/B/C/D/F): ").strip().upper()
            if grade in grade_to_points:
                break
            else:
                print("Invalid grade. Please enter one of A, B, C, D, F.")

        points = grade_to_points[grade]
        total_weighted_points += points * units
        total_units += units

    gpa = total_weighted_points / total_units
    print(f"\nYour GPA on a 5.0 scale is: {gpa:.2f}")

compute_gpa()
