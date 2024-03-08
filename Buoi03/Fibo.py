'''Display Fibonacci series up to n terms
Example: n = 10  1  1  2  3  5  8  13  21  34  55
'''
n = int(input("Nhập vào số phần tử:"))

fib_series = [1, 1]
for i in range(2, n):
    fib_series.append(fib_series[-1] + fib_series[-2])

print(fib_series)