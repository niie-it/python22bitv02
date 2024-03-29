ds_khoa = [
    { "ten": 'CNTT', "soluong": 700, "nam": '2012'},
    { "ten": 'LY', "soluong": 300, "nam": '2000'},
    { "ten": 'HOA', "soluong": 200, "nam": '2010'},
    { "ten": 'TOAN', "soluong": 500, "nam": '2000'}
]

# Câu 3a/Viết chương trình tạo ra một list chứa số lượng sinh viên của tất cả các Khoa trong list đã cho và được sắp xếp theo thứ tự tăng dần
#Ví dụ: output như sau: [200, 300, 500, 700]
mang_so_sv = sorted([khoa["soluong"] for khoa in ds_khoa])
print(mang_so_sv)

#Bớt vắn tắt cho dễ hiểu
mang_sosv = []
for khoa in ds_khoa:
    mang_sosv.append(khoa["soluong"])
mang_sosv = sorted(mang_sosv)
print(mang_sosv)

#Viết chương trình tìm tên Khoa có thời gian thành lập lâu nhất tính đến nay. #Ví dụ: output là TOAN
nam_thanh_lap_cu_nhat = min([int(khoa["nam"]) for khoa in ds_khoa])
print(nam_thanh_lap_cu_nhat)
khoa_lau_nhat = list(filter(lambda khoa: int(khoa["nam"]) == nam_thanh_lap_cu_nhat, ds_khoa))
khoa_lau_nhat = [khoa["ten"] for khoa in khoa_lau_nhat]
print(khoa_lau_nhat)

#c) Viết chương trình tìm các Khoa có số lượng sinh viên lớn hơn 200. In kết quả các Khoa tìm được ra màn hình theo thứ tự tăng dần theo từ điển. Ví dụ: output là CNTT, LY, TOAN
khoa_lon = list(filter(lambda khoa: khoa["soluong"] > 200, ds_khoa))
ds_ten_khoa_lon = [khoa["ten"] for khoa in khoa_lon]
