'''Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists
Original list:
[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
Grouping a sequence of key-value pairs into a dictionary of lists:
{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
'''
data = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

my_dict = {}
for key, value in data:
    if key in my_dict:
        my_dict[key].append(value)
    else: # Chưa có
        my_dict[key] = [value]
print(my_dict)