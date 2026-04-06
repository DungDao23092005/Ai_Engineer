# nested loop in Python
# giải thích: vòng lặp lồng nhau là khi một vòng lặp được đặt bên trong một vòng lặp khác. Vòng lặp bên trong sẽ được thực hiện hoàn chỉnh cho mỗi lần thực hiện của vòng lặp bên ngoài.

# ví dụ về vòng lặp lồng nhau để in ra một hình chữ nhật bằng ký tự "*":
'''rows=int(input("Nhap so dong: "))
columns=int(input("Nhap so cot: "))
sybol = str(input("Nhap ky tu: "))

for x in range(rows):
    for i in range(columns):
        print(sybol,end=" ")
    print() # in một dòng mới sau khi hoàn thành vòng lặp bên trong'''

# ví dụ về tam giác vuông bằng kí tự "*" người dùng nhập vào 1 số nguyên :
'''n=int(input("Nhap so n: "))
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()

matrix = [
    [1, 2, 3,7],
    [4, 5, 6,6],
    [7, 8, 9,10]
]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()'''

print("Bài 1")
# Bài 1
for i in range(3):
    for j in range(5):
        print("*", end=" ")
    print()

print("Bài 2")
# Bài 2
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()

print("Bài 3")
# Bài 3
for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print()

print("Bài 4")
# Bài 4
for i in reversed(range(1,6)):
    for j in range(i):
        print("*", end=" ")
    print()

print("Bài 5")
# Bài 5
for i in range(2,5):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}",end = " ")
    print()

print("Bài 6")
# Bài 6
for i in range(3):
    for j in range(1,4):
        print(f"{j}", end=" ")
    print()

print("Bài 7")
# Bài 7
dem=0
for i in range(3):
    for j in range(3):
        dem+=1
        print(dem, end=" ")
    print()

print("Bài 8")
# Bài 8
sum = 0
for i in range(1,4):
    for j in range(1,3):
        print (f"({i},{j})", end=" ")
        sum += 1
print(f"\nTổng số cặp (i,j) là: {sum}")

print("Bài 9")
# Bài 9
a = int(input("Nhap so a: "))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(f"{j}",end=" ")
    print()

print("Bài 10")
# Bài 10
n = int(input("Nhap so n: "))
for i in range(2,n+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")