class Person:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        return f"Person name: {self.name}"


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.__student_id = student_id  # encapsulation

    def get_info(self):  # polymorphism
        return f"Student name: {self.name}, ID: {self.__student_id}"


person = Person("John")
student = Student("Alice", "S123")

print(person.get_info())
print(student.get_info())
