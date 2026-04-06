# hàm trong python
# hàm là một khối mã có thể tái sử dụng để thực hiện một nhiệm vụ cụ thể. Nó giúp tổ chức mã, làm cho nó dễ đọc và bảo trì hơn. Dưới đây là một số ví dụ về cách định nghĩa và sử dụng hàm trong Python:
# Định nghĩa một hàm đơn giản
'''def greet(name):
    return f"Hello, {name}!"

# Gọi hàm
print(greet("Alice"))  # Output: Hello, Alice!'''

'''def happy_birthday(name, old):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print(f"Happy Birthday dear {name}!")
    print(f"Happy Birthday to you! You are now {old}.")

# Gọi hàm
happy_birthday("Dung", 25)'''

print("Bài 1")
#Bài 1
def xinchao():
    print("Xin chao ban")

xinchao()

print("Bài 2")
#Bài 2
def chao_ten(name):
    print(f"Xin chao {name}")

chao_ten("Dung")

print("Bài 3")
#Bài 3
def tong(a,b):
    return a+b

print(tong(3,5))

print("Bài 4")
#Bài 4
def binh_phuong(x):
    return x*x

print(binh_phuong(4)) #16

print("Bài 5")
#Bài 5
def la_so_chan(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(la_so_chan(6))#True
print(la_so_chan(7))#False

print("Bài 6")
#Bài 6
def so_lon_hon(a,b):
    if a>b:
        return a
    else:
        return b

print(so_lon_hon(10,7))#10

print("Bài 7")
#Bài 7
def giai_thua(n):
    if n== 0 or n==1:
        return 1
    else:
        return n*giai_thua(n-1)
    
print(giai_thua(5))#120

print("Bài 8")
#Bài 8
def dem_so_chan(numbers):
    count = 0
    for i in numbers:
        if i %2 == 0 :
            count+=1
    return count

print(dem_so_chan([1, 2, 3, 4, 6]))   # 3

print("Bài 9")
#Bài 9
def tim_max(numbers):
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    return max

print(tim_max([3, 7, 2, 9, 5]))   # 9

print("Bài 10")
#Bài 10
def tinh_toan(a,b):
    tong = a+b
    hieu =a-b
    tich=a*b
    thuong = a/b
    return tong,hieu,tich,thuong

tong,hieu,tich,thuong=tinh_toan(8,3)
print(tong)
print(hieu)
print(tich)
print(thuong)