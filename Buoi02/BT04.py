month = int(input('Month: '))
year = int(input('Year: '))

is_leap_year = False

if (year % 400 == 0 # Năm chia hết cho 400
    or (year % 4 == 0 and year % 100 != 0) # Chia hết cho 4 nhưng không chia hết cho 100
):
    is_leap_year = True

so_ngay = 0
if month in [1,3,5,7,8,10,12]:
    so_ngay = 31
elif month in [4,6,9,11]:
    so_ngay = 30
else:
    so_ngay = 29 if is_leap_year else 28