# Bài tập 2: Nhập vào tọa độ 2 điểm A(x1, y1) và B(x2, y2)
# Tính khoảng cách giữa 2 điểm
# HD: Sử dụng hàm mũ: **
# VD: 5^2 ==> 5**2

# Bài tập 3: Nhập bán kính R, xuất diện tích S=PI*R^2, chu vi P=PI*2*R của hình tròn làm tròn 2 chữ số
# Dùng thư viện math để lấy số PI chính xác
# import math
# math.pi
import math
R = float(input("Nhập bán kính:"))
S = round(math.pow(R, 2) * math.pi)
P = round(2 * R * math.pi)


'''Bài tập 4: BT đổi tiền: Nhập số tiền, bội số của 50k
- In số tiền cần đổi biết máy ATM vô hạn và có các mệnh giá:
50k, 100k, 200k, 500k đơn vị ngàn đồng cho trường hợp ít tờ nhất'''

so_tien_can_doi = int(input("Cần đổi (ngàn đồng): "))
so_to_500k = so_tien_can_doi // 500
so_tien_can_doi %= 500
so_to_200k = so_tien_can_doi // 200
so_tien_can_doi %= 200
so_to_100k = so_tien_can_doi // 100
so_tien_can_doi %= 100
so_to_50k = so_tien_can_doi // 50
so_tien_can_doi %= 50

print(f"{so_to_500k} tờ 500k, {so_to_200k} tờ 200k, {so_to_100k} tờ 100k, {so_to_50k} tờ 50k")