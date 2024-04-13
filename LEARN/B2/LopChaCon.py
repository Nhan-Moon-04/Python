class Person(object):
    def __init__(self, name, idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
    def detail(self):
        print("My name is {}".format(self.name))
        print("Idnumber is {}".format(self.idnumber))
        
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary=salary
        self.post=post
        
        #Goi init cua lop cha
        Person.__init__(self, name, idnumber)
    def detail(self):
        print("My name is {}".format(self.name))
        print("Idnumber is {}".format(self.idnumber))
        print("Salary is {}".format(self.salary))
        print("My post is {}".format(self.post))

nhan=Employee("Nguyen Thien Nhan", 2001223255, "13DHTH04", 12345)
nhan.display()
nhan.detail()