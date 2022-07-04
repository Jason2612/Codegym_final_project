"""
viet 1 chuong trinh noi dung on kien thuc ve datetime

1 chuong trinh mo phong chuong giang duong
trong do cu den dau gio, la hien thi thong bao
vao tiet n, het tiet thi hien thi thong bao la het tiet n

phat 1 doan nhac reng reng - tuong ung nhu chuong giang duong thay vi hien thi thong bao

- CRUD việc làm/ nhóm việc làm ( để người dùng có thể tái sử dụng ) 
- CRUD danh sách việc làm
- Chức năng đếm ngược
- Lưu trữ lại thời gian ( để có thể gợi ý thời gian cho người dùng ở lần tiếp theo )
"""

# 

# NANG CAP
# lưu giữ các lần chạy quá khứ
# Tạo 1 List lưu trữ các việc muốn làm
# Tạo def add 1 việc vào
# Tạo def delete 1 việc khỏi list
# Tạo def modifi 1 việc đã có trong list

# lưu nó vào 1 dictionary với thời gian được set trước
# người dùng có thể gọi nó ra và sử dụng
# Công việc chiều sáng tối





import time
import datetime
from playsound import playsound

dict_to_do = {}

# hàm đếm ngược
def countdown(h, m, s):
    total_seconds = h * 3600 + m * 60 + s
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1

key = 0
# hàm add 1 việc vào list
def adding_to_list(to_do_input):
    global key
    key += 1
    dict_to_do[key] = to_do_input 

# hàm delete 1 việc khỏi list
def delete_from_list(dict_key):
    if dict_key in dict_to_do:
        dict_to_do.pop(dict_key)

# hàm sửa 1 việc trong list
def modify_from_list(dict_key, modify_input):
    for key in dict_to_do:
        if int(dict_key) == key:
            dict_to_do[key] = modify_input

# Hàm lưu vào text hiển thị
def save_into_text():
    f = open(r"C:\\Users\\Phong\\Desktop\\My Testing Project\\Final Project\\note.txt", "w", encoding="UTF-8-sig")
    for key, value in dict_to_do.items():
        f.write('%s:%s\n' % (key, value))
    
# Hàm chuyển từ file note sang file history
def switch_line_to_file():
    f = open(r"C:\\Users\\Phong\\Desktop\\My Testing Project\\Final Project\\note.txt", "r", encoding="UTF-8-sig")
    g = open(r"C:\\Users\\Phong\\Desktop\\My Testing Project\\Final Project\\history.txt", "a", encoding="UTF-8-sig")

    for line in f:
        g.write(line)
    g.write(countdown())



# khu test code
for i in range(5):
    to_do_input = input("Nhap vao day: ")
    adding_to_list(to_do_input)
print(dict_to_do)

# dict_key = int(input("Nhap vao day: "))
try:
    save_into_text()
    switch_line_to_file()
except:
    print("hmm")
