"""Simple class."""

class Teacher:

    def __init__(self):
        super().__init__()
        self.school = "Tallinna Tööstushariduskeskus"
        self.group = []
        self.subjects = []


class Student:
    """Loon uue klassi"""

    def __init__(self, name="Anonymous", finished=False):
        self.name = name
        self.finished = finished


if __name__ == '__main__':
    student_1 = Student()
    student = Student("John")
    print(student.name)  # John
    print(student.finished)  # False
