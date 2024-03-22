'''IC2. Given the following two dictionary variables:
 price={"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
 quantity={"banana": 6, "orange": 32, "pear": 15}
Print out the order of fruits in a descending list of each type's value (with value = quantity * price)
'''
price={"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
quantity={"banana": 6, "orange": 32, "pear": 15}

for item in price: # Duyệt qua key
    print(quantity.get(item, 0), "x", item, price[item])

# Tạo mảng lưu trữ thành tiền
my_dict = {}
for item in price.keys():
    my_dict[item] = quantity.get(item, 0) * price[item]
    
print(my_dict)

# VD Duyệt qua item=(key, value)
for item_key, item_value in my_dict.items():
    print(item_key, item_value)

# Sắp giảm dần
sorted_my_dict = sorted(my_dict.items(), key=lambda x : x[1], reverse=True)
print(sorted_my_dict)