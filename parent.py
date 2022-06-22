# #parent class



# from tkinter import Y


# class Person(object):

#  #__init __is known as the constructor
#  def __init__(self,name,idnumber):
#         self.name = name
#         self.idnumber = idnumber




#  def display(self):
#       print(self.name)
#       print(self.idnumber)


# # def display(self):
# #     print(self.name)
# #     print(self.idnumber)

# def details(self):
#     # print("My name is {}".format(self.name))
#     print(f"My name is {self.name}")
#     print ("idnumber:{}".format (self.idnumber))


#     #childclass
# class Employee(Person):
#     def __init__(self,name,idnumber,salary,post):
#         self.salary = salary
#         self.post = post

#     #invoking the __init__ of the parent class
#         Person.__init__(self,name,idnumber)


#     def details(self):
#         print("My name is {}".format(self.name))
#         print("idnumber:{}".format(self.idnumber))
#         print("post:{}".format(self.post))


# #creation of an object variable or an instance
# y = "i want to make somethindklfiitykyhkgkfifof"
# a = Employee("Anny",908764,300000,y)

# #calling a function of the class person using #its instance
# a.display()
# a.details()

#parent class
class Student:
    def __int__(self,teacher,subject):
        self.teacher = teacher
        self.subject = subject

    def show(self):
        print(self.teacher)
        print(self.subject)
    

    def display(self):
        print("My class teachers name is {}".format(self.teacher))
        print("I offer these subject {}".format(self.subject))
        

#child class
class One(Student):
    def __init__(self,teacher,subject,number_student):
        self.number_student = number_student

        Student.__init__(self,teacher,subject)

    def display(self):
        print("My class teachers name is {}".format(self.teacher))
        print("I offer these subject {}".format(self.subject))
        
        print("number_student:{}".format(self.number_student))

y = One("Treasure","english",76)
y.show()
y.display()
    




    


        
    



    
