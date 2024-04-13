class person:
    def __init__(self, name, age=1,gender="male"):
        self.name=name
        self.age=age
        self.gender=gender
        
    def show_infor(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
    
nhan=person("Nguyen Thien Nhan", 19, "Male")
nhan.show_infor()
print("----------------------")