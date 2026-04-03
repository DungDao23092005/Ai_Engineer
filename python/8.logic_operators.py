# phép toán logic trong Python bao gồm các toán tử AND, OR, NOT. Chúng được sử dụng để kết hợp các điều kiện và trả về giá trị boolean (True hoặc False). Dưới đây là một số ví dụ về cách sử dụng các toán tử logic trong Python:
# AND (và): Toán tử AND trả về True nếu cả hai điều kiện đều đúng, ngược lại trả về False.
# OR (hoặc): Toán tử OR trả về True nếu ít nhất một trong hai điều kiện đúng, ngược lại trả về False.
# NOT (phủ định): Toán tử NOT trả về True nếu điều kiện là False, và ngược lại trả về False nếu điều kiện là True.
# ví dụ 1 về điểm số 
score =float(input("Nhap diem cua ban: "))
if score >= 8.5 and score <= 10:
    print("Ban dat loai gioi.")
elif score >= 7.0 and score < 8.5:
    print("Ban dat loai kha.")
elif score >= 5.0 and score < 7.0:
    print("Ban dat loai trung binh.")
elif score >= 5 and score < 5.0:
    print("Ban dat loai yeu.")
else:
    print("Ban da rot.")