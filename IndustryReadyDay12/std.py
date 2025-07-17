""" Create a class Student
→ Attributes: name, marks (list)
 Method to calculate average and check if passed (pass mark = 40)"""
class student :
    def __init__(self,name,marks=[]):
        self.name = name
        self.marks = marks
    def average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)
    def is_passed(self):
        return self.average()>=40
std=student("John", [45, 55, 65])
print(f"Student Name: {std.name}")
print(f"Marks: {std.marks}")
print(f"Average Marks: {std.average()}")
print(f"Passed: {'Yes' if std.is_passed() else 'No'}")
print(std.is_passed())

        