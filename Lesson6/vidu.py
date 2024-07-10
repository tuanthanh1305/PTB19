# for i in range(3,10):
#     print("Hello World")

# for i in range(6):
#     print(i)

# Nhập hai số nguyên a và b từ bàn phím
# a = int(input("Nhập số nguyên a: "))
# b = int(input("Nhập số nguyên b: "))

# Đảm bảo a luôn nhỏ hơn hoặc bằng b
# if a > b:
#     a, b = b, a

# Tính tổng các số chẵn từ a đến b
# sum = 0
# for i in range(a, b + 1):
#     if i % 2 == 0:
#         sum += i

# In kết quả
# print("Tổng các số chẵn từ", a, "đến", b, "là:", sum)

print("Bảng cửu chương")
for i in range(2,10):
    for j in range(1,11):
        result = i * j
        print(i, "*", j,"=", result)
    print()

