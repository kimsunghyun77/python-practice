def get_student_data():
    subjects = []
    for i in range(3):
        subject = input(f"과목 {i+1}의 이름: ")
        subjects.append(subject)
    
    students = []
    for i in range(5):
        name = input(f"학생 {i+1}의 이름: ")
        scores = []
        for subject in subjects:
            score = float(input(f"{name}의 {subject} 점수: "))
            scores.append(score)
        students.append({"name": name, "scores": scores})
    return students, subjects

def calculate_grade(avg_score):
    if avg_score >= 90:
        return "A"
    elif avg_score >= 80:
        return "B"
    elif avg_score >= 70:
        return "C"
    elif avg_score >= 60:
        return "D"
    else:
        return "F"

def rank_students(students):
    ranked_students = sorted(students, key=lambda s: sum(s["scores"]) / len(s["scores"]), reverse=True)
    return ranked_students

def main():
    students, subjects = get_student_data()
    ranked_students = rank_students(students)
    
    print("\n학생 성적 결과")
    for idx, student in enumerate(ranked_students, start=1):
        avg_score = sum(student['scores']) / len(student['scores'])
        grade = calculate_grade(avg_score)
        print(f"{idx}등: {student['name']} (평균: {avg_score:.2f}점, 학점: {grade})")

if __name__ == "__main__":
    main()

