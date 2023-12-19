class Student:
    count_st = 0
    def __init__(self,name:str, course:int):
        self.name = name
        self.course = course
        Student.count_st += 1
    def __str__(self):
        return f"(На даний момент кількість студентів - {Student.count_st})"


misha = Student("Misha",2)
petja = Student("Petja",3)
oksana = Student("Oksana",3)
print(misha)