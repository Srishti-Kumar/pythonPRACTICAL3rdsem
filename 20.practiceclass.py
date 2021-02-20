'''
class student:      #class student is created
    x=5

p1 = student()      #object p1 is created
print(p1.x)         #print x




class student:
  def __init__(self, name , city):
      self.name = name
      self.city = city


p1 = student('srishti', 'gurgaon')

print(p1.name)
print(p1.city)




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

'''

