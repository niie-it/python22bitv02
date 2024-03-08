# range(start, stop, step=1)

# range(7) <==> range(0,7)
print(list(range(7)))
print(list(range(1, 7)))
print(list(range(3, 7, 2)))
print(list(range(11, 1, -3)))

for i in range(2, 11):
    print(9, "x", i, "=", 9*i)