# vòng lặp while trong Python cho phép chúng ta thực hiện một khối mã nhiều lần miễn là một điều kiện nhất định còn đúng. Cấu trúc của vòng lặp while như sau:
# while condition:
#     # code to be executed
# Dưới đây là một số ví dụ về cách sử dụng vòng lặp while trong Python:

'''name = input("Enter your name: ")

while name == "":
    print("You did not enter a name. Please try again.")
    name = input("Enter your name: ")
print(f"Hello, {name}!")'''

# Bài 1
n=1
while n <6:
    print(n)
    n+=1

print("Bài 2")
# Bài 2
a = 5
while a>0:
    print(a)
    a-=1

print("Bài 3")
# Bài 3
b=2
while b<11:
    print(b)
    b+=2
    
print("Bài 4")
# Bài 4
c=1
sum = 0
while c<11:
    sum +=c
    c+=1
print(f"Tổng các số từ 1 đến 10 là: {sum}")

print("Bài 5")
# Bài 5
d=5
giaithua =1
while d>0:
    giaithua=giaithua*d
    d-=1
print(f"Giai thừa của 5 là: {giaithua}")

print("Bài 6")
# Bài 6
n=12345
dem=0
while n>0:
    dem+=1
    n//=10
print(f"Số chữ số của 12345 là: {dem}")

print("Bài 7")
# Bài 7
n=1234
reverse =0
while n>0:
    digit = n %10
    reverse = reverse *10 + digit
    n//=10
print(f"Số đảo ngược của 1234 là: {reverse}")

print("Bài 8")
# Bài 8
password = input("Enter your password: ")
while password !="python123":
    print("Password is incorrect!")
    password = input("Enter your password: ")
print("Password is correct. Welcome!")

print("Bài 9")
# Bài 9
total = 0
num = int(input("Enter a positive integer: "))
while num !=0:
    total +=num
    num = int(input("Enter a positive integer: "))
print(f"The sum of the entered numbers is: {total}")

print("Bài 10")
# Bài 10
secret=7
guess = int(input("Guess the secret number (between 1 and 10): "))
while guess != secret:
    if guess < secret:
        print("Nho hon dap an")
    else:
        print("Lon hon dap an")
    guess = int(input("Guess the secret number (between 1 and 10): "))
print("Chuc mung ban da doan dung!")