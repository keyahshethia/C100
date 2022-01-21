class Student(object):
    def __init__(self,name,age,gender,level,grades=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}
    
    def setGrade(self,course,grade):
        self.grades[course] = grade
    
    def setGrade(self,course):
        return self.grades[course]

    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)

keyah = Student("Keyah",14,"female",9,{"math":4.5})
anshu = Student("Anshu",24,"female",15,{"math":3.5})

print(keyah.getGPA())
print(anshu.getGPA())