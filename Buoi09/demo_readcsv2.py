# File demo_readcsv.py
import csv

with open("data.csv", "r", encoding="utf8") as csv_file:
    result = csv.DictReader(csv_file)
    
    # Xử lý trên mảng các dòng của file (mỗi dòng là 1 dict có key là tên các cột - định nghĩa ở dòng 0)
    # print(result)
    for item in result:
        print(item)
        print('Họ tên', item["Họ tên"])
    