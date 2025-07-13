while True:
    score = int(input("請輸入成績:"))
    grade = None

    if 0 <= score < 60:
        grade = "F"
    elif score < 70:
        grade = "D"
    elif score < 80:
        grade = "C"
    elif score < 90:
        grade = "B"
    elif score < 95:
        grade = "A"
    else:
        grade = "SS"

    print(f"score : {score}, and grade : {grade}")

    if score == -1:
        break
