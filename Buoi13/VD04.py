import pandas as pd

# Đọc dữ liêu từ file student.csv trả về DataFrame
df = pd.read_csv('student.csv')
print(df)

# In thông tin
print(df.to_string())

#Lấy 5 dòng đầu
print(df.head(5))

#Lấy 5 dòng cuối
print(df.tail(5))

print(df.info())

print(df.describe())

print(df.shape)