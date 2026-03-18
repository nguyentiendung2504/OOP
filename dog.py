class Dog:

    def __init__(self, ten, giong, mausac, camxuc):
        self.ten = ten
        self.giong = giong
        self.mausac = mausac
        self.camxuc = camxuc

    def sua(self):
        print("gau gau")

    def chay(self):
        print("dang chay")

    def an(self):
        print("dang an")


dog1 = Dog("Milu", "Poodle", "Trang", "Vui")

dog1.sua()
dog1.chay()
dog1.an()