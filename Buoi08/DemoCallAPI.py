'''
Gọi API lấy sản phẩm từ trang dummyjson.org thông qua endpoint: https://dummyjson.com/products
'''
import requests
import json

# Step 1: Gọi API
my_request = requests.get("https://dummyjson.com/products")

# Step 2: Kiểm tra kết quả gọi API
if my_request.status_code == 200: # OK/Success
    result_data = my_request.json()
    print(json.dumps(result_data, indent=4))
    
    #Step 3: Xử lý dữ liệu trả về (tùy bạn)


# Restful API: GET, POST, PUT, DELETE