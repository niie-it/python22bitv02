'''
Write a Python program to ask how much money the
user spent at the store.
– If they spend less than $75, they will not receive the discount.
– If they spend $75 or more, they get a $15 discount.
– If users spend $100 or more, they will receive a $25 discount.
– If users spend $150 or more, they will receive a $50 discount.
– Then print out the total amount the user must pay
'''
pay = int(input('How much money you pay? '))
discount = 0
if pay >= 150:
    discount = 50
elif pay >= 100:
    discount = 25
elif pay >= 75:
    discount = 15
print(f"Discount: {discount}$, need to pay: {pay - discount}")