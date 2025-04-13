 ##################

  #프로그램명: 객체 지향을 이용한 성적처리 프로그램

  #작성자: 자율전공학부/김성현

  #작성일: 4/13

  #프로그램 설명: class로 분류해서 과목과 점수를 입력받아 변수에 저장

  ###################

class Student:
    def __init__(self, student_id, name, eng, c_lang, python):
        self.student_id = student_id
        self.name = name
        self.eng = eng
        self.c_lang = c_lang
        self.python = python
        self.total = 0
        self.average = 0
        self.grade = ''
        self.rank = 1

        self.calculate_total_average()
        self.calculate_grade()

    def calculate_total_average(self):
        self.total = self.eng + self.c_lang + self.python
        self.average = self.total / 3

    def calculate_grade(self):
        avg = self.average
        if avg >= 90:
            self.grade = 'A'
        elif avg >= 80:
            self.grade = 'B'
        elif avg >= 70:
            self.grade = 'C'
        elif avg >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

    def __str__(self):
        return f"{self.student_id:<10}{self.name:<10}{self.eng:<5}{self.c_lang:<7}{self.python:<8}{self.total:<7}{self.average:<8.2f}{self.grade:<6}{self.rank:<5}"


class GradeManager:
    def __init__(self):
        self.students = []

    def input_student(self):
        student_id = input("학번: ")
        name = input("이름: ")
        eng = int(input("영어 점수: "))
        c_lang = int(input("C-언어 점수: "))
        python = int(input("파이썬 점수: "))
        student = Student(student_id, name, eng, c_lang, python)
        self.students.append(student)

    def calculate_ranks(self):
        for s in self.students:
            s.rank = 1
            for other in self.students:
                if other.total > s.total:
                    s.rank += 1

    def print_students(self):
        print("\n학번       이름       영어  C-언어  파이썬  총점   평균     학점  등수")
        print("------------------------------------------------------------------")
        for s in self.students:
            print(s)

    def insert_student(self, student):
        self.students.append(student)

    def delete_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]

    def search_by_id(self, student_id):
        return [s for s in self.students if s.student_id == student_id]

    def search_by_name(self, name):
        return [s for s in self.students if s.name == name]

    def sort_by_total(self):
        self.students.sort(key=lambda x: x.total, reverse=True)

    def count_above_80(self):
        return len([s for s in self.students if s.average >= 80])


def main():
    gm = GradeManager()

    print("학생 정보 입력 (총 5명)")
    for _ in range(5):
        gm.input_student()

    gm.calculate_ranks()
    gm.sort_by_total()
    gm.print_students()

    print("\n80점 이상 평균 학생 수:", gm.count_above_80())

    print("\n[학번으로 탐색] 학번이 '202301'인 학생:")
    found = gm.search_by_id('202301')
    for s in found:
        print(s)

    print("\n[학생 삭제] 학번이 '202301'인 학생 삭제 후 출력:")
    gm.delete_student('202301')
    gm.calculate_ranks()
    gm.sort_by_total()
    gm.print_students()


if __name__ == "__main__":
    main()