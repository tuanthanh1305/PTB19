# nhập số nguyên dương n
# Xuất ra dãy tăng dần bắt đầu từ 1 để tổng dãy số > n và dãy số ngắn nhất
n = int(input("Nhập vào số nguyên dương n"))

sum = 0 # biến tính tổng
i = 1 # biến đếm

print("Dãy số:")
while sum < n:
    print(i, end =" ")
    sum += i
    i += 1
    
