import numpy as np
import matplotlib.pyplot as plt

# Tạo mảng dữ liệu cho biến X
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# X = [1, 2, 3, 4, 5]

# Định nghĩa hàm y=f(x)=cos(x), g=g(x)=sin(x)
y, g = np.cos(X), np.sin(X)

plt.plot(X, y)
plt.plot(X, g)

# Tiêu đề
plt.title("Hàm số sin/cos")
plt.xlabel("Hoành độ")
plt.ylabel("Tung độ")

# Hiển thị lên đồ thị
plt.show()
