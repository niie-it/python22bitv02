import sqlite3

conn = sqlite3.connect("MyDB.db")
cur = conn.cursor()
# Ex 1: Tạo bảng HocVien (làm 1 lần thôi)
# cur.execute('''CREATE TABLE HocVien
# (
#     MaHV text PRIMARY KEY,
#     HoTen text,
#     DienThoai text,
#     NgaySinh date,
#     Email text
# )
# ''')

# Exam2: Chèn dữ liệu
mahv = 'HV001'
ho_ten = 'Nguyễn Văn Tèo'
dien_thoai = '0909009990'
ngay_sinh = '2004-02-29'
email = 'teo.nguyen@demo.com'
sql_insert = f"""
INSERT INTO HocVien(MaHV, HoTen, DienThoai, Email, NgaySinh)
VALUES('{mahv}', '{ho_ten}', '{dien_thoai}', '{email}', '{ngay_sinh}')
"""
conn.execute(sql_insert)
# Exam3: Lấy dữ liệu ra xem
conn.commit()
conn.close()
