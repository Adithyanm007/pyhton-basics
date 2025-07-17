"""Person → Teacher/Student
Base class Person: name, age
Subclasses Teacher, Student with extra attributes (subject, grade)
Method to introduce themselves"""
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old.")
class teacher(person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject
    def greet(self):
        super().greet()
        print(f"I'm a teacher and i teach {self.subject}.")
class student(person):
    def __init__(self,name,age,subject,grade):
        super().__init__(name,age)
        self.subject=subject
        self.grade=grade
    def greet(self):
        super().greet()
        print(f"I'm a student studying {self.subject} in grade {self.grade}.")
t1=teacher("Alice", 30, "Mathematics")
t1.greet()
s1=student("Bob", 20, "Physics", "12th")
s1.greet()
p= person("Charlie", 25)
p.greet()

    
