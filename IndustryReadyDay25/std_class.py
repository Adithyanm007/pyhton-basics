class Student:
    def __init__(self,name,grade,school):
        self.name = name
        self.grade = grade
        self.school = school
    def __str__(self):
        return f"Student Name: {self.name}, Studies in: {self.school}, Grade: {self.grade}"
std=Student("John Doe", "10th", "Springfield High")
print(std)
        