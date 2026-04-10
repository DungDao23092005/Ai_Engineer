# bài 2.variable
print("Bài 2.1")
#2.1
name = "Dung"
age = 21
tall =1.96
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Tall: {tall}")

print("Bài 2.2")
#2.2
a=10
b=5
print(f"a + b = {a+b}")
print(f"a - b = {a-b}")
print(f"a * b = {a*b}")
print(f"a / b = {a/b}")

print("Bài 2.3")
#2.3
x=10
y=5
print(f"Trước khi hoán đổi:x = {x}, y = {y}")
x,y=y,x #hoán đổi giá trị của x và y
print(f"Sau khi hoán đổi x={x}, y={y}")

print("Bài 2.4")
#2.4
dai=5
rong=4
chu_vi=2*(dai+rong)
print(f"Chu vi hình chữ nhật là :{chu_vi}")

print("Bài 2.5")
#2.5
ban_kinh=5
dien_tich=3.14*ban_kinh**2
print(f"Diện tích hình tròn là :{dien_tich}")

print("Bài 2.6")
#2.6
giay=50203
phut=giay/60
print(f"{giay} giây bằng {phut} phút")

print("Bài 2.7")
#2.7
C=30
F=(C *9/5)+32
print(f"{C} độ C bằng {F} độ F")

print("Bài 2.8")
#2.8
a,b,c = 1,2,3
print(f"a = {a}, b = {b}, c = {c}")

print("Bài 2.9")
#2.9
a,b,c=7,8,9
print(f"Tổng điểm trung bình là :{(a+b+c)/3}")

print("Bài 2.10")
#2.10
s="Never give up,blive in myself"
print(f"kiểu dữ liệu của s là : {type(s)}")

#bài 3.TypeCasting
print("Bài 3.1")
#3.1
age = "21"
age_int = int(age)
print(f"Tuổi sau khi chuyển đổi sang int: {age_int}, kiểu dữ liệu: {type(age_int)}")

print("Bài 3.2")
#3.2
b=3.9
b_int=int(b)
print(f"Giá trị sau khi chuyển đổi sang int: {b_int}, kiểu dữ liệu: {type(b_int)}")

print("Bài 3.3")
#3.3
c=123
c_str = str(c)
print(f"Giá trị sau khi chuyển đổi sang str: {c_str}, kiểu dữ liệu: {type(c_str)}")

print("Bài 3.4")
#3.4
d="5.42"
d_float=float(d)
print(f"Giá trị sau khi chuyển đổi sang float: {d_float}, kiểu dữ liệu: {type(d_float)}")

print("Bài 3.5")
#3.5
a=int(input("Nhập giá trị a: "))
b=int(input("Nhập giá trị b: "))
print(f"Tổng của a và b là: {a + b}")

print("Bài 3.6")
#3.6
d=0
d_bool=bool(d)
print(f"Giá trị sau khi chuyển đổi sang bool: {d_bool}, kiểu dữ liệu: {type(d_bool)}")

print("Bài 3.7")
#3.7
e=6
print(f"Giá trị e trước khi chuyển đổi= {e}, kiểu dữ liệu: {type(e)}")
e_str=str(e)
print(f"Giá trị e sau khi chuyển đổi sang str= {e_str}, kiểu dữ liệu: {type(e_str)}")

print("Bài 3.8")
#3.8
chieu_cao = float(input("Nhập chiều cao (m): "))
print(f"Chiều cao của bạn là: {chieu_cao} m")

print("Bài 3.9")
#3.9
age = 32
age_str = str(age)
print("age: " + age_str)

print("Bài 3.10")
#3.10
list   = ["1", "3", "6", "9"]
map_list = map(int, list) #chuyển đổi từng phần tử trong list sang int
for i in map_list:
    print(i,"sau khi chuyển đổi sang int, kiểu dữ liệu: ",type(i))

print("Bài 4")
#Bài 4 input
print("Bài 4.1")
#4.1
name = str(input("Nhập tên của bạn: "))
print(f"Xin chào : {name}")

print("Bài 4.2")
#4.2
age = int(input("Nhập tuổi của bạn: "))
print(f"Năm sinh của bạn là : {2025-age}")

print("Bài 4.3")
#4.3
a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
print(f"Tổng của a và b là: {a + b}")

print("Bài 4.4")
#4.4
dai=int(input("Nhập chiều dài hình chữ nhật: "))
rong=int(input("Nhập chiều rộng hình chữ nhật: "))
print(f"Diện tích hình chữ nhật là: {dai*rong}")

print("Bài 4.5")
#4.5
ban_kinh=float(input("Nhập bán kính hình tròn: "))
print(f"Diện tích hình tròn là: {3.14 * ban_kinh ** 2}")

print("Bài 4.6")
#4.6
C = float(input("Nhập nhiệt độ C: "))
F=(C *9/5)+32
print(f"{C} độ C bằng {F} độ F")

print("Bài 4.7")
#4.7
a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
c=int(input("Nhập số c: "))
print(f"Tổng điểm trung bình là :{(a+b+c)/3}")

print("Bài 4.8")
#4.8
a=int(input("Nhập số a: "))
print(f"{a % 2} là phần dư của a khi chia cho 2")

print("Bài 4.9")
#4.9
name=str(input("Nhập tên của bạn: "))
age=int(input("Nhập tuổi của bạn: "))
print(f"Xin chào {name}, bạn đã {age} tuổi.")

print("Bài 4.10")
#4.10
giay=int(input("Nhập số giây: "))
phut=giay/60
print(f"{giay} giây bằng {phut} phút")

print("Bài 7") 
#bài 7 if else
# Bài 7
print("Bài 7.1")
#7.1
a=int(input("Nhập số a: "))
if a <0:
    print("Số âm")
elif a >0:
    print("Số dương")
else:
    print("Số bằng 0")

print("Bài 7.2")
#7.2
n=int(input("Nhập số n: "))
if n % 2 ==0 :
    print("Số chẵn")
else:
    print("Số lẻ")

print("Bài 7.3")
#7.3
age=int(input("Nhập tuổi của bạn: "))
if age < 18:
    print("Bạn chưa đủ tuổi để lái xe.")
else:
    print("Bạn đủ tuổi để lái xe.")

print("Bài 7.4")
#7.4
a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
if a > b:
    print(f"{a} lớn hơn {b}")
elif a < b:
    print(f"{a} nhỏ hơn {b}")
else:
    print(f"{a} bằng {b}")

print("Bài 7.5")
#7.5
score=int(input("Nhập điểm của bạn: "))
if score >=5:
    print("pass")
else:
    print("fail")

print("Bài 7.6")
#7.6
password=str(input("Nhập mật khẩu: "))
if password == "123456":
    print("Đăng nhập thành công")
else:
    print("Đăng nhập thất bại")

print("Bài 7.7")
#7.7
a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
c=int(input("Nhập số c: "))
if a > b and a > c:
    print(f"{a} là số lớn nhất")
elif b > a and b > c:
    print(f"{b} là số lớn nhất")
else:    print(f"{c} là số lớn nhất")

print("Bài 7.8")
#7.8
year=int(input("Nhập năm: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} là năm nhuận")
else:    print(f"{year} không phải là năm nhuận")

print("Bài 7.9")
#7.9
x=int(input("Nhập số x: "))
if x>10 and x<20:
    print(f"{x} nằm trong khoảng từ 10 đến 20")
else:
    print(f"{x} không nằm trong khoảng từ 10 đến 20")

print("Bài 7.10")
#7.10
phep_tinh=str(input("Nhập phép tính (+, -, *, /): "))
a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
if phep_tinh == "+":
    print(f"{a} + {b} = {a+b}")
elif phep_tinh == "-":
    print(f"{a} - {b} = {a-b}")
elif phep_tinh == "*":
    print(f"{a} * {b} = {a*b}")
elif phep_tinh == "/":
    if b != 0:
        print(f"{a} / {b} = {a/b}")
    else:
        print("Không thể chia cho 0")
else:    print("Phép tính không hợp lệ")

print("Bài 8")
#bài 8 logic operators
# Bài 8
print("Bài 8.1")
#8.1
age=int(input("Nhập tuổi của bạn: "))
if age >= 18 and age <= 60:
    print("Bạn là người trưởng thành")
else:    print("Bạn không phải là người trưởng thành")

print("Bài 8.2")
#8.2
login=str(input("Nhập tên đăng nhập: "))
if login == "admin" or login == "user":
    print("Đăng nhập thành công")
else:    print("Đăng nhập thất bại")

print("Bài 8.3")
#8.3
a=int(input("Nhập số a: "))
if a>20 and a<50:
    print(f"{a} nằm trong khoảng từ 20 đến 50")
else:    print(f"{a} không nằm trong khoảng từ 20 đến 50")

print("Bài 8.4")
#8.4
score=int(input("Nhập điểm của bạn: "))
if score >= 90 or score == 100:
    print("Xuất sắc")
elif score >= 80 and score < 90:
    print("Giỏi")
elif score >= 70 and score < 80:
    print("Khá")
elif score >= 60 and score < 70:
    print("Trung bình")
else:    print("Yếu")

print("Bài 8.5")
#8.5
thu=str(input("Nhập ngày trong tuần: "))
if thu in ["thứ 2", "thứ 3", "thứ 4", "thứ 5", "thứ 6"]:
    print(f"{thu} là ngày trong tuần")
elif thu in ["thứ 7", "chủ nhật"]:
    print(f"{thu} là ngày cuối tuần")
else:    print("Ngày không hợp lệ")

print("Bài 8.6")
#8.6
user=str(input("Nhập loại người dùng: "))
if user =="Svip" or user =="Vip":
    print("Bạn được miễn phí vận chuyển")
else:    print("Bạn phải trả phí vận chuyển")

print("Bài 8.7")
#8.7
password=str(input("Nhập mật khẩu: "))
if password not in ["123456", "password", "admin"]:
    print("Mật khẩu hợp lệ")
else:    print("Mật khẩu không hợp lệ")

print("Bài 8.8")
#8.8
score=int(input("Nhập điểm của bạn: "))
if score >=15:
    print("Bạn đã đậu đại học")
else:    print("Bạn đã trượt đại học")

print("Bài 8.9")
#8.9
a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
c=int(input("Nhập số c: "))
if a+b>c and a+c>b and b+c>a:
    print("Ba cạnh này có thể tạo thành một tam giác")
else:    print("Ba cạnh này không thể tạo thành một tam giác")

print("Bài 8.10")
#8.10
so=int(input("Nhập số: "))
if so == 5 and so == 10:
    print("Bạn đã đoán đúng số")
else:    print("Bạn đã đoán sai số")

#bài 10 strings
print("Bài 10")
#Bài 10
print("Bài 10.1")
#10.1
s=str(input("Nhập một chuỗi: "))
print(f"Viết hoa chuổi : {s.upper()}")

print("Bài 10.2")
#10.2
s=str(input("Nhập một chuỗi: "))
print(f"Viết thường chuỗi : {s.lower()}")

print("Bài 10.3")
#10.3
s=str(input("Nhập một chuỗi: "))
print(f"Độ dài của chuỗi là : {len(s)}")

print("Bài 10.4")
#10.4
s=str(input("Nhập một chuỗi: "))
s = s.replace(" ", "")
print(f"Chuỗi sau khi xóa khoảng trắng: {s}")

print("Bài 10.5")
#10.5
s=str(input("Nhập một chuỗi: "))
if "a" in s:
    print("Chuỗi có chứa ký tự 'a'")
else:    print("Chuỗi không chứa ký tự 'a'")

print("Bài 10.6")
#10.6
s=str(input("Nhập một chuỗi: "))
print(f"Chuỗi bạn vừa nhập là: {s}")
print(f"Chuỗi sau khi cắt :{s[0:5]}")

print("Bài 10.7")
#10.7
s=str(input("Nhập một chuỗi: "))
print(f"Chuỗi bạn vừa nhập là: {s}")
print(f"Đảo chuỗi: {s[::-1]}")

print("Bài 10.8")
#10.8
s=str(input("Nhập một chuỗi: "))
print(f"Chuỗi bạn vừa nhập là: {s}")
print(f"Chuỗi sau khi xóa khoảng trắng là : {s.strip()}")

print("Bài 10.9")
#10.9
s=str(input("Nhập một chuỗi: "))
print(f"Chuỗi bạn vừa nhập là: {s}")
print(f"Chuỗi sau khi tách: {s.split()}")

print("Bài 10.10")
#10.10
s=str(input("Nhập một chuỗi: "))
print(f"Chuỗi bạn vừa nhập là: {s}")
print(f"Chuỗi của bạn sau khi nối là: {'-'.join(s)}")

print("Bài 11")
#Bài 11 string in dexing
print("Bài 11.1")
#11.1
s = "Hello, World!"
print(s[0])

print("Bài 11.2")
#11.2
s = "Hello, World!"
print(s[-1])

print("Bài 11.3")
#11.3
s = "Hello, World!"
print(s[:3])

print("Bài 11.4")
#11.4
s = "Hello, World!"
print(s[-3:])

print("Bài 11.5")
#11.5
s = "Hello, World!"
print(s[::-1])

print("Bài 11.6")
#11.6
s = "Hello, World!"
print(s[::2])

print("Bài 11.7")
#11.7
s = "Hello, World!"
print(s[2:5])

print("Bài 11.8")
#11.8
s = "Hello, World!"
print(len(s))

print("Bài 11.9")
#11.9
s = "Hello, World!"
if s[1] == "a":
    print("Ký tự thứ 2 là 'a'")
else:
    print("Ký tự thứ 2 không phải là 'a'")

print("Bài 11.10")
#11.10
s = "Hello, World!"
for i in s:
    print(i)

print("Bài 12")
#Bài 12 formart_specifier
print("Bài 12.1")
#12.1
a=12.5245252
print(f"Số thực 2 chữ số thập phân là : {a:.2f}")

print("Bài 12.2")
#12.2
b = 123456789
print(f"Số có dấu phẩy ngăn cách hàng nghìn là : {b:,}")

print("Bài 12.3")
#12.3
c=12345678959696789203
print(f"Canh trái chuỗi 10 kí tự là : {c:<10}")

print("Bài 12.4")
#12.4
d=12345678959696789203
print(f"Canh phải chuỗi 10 kí tự là : {d:>10}")

print("Bài 12.5")
#12.5
f=12345678959696789203
print(f"Canh giữa chuỗi 10 kí tự là : {f:^10}")

print("Bài 12.6")
#12.6
e=0.32
print(f"Phần trăm của e là : {e:.0%}")

print("Bài 12.7")
#12.7
b=23213.12345
print(f"giữ 3 số sau dấu chấm là : {b:.3f}")

print("Bài 12.8")
#12.8
g=4235694
print(f"In số có 0 phía trước là : {g:010}")

print("Bài 12.9")
#12.9
h=123456789.12354512421
print(f"Hiển thị tiền tệ : {h:,.2f}")

print("Bài 12.10")
#12.10
i=0.123456789
k=12354.123456789
print("nhiều biến cùng lúc : {:.2f}, {:,.2f}".format(i, k))

print("Bài 13")
#Bài 13 while loop
print("Bài 13.1")
#13.1
i=1
while i <11:
    print(i)
    i+=1

print("Bài 13.2")
#13.2
i=0
while i < 21:
    print(i)
    i+=2

print("Bài 13.3")
#13.3
n = int(input("Nhập số n: "))
i=1
sum =0
while i<=n:
    sum+=i
    i+=1
print(f"Tổng các số từ 1 đến {n} là: {sum}")

print("Bài 13.4")
#13.4
password = input("Nhập mật khẩu: ")
while password == "123456":
    print("Mật khẩu đúng!")
    break
else:
    print("Mật khẩu sai!")

print("Bài 13.5")
#13.5
i=10
while i>0:
    print (i)
    i-=1
print("Hết giờ!")

print("Bài 13.6")
#13.6
i=1
while i<11:
    print(f"5 * {i} = {5 * i}")
    i+=1

print("Bài 13.7")
#13.7
n=int(input("Nhập số n: "))
while n != 0 :
    print("Tiếp tục")
    n=int(input("Nhập số n: "))
else:
    print("Kết thúc chương trình")

print("Bài 13.8")
#13.8
i=0
total=0
while i < 100:
    if i % 2 == 0 and i <51:
        total+=i    
    i+=2
print(f"Tổng các số chẵn nhỏ hơn 51 là: {total}")

print("Bài 13.9")
#13.9
dem =0
i=1023
while i >0:
    dem+=1
    i//=10

print(f"Số chữ số của 1023 là: {dem}")

print("Bài 13.10")
#13.10
n=int(input("Nhập số n: "))
while n != 6:
    print("Bạn đã chọn sai")
    n=int(input("Nhập số n: "))
else:
    print("Bạn đã chọn đúng")

#Bài 14 For loop
print("Bài 14")
#Bài 14.1
for i in range(1,11):
    print(i)

print("Bài 14.2")
for i in range(0,21,2):
    print(i)

print("Bài 14.3")
total = 0
for i in range(1,101):
    total+=i

print(f"Tổng các số từ 1 đến 100 là: {total}")

print("Bài 14.4")
s=str(input("Nhập chuỗi: "))
for i in s :
    print(i)

print("Bài 14.5")
for i in range(1,11):
    print(f"7 * {i} = {7 * i}")

print("Bài 14.6")
total=1
n=int(input("Nhập số n: "))
for i in range(1,n+1):
    total*=i
print(f"Giá trị của {n}! là: {total}")

print("Bài 14.7")
list1=[1,2,3,4,5,6,-2,7,-5,8,4,9,-1]
for i in list1:
    if i<0:
        print(i)

print("Bài 14.8")
list2=[1,2,3,4,5,6,-2,7,-5,8,4,9,-1]
for i in list2:
    print(i)

print("Bài 14.9")
list3=[1,2,3,4,5,6,-2,7,-5,8,4,9,-1]
for index,value in enumerate(list3):
    print(f"Index: {index}, Value: {value}")

print("Bài 14.10")
for i in range(5):
    print("*"*5)