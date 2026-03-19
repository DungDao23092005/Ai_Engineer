import math

'''friends=5
#friends+=1
#friends-=1
friends*=2
print(friends)
# Toán tử cộng (+), trừ (-), nhân (*), chia (/), chia lấy phần nguyên (//), chia lấy phần dư (%), lũy thừa (**)
a=int(input("Nhap so a:"))
b=int(input("Nhap so b:"))
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")
print(f"a ** b = {a ** b}")

# các hàm khác

x =3.14
y=4
z=5

result1 = round(x)
result2 = abs(-y)
result3 = max(x, y, z)
result4 = min(x, y, z)
result5 = pow(y, 2)

print(f"round({x}) = {result1}")
print(f"abs(-{y}) = {result2}")
print(f"max({x}, {y}, {z}) = {result3}")
print(f"min({x}, {y}, {z}) = {result4}")
print(f"pow({y}, 2) = {result5}")'''

# Sử dụng hàm trong module math

print(math.pi)
print(math.e)
result1 = math.sqrt(16)
result2 = math.floor(9.9) # làm tròn xuống, trả về số nguyên lớn nhất nhỏ hơn hoặc bằng số đã cho
result3 = math.ceil(9.1) # làm tròn lên, trả về số nguyên nhỏ nhất lớn hơn hoặc bằng số đã cho
print(result1)
print(result2)
print(result3)

# tính chu vi và diện tích hình tròn
radius = float(input("Nhap ban kinh hinh tron: "))
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"Chu vi hinh tron la: {circumference}")
print(f"Dien tich hinh tron la: {area}")