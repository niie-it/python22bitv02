# File MyCircle.py
'''Định nghĩa lớp hình tròn (Circle) có thành phần dữ liệu (xác định ra hình tròn) là bán kính (radius)'''
import math
class Circle:
    radius: int = 0
    
    # Định nghĩa hàm tạo/dựng (contructor) của hình tròn
    # tại sao có??? ==> dùng để khởi tạo
    # tên: __init__ là keyword, gõ cho đúng
    # từ self: bắt buộc phải có và đứng ở vị trí đầu tiên của method
    def __init__(self, r):
        self.radius = r
    
    # Hàm __str__() là hàm đặc biệt dùng đổi đối tượng thành chuỗi
    def __str__(self):
        return f"Circle has R={self.radius}"
    
    # Hàm tính diện tích (hàm do người dùng định nghĩa)
    def calculate_area(self):
        return math.pi * self.radius**2
    
    # Hàm tính chu vi (hàm do người dùng định nghĩa)
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
# Demo
C1 = Circle(7)
print(C1) # C1.__str__()