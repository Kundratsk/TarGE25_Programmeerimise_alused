"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    def Empty(self):
        """Create empty object."""
        pass


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        """Initialize a person object."""
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname, lastname, age):
        """Initialize a Student object."""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    # empty usage
    empty_object = Empty()
    # 3 x person usage
    p1 = Person()
    p1.firstname = "John"
    p1.lastname = "Doe"
    p1.age = 20
    p2 = Person()
    p2.firstname = "Taat"
    p2.lastname = "Bataat"
    p2.age = 30
    p3 = Person()
    p3.firstname = "Peet"
    p3.lastname = "Tee"
    p3.age = 40
    # 3 x student usage
    Student1 = Student("Koomas", "Pang", 16)
    print(Student1.lastname)
    print(Student1.firstname)
    print(Student1.age)
    Student2 = Student("Poomas", "Kang", 13)
    print(Student2.lastname)
    print(Student2.firstname)
    print(Student2.age)
    Student3 = Student("Panedelnik", "Lang", 11)
    print(Student3.lastname)
    print(Student3.firstname)
    print(Student3.age)