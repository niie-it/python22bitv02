#File. hours.py đọc nội dung chấm công file hours.txt
# xuất: Suzy ID 123 worked 31.4 hours: 6.3 / day

# Mở file thì nhớ đóng file
# my_file = open("hours.txt", "r")
# my_file.close()
with open("hours.txt", "r") as my_file:
    # Không cần đóng (tự đóng khi ra khỏi lệnh with)
    for line in my_file:
        print(line)
        arr = line.split()
        hours = arr[2:]
        total_hours = 0
        for hour in hours:
            total_hours += float(hour)
        print(f"{arr[1]} ID {arr[0]} worked {total_hours} hours: {total_hours/len(hours)} / day")