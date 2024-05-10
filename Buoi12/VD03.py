# Biểu đồ Bar (coulmn đứng)
import matplotlib.pyplot as plt

# Dữ liệu tự chuẩn bị (lấy từ đồ án nhóm)
D1 = { 'AP': 500, 'Security': 310,
'Chem': 150, 'Bio': 280, 'Edu': 340}
D2 = { 'AD': 400, 'Security': 210,
'Chem': 250, 'Bio': 380, 'Edu': 340}
arr_key1 = ["AP", "Sec1", "Chem", "Bio", "Edu"]
arr_key2 = ["AD", "Sec2", "Chem", "Bio", "Edu"]


plt.bar(arr_key1, [1, 5, 6, 7, 11], label="V01", color='g')
plt.bar(arr_key2, [11, 25, 16, 7, 41], label="V02", color='b')
# plt.xticks(range(len(D)), D.keys())

plt.legend()

plt.title('Số lượng sinh viên')
plt.show()
