# for loop in Python
# Dưới đây là một số ví dụ về cách sử dụng vòng lặp for trong Python:

# reversed đảo ngược một chuỗi hoặc một dãy số
# range(start, stop, step) tạo ra một dãy số từ start đến stop (không bao gồm stop) với bước nhảy step
'''for x in reversed(range(1,11,2)):
    print(x)

print("Happy New Year!")'''

# Bài 1
for i in range(1,6):
    print(i)

print("Bài 2")
# Bài 2
for i in reversed(range(1,6)):
    print(i)

print("Bài 3")
# Bài 3
for i in range(2,11,2):
    print(i)

print("Bài 4")
# Bài 4
sum =0
for i in range(1,11):
    sum +=i
print(f"Tổng các số từ 1 đến 10 là: {sum}")

print("Bài 5")
# Bài 5
giaithua =1
for i in range(1,6):
    giaithua *=i
print(f"Giai thừa của 5 là: {giaithua}")

print("Bài 6")
# Bài 6
text = "Python"
for char in text:
    print(char)

print("Bài 7")
# Bài 7
sum = 0
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    sum += num
print(f"Tổng của các số trong danh sách là: {sum}")

print("Bài 8")
# Bài 8
for i in range(1,11):
    print(f"5 * {i} = {i*5}")

print("Bài 9")
# Bài 9
dem =0
n=int(input("Nhap so n: "))
for i in range(0,n+1):
    if i == 0:
        continue
    elif i %3 == 0:
        print(i,sep =", ",end=",")
        dem+=1
print(f"\nCó {dem} số chia hết cho 3 từ 0 đến {n}")

print("Bài 10")
# Bài 10
a = int(input("Nhap so a: "))
if a <=1 :
    print("Khong phai so nguyen to")
else:
    for i in range(2,a):
        if a % i == 0:
            print("Khong phai so nguyen to")
            break
    else:
        print("La so nguyen to")