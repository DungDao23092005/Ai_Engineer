# if trong Python là một cấu trúc điều khiển cho phép chúng ta thực hiện một khối mã nếu một điều kiện nào đó là đúng. Cấu trúc cơ bản của câu lệnh if như sau:
# if condition:
#     # code to execute if condition is true
# else:
#     # code to execute if condition is false
# Chúng ta có thể sử dụng các toán tử so sánh để tạo điều kiện, ví dụ: ==, !=, >, <, >=, <=. Dưới đây là một ví dụ về cách sử dụng if trong Python:
# ví dụ 1 về tuổi
'''age = int(input("Nhap tuoi cua ban: "))

if age >= 18 and age < 60:
    print(f"Ban la nguoi trung nien.")

elif age >= 60:
    print(f"Ban la nguoi gia.")    

elif age < 18 and age >= 0:
    print(f"Ban la tre em.")

else:
    print(f"Tuoi khong hop le.")'''

# ví dụ 2 về phép toán
num1 = float(input("Nhap so thu nhat: "))
num2 = float(input("Nhap so thu hai: "))
operation = input("Nhap phep toan (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"Kết quả: {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"Kết quả: {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"Kết quả: {num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Kết quả: {num1} / {num2} = {result}")
    else:
        print("Khong the chia cho 0, vui long nhap lai so thu hai.")
else:
    print("Phep toan khong hop le.")
