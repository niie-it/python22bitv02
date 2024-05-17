# Demo Series - dữ liệu cột
import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a)
myvar2 = pd.Series(a, index= ["x", "y", "z"])

print(myvar)

print(myvar2)
# print(myvar["y"])
