from models import Person, Student
from courses import Course, Department
from enrollment import Enrollment
from university import university

def main():
    uni = university()
    student1 = Student(1,"Ahmed",20,"01012345678","Artificial Intelligence")
    student2 = Student(2,"Omar",21,"01198765432","Computer Science")

    uni.add_student(student1)
    uni.add_student(student2)

    department = Department(None, "AI01")
    uni.add_department(department)
    course1 = Course("AI101","Introduction to Artificial Intelligence",3,department)
    course2 = Course("CS101","Programming Fundamentals",3,department)

    uni.add_course(course1)
    uni.add_course(course2)

    instructor = Person(100,"Dr. Ahmed Hassan",40,"ahmed@university.edu")
    department.add_instructor(instructor)
    
    uni.assign_instructor_to_course(instructor,"AI101")
    uni.enroll_student(1, "AI101")
    uni.enroll_student(1, "CS101")
    uni.enroll_student(2, "AI101")
    uni.record_grade(1, "AI101", 95)
    uni.record_grade(1, "CS101", 85)
    uni.record_grade(2, "AI101", 75)
    print("\n========== STUDENT 1 ========")
    student1.display_student()
    print("\n========== STUDENT 2 =========")
    student2.display_student()
    print("\n========== COURSE 1 ========")
    course1.display_course_info()
    print("\n======== COURSE 2 ==========")
    course2.display_course_info()
    print("\n========== ENROLLMENTS =======")
    for enrollment in uni.enrollments:
        enrollment.display_info()
        print()
    print("========== DEPARTMENT =======")
    department.display_department_info()
    print("\n========== GPA ========")
    gpa1 = uni.calculate_student_gpa(1)
    gpa2 = uni.calculate_student_gpa(2)
    print(f"Ahmed GPA: {gpa1:.2f}")
    print(f"Omar GPA: {gpa2:.2f}")
    print("\n======== REMOVE STUDENT ==========")
    uni.remove_student_from_course(1, "CS101")
    print("\n========== ENROLLMENTS AFTER REMOVAL ========")
    for enrollment in uni.enrollments:
        enrollment.display_info()
        print()
if __name__ == "__main__":
    main()