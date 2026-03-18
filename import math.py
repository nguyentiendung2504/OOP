import math

class Point:
    """Represents a point in 2D geometry"""

    x: int
    y: int

    # Constructor - hàm khởi tạo
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Hàm trả về chuỗi
    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)

    # Hàm nhập dữ liệu cho điểm
    def read(self):
        self.x = int(input("Nhap x: "))
        self.y = int(input("Nhap y: "))

    # Hàm tính khoảng cách giữa hai điểm
    def distance(self, point):
        d = math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        return d

