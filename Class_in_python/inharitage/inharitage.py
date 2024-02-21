class Person():
    def __init__(self,name,year) :
        self.Name = name
        self.Year = year

class Student(Person):
    def __init__(self, name, year,lesson):
        super().__init__(name, year)
        self.Lesson = lesson

student1 = Student("Julson", "2024","Python")
print(Student.name)
print(Student.year)
print(Student.lesson)