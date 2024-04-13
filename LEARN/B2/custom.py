class Customer:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def Xuat(self):
        print(self.ten)
        print(self.tuoi)


nhan = Customer("Nguyen Thien Nhan", 19)
nhan.Xuat()
print("")
print('cac thuoc tinh co san cua class')
print("Nhan.dict",nhan.__dict__)
print("Nhan.doc",nhan.__doc__)
print("Nhan.class",nhan.__class__)
print("Nhan.class.name",nhan.__class__.__name__)