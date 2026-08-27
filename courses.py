class Department :
    def __init__(self, course, dept_id):
        self._dept_id = dept_id
        self.course = course
        self._courses = []
        self._instructors = []

    def add_course(self, course):
        if course not in self._courses:
            self._courses.append(course)
        else:
            print(f"Course {course} already exists in the department.")

    def remove_course(self, course):
        if course in self._courses:
            self._courses.remove(course)
        else:
            print(f"Course {course} does not exist in the department.")

    def add_instructor(self, instructor):
        if instructor not in self._instructors:
            self._instructors.append(instructor)
        else:
            print(f"Instructor {instructor} already exists in the department.")

    def remove_instructor(self, instructor):
        if instructor in self._instructors:
            self._instructors.remove(instructor)
        else:
            print(f"Instructor {instructor} does not exist in the department.")

    def display_department_info(self):
        print(f"Department ID: {self._dept_id}")
        print("Courses:")
        for course in self._courses:
            print(f"- {course.course_code}: {course.title}")
        print("Instructors:")
        for instructor in self._instructors:
            print(f"- {instructor.name}")


class Course: 
    def __init__(self, course_code, title, credit_hours, department = None):
        self.course_code = course_code
        self.title = title
        self.credit_hours = credit_hours
        self.department = department
        self.instructor = None


    def assign_instructor(self, instructor):
        if self.instructor is None:
            self.instructor = instructor
            instructor.assign_course(self)
        else:
            print(f"Course {self.course_code} already has an instructor assigned.")

    def remove_instructor(self):
        if self.instructor is not None:
            self.instructor.remove_course(self)
            self.instructor = None
        else:
            print(f"Course {self.course_code} does not have an instructor assigned.")

    def display_course_info(self):
        print(f"Course Code: {self.course_code}")
        print(f"Title: {self.title}")
        print(f"Credit Hours: {self.credit_hours}")
        if self.department:
            print(f"Department: {self.department._dept_id}")
        if self.instructor:
            print(f"Instructor: {self.instructor.name}")