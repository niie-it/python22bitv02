# Ví dụ về dict
thong_ke ={
    "Nam": 31,
    "Nữ": 5
}
print(thong_ke)
print("Nam", thong_ke["Nam"])
# print("Khác", thong_ke["Khác"])
print("Khác", thong_ke.get("Khác"))
print("Khác", thong_ke.get("Khác", 0))