#Write a program to create a parent class Person (attributes - name, idnumber) with a method 
# display to display the attributes. Create a child class Employee (attributes - name, idnumber, salary, post).
#  Access the attributes of parent class in child class. 
# Then, create an object for child class and call the display method to display the name and idnumber.

#parent class

class person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber

    def display(self):
        print("Name of the person is{} and idnumber is {} ".format(self.name,self.idnumber))

#child class

class Employee(person):
    def __init__(self, name, idnumber,salary,post):
        person.__init__(self,name,idnumber)
        self.salary=salary
        self.post=post

emp1=Employee("Samira",1234,20000,"Intern")
emp1.display()

print("{} has salary {} and post is {} ".format(emp1.name,emp1.salary,emp1.post))