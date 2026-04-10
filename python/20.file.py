#file trong python là một đối tượng được sử dụng để lưu trữ dữ liệu trên đĩa. Python cung cấp các hàm tích hợp để làm việc với file, cho phép bạn đọc, ghi và quản
#lý file một cách dễ dàng. Dưới đây là một số ví dụ về cách làm việc với file trong Python:

#1. Mở file và ghi dữ liệu vào file
'''with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a file example.\n")
#2. Mở file và đọc dữ liệu từ file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)'''

#tạo file mới và ghi dữ liệu vào file
'''f = open("vidu1.txt","x") #tạo file mới
f.write("Hello, this is a new file.\n")
f.close()'''

# đọc file
'''f = open("vidu1.txt","r")
content = f.read()
# f.write("This line is added to the file.\n") #lỗi vì file đang ở chế độ đọc
print(content)
f.close()'''

#nối file
'''f = open("vidu1.txt","a") #mở file ở chế độ nối
f.write("This line is added to the file.\n")
f.close()'''

'''f = open("vidu1.txt","w") #mở file ở chế độ ghi, sẽ xóa nội dung cũ và ghi mới
for i in range(0,11):
    f.write("Xin chao cac ban\n")
f.close()'''

f=open("vidu1.txt","r",encoding="utf-8") #mở file ở chế độ đọc với encoding utf-8
danh_sach=f.readlines() #đọc tất cả các dòng trong file và trả về một danh sách
print(danh_sach)