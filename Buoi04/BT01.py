'''
Write a function to find the length of a string (don't use the len() function)
Viết hàm tính độ dài của chuỗi (ko sử dụng hàm len() sẵn có)
'''

def lay_do_dai(chuoi: str):
    print(type(chuoi)) # In ra kiểu dữ liệu của tham số chuoi
    count = 0
    for ki_tu in chuoi:
        count += 1
    return count

print(lay_do_dai("Anh yeu Oython"))
print(lay_do_dai([1, 3, 2, 9]))
# print(lay_do_dai(1289))
# PYTHON không check kiểu tham số truyền vào, người tự check

