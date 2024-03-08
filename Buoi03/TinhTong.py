'''Write a program to sum the total number of digits in a number using a while loop.
Example: n = 12923 => 17
'''
number = int(input("Nhập vào số nguyên:"))
sum = 0
tmp = number
while tmp > 0:
    sum = sum + tmp % 10
    tmp = tmp // 10

print(f"Tổng các chữ số của {number} là {sum}.")