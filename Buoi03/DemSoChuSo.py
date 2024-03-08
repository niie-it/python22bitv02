'''
Count the total number of digits in a number
Example, the number is 75869, so the output should be 5
Nhập vào số nguyên. Xuất ra số đó có bao nhiêu chữ số (ko dùng hàm len của lớp chuỗi/string)
'''
number = int(input("Nhập vào số nguyên:"))
count = 0
# tmp = 75869
# tmp = 7586 ==> tmp = tmp // 10
tmp = number
while tmp > 0:
    count = count + 1
    tmp = tmp // 10

print(f"{number} có {count} chữ số.")
    