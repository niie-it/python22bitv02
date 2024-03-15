'''
Write a function to count the number of vowels (a e i o u) and consonants in the string
Đếm số lượng nguyên âm (a e i o u) và số lượng phụ âm (chữ cái còn lại) trong chuỗi.
'''
chuoi_nhap = input("Nhập chuỗi: ").strip()
nguyen_am = "ueoai"
so_ki_tu_nguyen_am = 0
so_ki_tu_phu_am = 0

for ki_tu in chuoi_nhap.lower():
    if ki_tu in nguyen_am:
        so_ki_tu_nguyen_am += 1
    elif ki_tu.isalpha():
        so_ki_tu_phu_am += 1

print(so_ki_tu_phu_am, 'phụ âm', so_ki_tu_nguyen_am, 'nguyên âm')
