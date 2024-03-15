'''BT2: Nhập vào 01 chuỗi. Đếm xem chuỗi đó có bao nhiêu từ?
HINT: Sử dụng hàm split() để tách chuỗi thành mảng.'''


chuoi_nhap = input("Nhập chuỗi: ").strip()

mang_tu = chuoi_nhap.split() # tách theo khoảng trắng
print(f"{chuoi_nhap} có {len(mang_tu)} từ.")

# Suy nghĩ: Đếm số lần xuất hiện từng từ?
# Dùng từ điển (dict) để lưu trữ
thong_ke = {}
for tu in mang_tu:
    # Kiểm tra tu đã có trong dict thong_ke hay chưa
    thong_ke[tu] = thong_ke.get(tu, 0) + 1
print(thong_ke)