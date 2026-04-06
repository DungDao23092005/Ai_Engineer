# Lists, Sets, and Tuples in Python
#Lists là một kiểu dữ liệu có thể chứa nhiều giá trị khác nhau, có thể thay đổi được và được sắp xếp theo thứ tự. Lists được sử dụng để lưu trữ các phần tử có thể thay đổi và có thể chứa các phần tử trùng lặp. Lists được tạo bằng cách sử dụng dấu ngoặc vuông [] và các phần tử được phân tách bằng dấu phẩy.
#set là một kiểu dữ liệu không có thứ tự, không chứa các phần tử trùng lặp và có thể thay đổi được. Sets được sử dụng để lưu trữ các phần tử duy nhất và thực hiện các phép toán tập hợp như hợp, giao, hiệu và đối xứng.
#tuples là một kiểu dữ liệu có thể chứa nhiều giá trị khác nhau, có thể thay đổi được nhưng không thể thay đổi sau khi đã tạo ra. Tuples được sử dụng để lưu trữ các giá trị không thay đổi và có thể được sử dụng làm khóa trong từ điển hoặc phần tử trong tập hợp.

# Ví dụ về Lists
#fruits = ["apple", "banana", "cherry","coconut"]
#print(fruits)  # Output: ['apple', 'banana', 'cherry']
#print(fruits[0:3:1])  # Output: ['apple', 'banana', 'cherry']

#for fruit in fruits:
    #print(fruit)

#print(dir(fruits))  # Output: ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
#help(fruits)
#print(len(fruits))  # Output: 4
#fruits.append("pineapple")
#fruits[0] = "orange"
#fruits.insert(1,"grape") #chèn "grape" vào vị trí index 1
#fruits.remove("banana") #xóa phần tử "banana" khỏi list
#fruits.pop() #xóa phần tử cuối cùng của list
#fruits.sort() #sắp xếp list theo thứ tự tăng dần
#fruits.reverse() #đảo ngược thứ tự của list
#fruits.clear() #xóa tất cả phần tử khỏi list
#fruits_copy = fruits.copy() #tạo một bản sao của list fruits
#fruits_count = fruits.count("apple") #đếm số lần xuất hiện của phần tử "apple" trong list
#fruits_index = fruits.index("cherry") #tìm vị trí index của phần tử "cherry" trong list 

# Ví dụ về Sets
#my_set = {1, 2, 3, 4, 5}
#my_set[0] = 10  # Lỗi: Sets không thể thay đổi sau khi đã tạo ra
#print(my_set)  # Output: {1, 2, 3, 4, 5}
#my_set.add(6)  # Thêm phần tử 6 vào set
#my_set.remove(3)  # Xóa phần tử 3 khỏi set
#print(my_set)  # Output: {1, 2, 4, 5, 6}

# Ví dụ về Tuples
#my_tuple = (1, 2, 3, 4, 5)
#print(my_tuple)  # Output: (1, 2, 3, 4, 5)
#my_tuple[0] = 10  # Lỗi: Tuples không thể thay đổi sau khi đã tạo ra
# Tuples có thể chứa các phần tử trùng lặp
#my_tuple_with_duplicates = (1, 2, 2, 3, 4)
#print(my_tuple_with_duplicates)  # Output: (1, 2, 2, 3, 4)

'''print("Bài 1")
# Bài 1
my_list = [1,2,3,4,5]
print(my_list)  # Output: [1, 2, 3, 4, 5]

print("Bài 2")
# Bài 2
numbers = [10, 20, 30, 40, 50]
print(numbers[0])  # Output: 10
print(numbers.pop())  # Output: 50

print("Bài 3")
# Bài 3
fruits = ["apple", "banana", "orange"]
fruits[1] = "mango"
print(fruits)  # Output: ['apple', 'mango', 'orange']

print("Bài 4")
# Bài 4
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)
numbers.append(6)
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]

print("Bài 5")
# Bài 5
total = 0
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    total += number
print(total)  # Output: 15

print("Bài 6")
# Bài 6
max_number = 0
numbers = [2, 4, 6, 8, 10]
for number in numbers:
    if number > max_number:
        max_number = number
print(max_number)  # Output: 10

print("Bài 7")
# Bài 7
numbers = [1, 2, 2, 3, 4, 2, 5]
print(numbers.count(2))  # Output: 3

print("Bài 8")
# Bài 8
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 8, 9]
numbers.reverse()
print(numbers)  # Output: [9, 8, 5, 2, 1]

print("Bài 9")
# Bài 9
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers_chan = []
for number in numbers:
    if number % 2 == 0:
        numbers_chan.append(number)
print(numbers_chan)  # Output: [2, 4, 6, 8]

print("Bài 10")
# Bài 10
n =int(input("Nhập số n: "))
numbers = []
for i in range(1,n+1):
    x=int(input(f"Nhập số thứ {i}: "))
    numbers.append(x)
print(numbers)  # Output: [1, 2, 3, ..., n]
print(sum(numbers))  # Output: Tổng của các số đã nhập
print(max(numbers))  # Output: Số lớn nhất trong các số đã nhập
print(min(numbers))  # Output: Số nhỏ nhất trong các số đã nhập'''

'''# Bài tập về tuple
print("Bài 1")
# Bài 1
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple)  # Output: (10, 20, 30, 40, 50)

print("Bài 2")
# Bài 2
colors = ("red", "green", "blue")
print(colors[0])# Output: "red"
print(colors[-1])# Output: "blue"

print("Bài 3")
# Bài 3
colors = ("red", "green", "blue")
for color in colors:
    print(color)

print("Bài 4")
# Bài 4
total =0
numbers = (1, 2, 3, 4, 5)
for number in numbers:
    total += number
print(total)

print("Bài 5")
# Bài 5
numbers = (1, 2, 2, 3, 4, 2, 5)
print(numbers.count(2))

print("Bài 6")
# Bài 6
max_number = 0
numbers = (5, 8, 2, 9, 1)
for number in numbers:
    if number>max_number:
        max_number=number
print(max_number)

print("Bài 7")
# Bài 7
data = (100, 200, 300, 400, 500)
print(data[:3])  # Output: (200, 300, 400)
print(data[-2:])  # Output: (400, 500)

print("Bài 8")
# Bài 8
point = (10, 20)
x,y=point
print(f"x={x}, y={y}")

print("Bài 9")
# Bài 9
numbers = (1, 2, 3, 4, 5)
numbers_list = list(numbers)
print(numbers_list)  # Output: [1, 2, 3, 4, 5]
numbers_list.append(6)
numbers = tuple(numbers_list)
print(numbers)  # Output: (1, 2, 3, 4,  5, 6)

print("Bài 10")
# Bài 10
n = int(input("Nhập số n: "))
my_tuple = ()
for i in range(1, n+1):
    x = int (input(f"Nhập số thứ {i}: "))
    my_tuple += (x,)
print(my_tuple)  # Output: (1, 2, 3, ..., n)'''

# Bài tập về set
print("Bài 1")
# Bài 1
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

print("Bài 2")
# Bài 2
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)  # Output: {1, 2, 3, 4}

print("Bài 3")
# Bài 3
numbers = {1, 2, 3, 4}
numbers.remove(2)
print(numbers)  # Output: {1, 3, 4}

print("Bài 4")
# Bài 4
numbers = [1, 2, 2, 3, 4, 4, 5, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

print("Bài 5")
# Bài 5
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
union = a.union(b)
print(union)  # Output: {1, 2, 3, 4, 5, 6}
intersection = a.intersection(b)
print(intersection)  # Output: {3, 4}
difference = a.difference(b)
print(difference)  # Output: {1, 2}
symmetric_difference = a.symmetric_difference(b)
print(symmetric_difference)  # Output: {1, 2, 5,\   6}

print("Bài 6")
# Bài 6
numbers = {10, 20, 30, 40, 50}
x=30
if x in numbers:
    print("Co trong set")
else :
    print("khong co trong set")

print("Bài 7")
#Bài 7
n=int(input("Nhap so n:"))
numbers = set()
for number in range(1,n+1):
    x=int(input(f"Nhap so thu {number} :"))
    numbers.add(x)
print(numbers)

print("Bài 8")
#Bài 8
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common=set(list1) & set(list2)

print("Cac phan tu chung",common)

print("Bài 9")
#Bài 9
text = "programming"
my_set1=set(text)
print(my_set1)

print("Bài 10")
#Bài 10
dem = 0
m = input("Nhap 1 cau: ")
my_set2 = set(m.split())

for x in my_set2:
    dem += 1

print(my_set2)
print(dem)