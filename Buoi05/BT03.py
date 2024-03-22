'''A positive integer with n digits is called an Armstrong number when the sum of the nth powers of its digits is equal to itself.
For example:
371 is Armstrong's number because: 3^3 + 7^3 + 1^3 = 371
8208 is Armstrong's number because: 8^4 + 2^4 + 8^4 = 8208
Check to see if a positive integer entered from the keyboard is an Armstrong number or not?
'''
# Viết hàm để kiểm tra, trả về True/False
def la_so_amstrong(so_nguyen: int):
    # Đổi số sang chuỗi
    chuoi_so = str(so_nguyen)
    do_dai = len(chuoi_so)
    
    tong = 0
    for ki_so in chuoi_so:
        tong += int(ki_so) ** do_dai
        
    return tong == so_nguyen

print('8208 is amstrong number?', la_so_amstrong(8208))
print('18298 is amstrong number?', la_so_amstrong(18298))