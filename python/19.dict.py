# dict trong python là một cấu trúc dữ liệu lưu trữ các cặp key-value. Mỗi key phải là duy nhất và có thể được sử dụng để truy cập giá trị tương ứng. Dưới đây là một số ví dụ về cách tạo và sử dụng dict trong Python:
# Tạo một dict

'''Sinh_vien ={
    "Ho_Ten": "Dao Vu Dung",
    "Tuoi":21,
    "GPA":3.5
}

#1.in ra dict
print(Sinh_vien)
#2.truy cập phần tử trong dict
print(Sinh_vien["GPA"]) #3.5
#3.thêm hoặc sửa phần tử trong dict
Sinh_vien["GPA"] = 3.8
Sinh_vien["Tuoi"] = 22
print(Sinh_vien) #{'Ho_Ten': 'Dao Vu Dung', 'Tuoi': 22, 'GPA': 3.8}
#4.xóa phần tử trong dict
del Sinh_vien["GPA"]
print(Sinh_vien) #{'Ho_Ten': 'Dao Vu Dung', 'Tuoi': 22}
#5.duyệt các phần tử trong dict
print()
for key in Sinh_vien:
    print(key, Sinh_vien[key])

#6.dùng key() value() items() để duyệt dict
print()
for key in Sinh_vien.keys():
    print(key)
print()
for value in Sinh_vien.values():
    print(value)
print()
for key, value in Sinh_vien.items():
    print(key, value)

#7.kiểm tra sự tồn tại của key trong dict
print("GPA" in Sinh_vien) #False
print("Tuoi" in Sinh_vien) #True

#8.sử dụng get() để truy cập phần tử trong dict
print(Sinh_vien.get("GPA", "Không tìm thấy key")) #Không tìm thấy key
print(Sinh_vien.get("Tuoi", "Không tìm thấy key")) #22'''

#Bài Tập về dict
print("Bài 1")
#Bài 1
sinh_vien = {
    "Ten": "Dao Vu Dung",
    "Tuoi": 21,
    "lop": "KTPM"
}

print(sinh_vien)

print("Bài 2")
#Bài 2
student = {"name": "An", "age": 18, "class": "12A1"}
print(student["name"])
print(student["age"])

print("Bài 3")
#Bài 3
student = {"name": "An", "age": 18}
student["class"]="12A1"
student["city"]="Hanoi"
print(student)

print("Bài 4")
#Bài 4
student = {"name": "An", "age": 18, "city": "Hanoi"}
student["age"]=19
student["city"]= "Da Nang"
print(student)

print("Bài 5")
#Bài 5
student = {"name": "An", "age": 18, "city": "Hanoi"}
del student["city"]
print(student)

print("Bài 6")
#Bài 6 
student = {"name": "An", "age": 18, "class": "12A1"}
for key in student:
    print(key,student[key])

print("Bài 7")
#Bài 7
student = {"name": "An", "age": 18, "class": "12A1"}
key1=input("Nhập key cần kiểm tra: ")
if key1 in student:
    print("Có trong dictionary")
else:
    print("Không có trong dictionary")

print("Bài 8")
#Bài 8
n = int(input("Nhập số phần tử của list: "))
my_list = []
for i in range(1,n+1):
    x=input(f"Nhập phần tử thứ {i}: ")
    my_list.append(x)

my_dict= {}
for i in my_list:
    if i in my_dict:
        my_dict[i]+=1
    else:
        my_dict[i]=1

print(my_dict)

print("Bài 9")
#Bài 9
cau = str(input("Nhập một câu: "))
tu = cau.split()
dem={}
for i in tu:
    if i in dem:
        dem[i]+=1
    else:
        dem[i]=1

print(dem)

#Bài 10
print("Bài 10")
cau = str(input("Nhập một câu: "))
tu = cau.split()
dem= {}
for i in tu:
    if i in dem:
        dem[i]+=1
    else:
        dem[i]=1

max_word = ""
max_count = 0
for word, count in dem.items():
    if count > max_count:
        max_count = count
        max_word = word

print(f"Từ xuất hiện nhiều nhất: {max_word} với số lần xuất hiện: {max_count}")