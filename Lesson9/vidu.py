# # Toán tử in trả về: True or False
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# giatri= 10 in A
# print(giatri)
# Thêm phần tử vào cuối danh sách
# A.append(10)
# print(A)
# Thêm phần tử vào vị trí chỉ định 
# A.insert(10,11)
# print(A)
# Câu lệnh xoá phần tử trong danh sách 
# remove xoá giá trị nào đó khỏi phần tử
# A.remove(9)
# print(A)
# pop xoá bằng chỉ số
# A.pop(0)
# print(A)
#xoá toàn bộ danh sách
# A.clear()
# print(A)

#Cập nhật phần tử trong danh sách
B = [1, 3, 2, 4, 5, 6, 7, 8, 9]
# B[0] = 0
# print(A)
# Sắp xếp danh sách theo thứ tự tăng dần
# B.sort()
# print(B)
# Sắp xếp theo thứ tự giảm dần
# B.sort(reverse = True)
# print(B)
# Nối phần tử trong danh sách
C = [10, 11, 12]
# D = B + C # lúc này đã là [1,2,3,4,5,6,7,8,9,10,11,12]
# print(D)
# sử dụng extend()
D.extend(C)
print(D)