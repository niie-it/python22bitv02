# File demo_readcsv.py
import csv

with open("data.csv", "r", encoding="utf8") as csv_file:
    result = list(csv.reader(csv_file))
    
    # Xử lý trên mảng các dòng của file (mỗi dòng là 1 mảng các cột)
    # print(result)
    
    #VD lấy thông tin sv có điểm cao nhất
    # Duyệt từ dòng 1 trở đi (dòng 0 là tiêu đề)
    for index_item in range(1, len(result)):
        print(result[index_item])
    