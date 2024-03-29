'''
Write a Python program to permit user can enter your name, your age, your major and store all information into one text file.
Input:
    Q: What is your name?
    A: David
    Q: How old are you?
    A: 20 years old
    Q: What is your major?
    A: Information Technology
Output: File student.txt
    Line 1: David
    Line 2: 20 year old
    Line 3: Information Technology
'''
name = input("What is your name? ")
yrs = int(input("How old are you? "))
major = input("What is your major? ")

with open("student.txt", "a", encoding="utf8") as my_file:
    #w: Mở file để ghi (nếu đã có file thì ghi đè)
    #a: Mở để ghi thêm cuối file
    my_file.write(f"{name}\n")
    my_file.write(f"{yrs} years old\n")
    my_file.write(f"{major}\n\n")
# Dùng with thì không cần close() vì ra khỏi khối lệnh with file sẽ tự close