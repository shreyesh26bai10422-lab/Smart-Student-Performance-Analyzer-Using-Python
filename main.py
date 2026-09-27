from student_manager import add_student, show_students
from analyzer import analyze_students
from report import print_report

def main():
    while True:
        print("\n--- Student Performance Analyzer ---")
        print("1. Add student")
        print("2. Show students")
        print("3. Analyze performance")
        print("4. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            data = analyze_students()
            print_report(data)
        elif choice == "4":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
