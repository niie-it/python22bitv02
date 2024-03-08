'''
Randomly generate a Vietlott MEGA645 lottery ticket with 6 numbers, each number belongs to [1, 45]
HINT:
Using list []
Add a element to list: .append(element)
Using random library:
from random import *
number = randint(1, 45)
'''
from random import randint

bo_so = [] # Mảng rỗng
while len(bo_so) < 6:
    tmp = randint(1, 45)
    if tmp not in bo_so:
        bo_so.append(tmp)
print("Vé của bạn là:", bo_so)
bo_so_sorted = sorted(bo_so)
print("Vé của bạn là:", bo_so_sorted)