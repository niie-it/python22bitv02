# File MyFunc.py
def say_hello(name: str):
   print(f"Hello Mr/Ms {name}.") 

def say_goodbye(name: str):
   print(f"Bye bye {name}. See u tomorrow!") 
   
def tinh_toan(x, y):
    return x ** y / (x - y)

# Chỉ gọi hàm __main__ khi chạy trực tiếp file
if __name__ == "__main__":
    # Gọi hàm
    say_hello("Nam Phương")
    say_goodbye("Lê Lai")
    print(tinh_toan(11, 7))
    say_goodbye("Lê Lợi")