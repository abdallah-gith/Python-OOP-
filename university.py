from models import Student
from courses import Course, Department
from enrollment import Enrollment
class university:
    def __init__(self):
        self.students = []
        self.department = []
        self.courses = []
        self.enrollments = []
    def add_student(self, student) -> None:
        self.students.append(student)
    def add_department(self, department):
        self.department.append(department)
    def add_course(self, course):
        self.courses.append(course)
        if course.department is not None:
            course.department.add_course(course)
    def search_student(self, student_id):
        for student in self.students:
            if student.person_id == student_id:
                return student

        print("Student not found")
        return None

    def search_course(self, course_code):
        for course in self.courses:
            if course.course_code == course_code:
                return course

        print("Course not found")
        return None

    def enroll_student(self, student_id, course_code):
        student = self.search_student(student_id)
        course = self.search_course(course_code)

        if student is not None and course is not None:

            for enrollment in self.enrollments:
                if (
                    enrollment.student.person_id == student_id
                    and enrollment.course.course_code == course_code
                ):
                    print("Student is already enrolled in the course")
                    return

            enrollment_id = len(self.enrollments) + 1

            enrollment = Enrollment(
                enrollment_id,
                student,
                course
            )

            self.enrollments.append(enrollment)

            if not hasattr(student, "enrollments"):
                student.enrollments = []

            if not hasattr(course, "students"):
                course.students = []

            student.enrollments.append(enrollment)
            course.students.append(student)

            print("Student enrolled successfully")

    def remove_student_from_course(self, student_id, course_code):
        student = self.search_student(student_id)
        course = self.search_course(course_code)
        if student is None or course is None:
            return
        for enrollment in self.enrollments:
            if (enrollment.student == student and
                    enrollment.course == course):
                self.enrollments.remove(enrollment)
                if hasattr(student, "enrollments"):
                    student.enrollments.remove(enrollment)
                print("Student removed from course")
                return

        print("Enrollment not found")
    def assign_instructor_to_course(self, instructor, course_code):
        course = self.search_course(course_code)

        if instructor is not None and course is not None:

            if course.instructor is not None:
                print("Course already has an instructor")
                return

            course.instructor = instructor

            if not hasattr(instructor, "courses"):
                instructor.courses = []

            instructor.courses.append(course)

            print("Instructor assigned successfully")

    def record_grade(self, student_id, course_code, score):
        student = self.search_student(student_id)
        course = self.search_course(course_code)
        if student is None or course is None:
            return
        for enrollment in self.enrollments:
            if (
                enrollment.student.person_id == student_id
                and enrollment.course.course_code == course_code
            ):
                enrollment.set_grade(score)

                print("Grade recorded successfully")
                return

        print("Enrollment not found")

    def calculate_student_gpa(self, student_id):
        student = self.search_student(student_id)

        if student is None:
            return 0

        total_points = 0
        total_courses = 0
        for enrollment in student.enrollments:

            if enrollment.grade is not None:

                if enrollment.grade.letter_grade == "A":
                    total_points += 4

                elif enrollment.grade.letter_grade == "B":
                    total_points += 3

                elif enrollment.grade.letter_grade == "C":
                    total_points += 2

                elif enrollment.grade.letter_grade == "D":
                    total_points += 1
                elif enrollment.grade.letter_grade == "F":
                    total_points += 0
                total_courses += 1
        if total_courses == 0:
            return 0

        return total_points / total_courses