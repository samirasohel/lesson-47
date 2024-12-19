#Write a program to create a parent class Person (attributes - fname, lname) with a method 
# printname to display the full name. 
# Create a child class Student (attributes - fname, lname, year).
#  Access the attributes of parent class in child class using super() function. 
# Then, create an object for the child class and call the display method to display the full name. Also, print the graduation year.

#parent class

class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def printname(self):
        print("Name of the person is ",self.fname,self.lname)

#child class

class Student(person):
    def __init__(self,fname,lname,graduationyear):
        super().__init__(fname,lname)
        self.graduationyear=graduationyear

stud1=Student("Samira","sohel",2020)
stud1.printname()
print("{} war graduated in the year {}".format(stud1.fname,stud1.graduationyear))