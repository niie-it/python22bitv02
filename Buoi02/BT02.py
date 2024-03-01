'''
Write a Python program that can check the parity of an
input number. Print to the screen whether the entered
number is even, odd, or neither of the above cases.
'''
so_nguyen = int(input("Nhập vào số nguyên:"))
if so_nguyen == 0:
    print("Không chẵn không lẻ")
    print("END")
elif so_nguyen % 2 == 0:
    print(so_nguyen, "là số chẵn")
else:
    print(so_nguyen, "là số lẻ")