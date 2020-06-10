class Student:
    def__init__(self,n,g):
        self.name=name
        self.grade=grade


    def display(self):
        return self.name+"got grade" + self.grade

stu=Student("John","B")
print("Name:",stu.name)
print("Grade:",stu.grade)
print(stu.display)

##
class Person:
    @staticmethod
    def hello():
        print("hello world")


per=Person()
per.hello
Person.hello()