import csv
from student_manager import DATA_FILE, ensure_file

def grade(percent):
    if percent >= 90:
        return "A+"
    if percent >= 80:
        return "A"
    if percent >= 70:
        return "B"
    if percent >= 60:
        return "C"
    if percent >= 50:
        return "D"
    return "F"

def analyze_students():
    ensure_file()
    with DATA_FILE.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    results = []
    for row in rows:
        marks = [float(row["maths"]), float(row["physics"]), float(row["python"])]
        total = sum(marks)
        percent = total / 3
        results.append({
            "roll_no": row["roll_no"],
            "name": row["name"],
            "total": total,
            "percentage": percent,
            "grade": grade(percent)
        })

    if not results:
        return {"results": [], "average": 0, "topper": None}

    average = sum(r["percentage"] for r in results) / len(results)
    topper = max(results, key=lambda x: x["percentage"])
    return {"results": results, "average": average, "topper": topper}
