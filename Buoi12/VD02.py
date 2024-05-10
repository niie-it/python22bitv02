# Biểu đồ Bar (coulmn đứng)
import matplotlib.pyplot as plt

# Dữ liệu tự chuẩn bị (lấy từ đồ án nhóm)
D = { 'AP': 500, 'Security': 310,
'Chem': 150, 'Bio': 280, 'Edu': 340}

plt.bar(range(len(D)), list(D.values()),color='r')
plt.xticks(range(len(D)), D.keys())

# plt.barh(range(len(D)), list(D.values()),color='b')

plt.title('Số lượng sinh viên')
plt.show()
