class Person:
    def __init__(self, person_id, name, age, contact_info):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.contact_info = contact_info

    def display_info(self):
        print(f"ID: {self.person_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Contact Info: {self.contact_info}")


class Student(Person):
    def __init__(self, person_id, name, age, contact_info, major):
        super().__init__(person_id, name, age, contact_info)
        self.major = major

    def display_student(self):
        self.display_info()
        print(f"Major: {self.major}")
