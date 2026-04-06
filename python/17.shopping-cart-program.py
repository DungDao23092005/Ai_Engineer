foods = []
prices = []
total = 0

while True :
    food = input("Nhap thuc pham ban muon hoac nhan q de thoat:")
    if food.lower() == "q":
        break
    else:
        price = int(input("Nhap gia ma ban mua :"))
        if price < 0 :
            print("vui long nhap so duong")
        else:
            foods.append(food)
            prices.append(price)


print("----- Your Cart -----")

for food in foods :
    print(food ,end = " ")

for price in prices :
    total += price

print()
print(f"So tien ban can phai thanh toan la : {total}")