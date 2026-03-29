# Toán tử 3 ngôi trong Python, còn được gọi là biểu thức điều kiện, cho phép chúng ta viết các câu lệnh if-else ngắn gọn hơn. Cấu trúc của toán tử 3 ngôi như sau:
# value_if_true if condition else value_if_false
# Dưới đây là một số ví dụ về cách sử dụng toán tử 3 ngôi trong Python:

# Bài 1
n = 7
ketqua1 ="Chan" if n % 2 == 0 else "Le"
print("Ket qua 1 :", ketqua1)

# Bài 2
a_1 = 12
b_1 = 20
max_value = a_1 if a_1 > b_1 else b_1
print("Ket qua 2 :", max_value)

# Bài 3
age = 16
ketqua3 = "Du tuoi" if age >= 18 else "Chua du tuoi"
print("Ket qua 3 :", ketqua3)

# Bài 4
x = -9
abs_x = x if x >=0 else -x
print("Ket qua 4 :", abs_x)

# Bài 5
text = ""
ketqua5 = "Rong" if not text else "Khong rong"
print("Ket qua 5 :", ketqua5)

# Bài 6
score = 8.5
ketqua6 = "Dat" if score >= 5 else "khong dat"
print("Ket qua 6 :", ketqua6)

# Bài 7
a_2 = 15
b_2 = 9
min_value = a_2 if a_2 < b_2 else b_2
print("Ket qua 7 :", min_value)

# Bài 8
x_1 =0
ketqua8 = "Duong" if x_1 > 0 else ("Am" if x_1 < 0 else "Bang 0")
print("Ket qua 8 :", ketqua8)

# Bài 9
score_1 = 7.2
ketqua9 = "Gioi" if score_1 >= 8 else ("Kha" if score_1 >= 6.5 else ("Trung binh" if score_1 >=5 else "Yeu"))
print("Ket qua 9 :", ketqua9)

# Bài 10
a_3 =4
b_3 = 9
c_3 = 6
max_value_2 = a_3 if (a_3 > b_3 and a_3 >c_3) else (b_3 if b_3>a_3 and b_3>c_3 else c_3)
print("Ket qua 10 :", max_value_2)

# Bài 11
x_11 = int(input("Nhap mot so: "))
ketqua11 = "So duong" if x_11 > 0 else ("So am" if x_11 < 0 else "So 0")
print("Ket qua 11 :",ketqua11)

# Bài 12
score_12 = float(input(" Nhap diem: "))
ketqua12 = "Gioi" if score_12 >= 8 else ("Kha" if score_12 >=6.5 else ("Trung binh" if score_12 >=5 else "Yeu"))
print("Ket qua 12 :", ketqua12)

# Bài 13
n_13 = int(input("Nhap mot so: "))
ketqua13 = "Chia het cho 2 va 3" if n_13 % 2 == 0 and n_13 % 3 == 0 else ("Chi chia het cho 2" if n_13 %2 == 0 else ("Chi chia het cho 3" if n_13 % 3 ==0 else "Khong chia het cho 2 va 3"))
print("Ket qua 13 :", ketqua13)

# Bài 14
age_14 = int(input("Nhap tuoi: "))
ketqua14 = "Tre em" if age_14 <12 else ("Thieu nien" if age_14 >=12 and age_14 <18 else ("Nguoi lon" if age_14 >=18 and age_14 <60 else "Nguoi cao tuoi"))
print("Ket qua 14 :", ketqua14)

# Bài 15
a_15 = float(input("Nhap so a: "))
b_15 = float(input("Nhap so b: "))
c_15 = float(input("Nhap so c: "))
max_ab = a_15 if a_15 > b_15 else b_15
max_abc = max_ab if max_ab > c_15 else c_15
print("Ket qua 15 :", max_abc)

# Bài 16
n_16 = int(input("Nhap mot so: "))
ketqua16 = "Chan" if n_16 %2 == 0 else "Le"
print("Ket qua 16 :", ketqua16)

# Bài 17
a_17 = float(input("Nhap so a: "))
b_17 = float(input("Nhap so b: "))
ketqua17 = "a lon hon b" if a_17 > b_17 else ("a nho hon b" if a_17 < b_17 else "a bang b")
print("Ket qua 17 :", ketqua17)

# Bài 18
text_18 = input("Nhap mot chuoi: ")
ketqua18 = "Rong" if text_18 == "" else "Chuoi co noi dung"
print("Ket qua 18 :", ketqua18)

# Bài 19
temp = float(input("Nhap nhiet do: "))
ketqua19 = "Lanh" if temp < 20 else ("Mat" if temp >=20 and temp<30 else "Nong")
print("Ket qua 19 :", ketqua19)

# Bài 20
char = input("Nhap mot ky tu: ")
ketqua20 ="Nguyen am" if char in "aeiou" else "Phu am"
print("Ket qua 20 :", ketqua20)