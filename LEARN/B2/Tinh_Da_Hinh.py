class person:
    def normal(self):
        print("Toi la nguoi thuong")
    def super(self):
        print("Toi la siu nhan")
class animal:
    def normal(self):
        print("Toi la dong vat binh thuong")
    def super(self):
        print("Toi la siu dong vat")
def test_super(test):
    test.normal()
    
nhan=person()
meo=animal()
test_super(nhan)
test_super(meo)