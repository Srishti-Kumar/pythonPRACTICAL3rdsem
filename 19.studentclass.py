class student:
    marks = []
    # Constructor
    def getdata(self,rollno,name,course,m1,m2,m3):
        self.rollno = rollno
        self.name = name
        self.course = course
        self.marks.append(m1)
        self.marks.append(m2)
        self.marks.append(m3)

    def displaydata(self):
        print("RollNo : ", self.rollno)
        print("Name   : ", self.name)
        print("Marks are : ", student.marks)
        print("\n")

    def total(self):
        return (student.marks[0]+student.marks[0]+student.marks[0])

rollno=int(input("enter the roll no: "))
name=input("enter the name: ")
course=input("enter the course: ")
m1=int(input("enter the marks in first subject: "))
m2=int(input("enter the marks in second subject: "))
m3=int(input("enter the marks in third subject: "))

s1 = student()
s1.getdata(rollno,name,course,m1,m2,m3)
s1.displaydata()
print("aggregate/total Marks out of 300 are: ", s1.total())




