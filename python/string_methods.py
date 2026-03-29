# String methods in Python
# Dưới đây là một số phương thức (method) phổ biến để làm việc với chuỗi (string) trong Python:
#name = input("Enter your name: ")
#phone_number = input("Enter your phone number: ")
#result = len(name)
#result = name.find("a") # tìm vị trí đầu tiên của chữ "a" trong chuỗi, nếu không tìm thấy sẽ trả về -1
#result = name.rfind("a") # tìm vị trí cuối cùng của chữ "a" trong chuỗi, nếu không tìm thấy sẽ trả về -1    
#name =name.capitalize() # viết hoa chữ cái đầu tiên của chuỗi
#name = name.upper() # chuyển tất cả các chữ cái trong chuỗi thành chữ hoa
#name = name.lower() # chuyển tất cả các chữ cái trong chuỗi thành chữ thường
#result = name.isdigit() # kiểm tra xem chuỗi có phải là một số hay không, trả về True hoặc False
#result = name.isalpha() # kiểm tra xem chuỗi có phải là một chuỗi chỉ chứa chữ cái hay không, trả về True hoặc False
#result = phone_number.count("-") # đếm số lần xuất hiện của ký tự "-" trong chuỗi
#result = phone_number.replace("-", "") # thay thế tất cả các ký tự "-" bằng một chuỗi rỗng, tức là loại bỏ chúng khỏi chuỗi
#print(result)
#print(name)

username = input("Enter your username: ")

if len(username) > 12:
    print("Username is too long. Please choose a username with 12 characters or less.")
elif not username.find(" ") == -1:
    print("Username should not contain spaces. Please choose a username without spaces.")
elif not username.isalpha():
    print("Username should only contain letters. Please choose a username with letters only.")
else:
    print(f"Welcome, {username}!")

