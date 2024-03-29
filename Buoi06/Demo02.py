#Demo các thư viện liên quan đến thư mục

import os
import os.path

# In thư mục hiện hành
current_folder = os.getcwd()
print('TM hiện tại', current_folder)

# Thư mục cha
print('Thư mục cha', os.path.abspath(os.path.join(current_folder, os.pardir)))
print('Thư mục cha', os.path.dirname(current_folder))