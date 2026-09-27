from analyzer import grade

def test_grades():
    assert grade(95) == "A+"
    assert grade(85) == "A"
    assert grade(75) == "B"
    assert grade(65) == "C"
    assert grade(55) == "D"
    assert grade(40) == "F"

if __name__ == "__main__":
    test_grades()
    print("All basic tests passed.")
