# string indexing in Python
# Dưới đây là một số ví dụ về cách sử dụng chỉ mục (indexing) để truy cập các ký tự trong chuỗi (string) trong Python:
# [start : end : step]

credits_number = "1234567890"
# Truy cập
print(credits_number[0])  # In ra ký tự đầu tiên
print(credits_number[:4])  # In ra các ký tự từ vị trí 0 đến 3
print(credits_number[4:8])  # In ra các ký tự từ vị trí 4 đến 7
print(credits_number[4:10])  # In ra các ký tự từ vị trí 4 đến cuối chuỗi
print(credits_number[::2])  # In ra các ký tự ở vị trí chẵn (0, 2, 4, 6, 8)

# đảo ngược chuỗi
credits_number = credits_number[::-1]
print(credits_number)  # In ra chuỗi đã được đảo ngược