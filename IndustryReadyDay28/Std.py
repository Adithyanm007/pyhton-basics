"""Try building a class Student:
private: __grades (list)
public: add_grade(), average(), get_grades()"""
class Student:
    def __init__(self,name,grade=[]):
        self.name = name
        self.__grades = grade
    def add_grade(self,grade):
        if 0 <=grade<=100:
            self.__grades.append(grade)
            print(f"Added grade {grade} for {self.name}.")
        else:
            print("Invalid grade. Must be between 0 and 100.")
    def average(self):
            if self.__grades==[]:
                return 0
            return sum(self.__grades)/len(self.__grades)
    def get_grades(self):
            return self.__grades.copy()
student = Student("Alice")
print(f"Grades for {student.name}: {student.get_grades()}")
student.add_grade(-85)   
student.add_grade(90)
student.add_grade(78)
print(f"Average grade for {student.name} is {student.average()}")
print(f"Grades for {student.name}: {student.get_grades()}")