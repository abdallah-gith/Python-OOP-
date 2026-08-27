class Grade:
    def __init__(self, score):
        self.score = score
        self.letter_grade = self.calculate_letter_grade()

    def calculate_letter_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"


class Enrollment:
    def __init__(self, enrollment_id, student, course):
        self.enrollment_id = enrollment_id
        self.student = student
        self.course = course
        self.grade = None

    def set_grade(self, score):
        self.grade = Grade(score)

    def display_info(self):
        print("Enrollment ID:", self.enrollment_id)
        print("Student:", self.student.name)
        print("Course:", self.course.title)

        if self.grade is not None:
            print("Score:", self.grade.score)
            print("Letter Grade:", self.grade.letter_grade)
        else:
            print("Grade: Not assigned")
