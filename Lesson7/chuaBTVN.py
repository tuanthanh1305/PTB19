# ​Chọn số yêu thích gán vào 1 biến
# Nhập từ bàn phím số may mắn
# Nếu sai thì thông báo cho họ biết lớn hơn hay bé hơn 
secrets_number = 12
while True:
    n = int(input("Nhập vào số n"))
    
    if n == secrets_number:
        print("Corect!")
        break
    
    if n > secrets_number:
        print("Bigger")
        continue