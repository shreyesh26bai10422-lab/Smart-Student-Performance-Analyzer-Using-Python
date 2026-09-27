import csv
from pathlib import Path

DATA_FILE = Path("students.csv")

def ensure_file():
    if not DATA_FILE.exists():
        DATA_FILE.write_text("roll_no,name,maths,physics,python\n", encoding="utf-8")

def add_student():
    ensure_file()
    roll = input("Roll number: ").strip()
    name = input("Name: ").strip()
    marks = []
    for subject in ["Maths", "Physics", "Python"]:
        while True:
            try:
                value = float(input(f"{subject} marks (0-100): "))
                if 0 <= value <= 100:
                    marks.append(value)
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Enter a number.")
    with DATA_FILE.open("a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([roll, name, *marks])
    print("Student added successfully.")

def show_students():
    ensure_file()
    with DATA_FILE.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("No student records found.")
        return
    for row in rows:
        print(row)
