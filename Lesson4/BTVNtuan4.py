An = float(input("Nhập vào chiều cao của An (đơn vị mét)"))
Minh = float(input("Nhập vào chiều cao của Minh (đơn vị mét)"))
Lan = float(input("Nhập vào chiều cao của Lan(đơn vị mét)"))

if An >= Minh and An >= Lan:
    cao_nhat = An
    nguoi_cao_nhat = "An"
elif Minh >= An and Minh >= Lan:
    cao_nhat = Minh
    nguoi_cao_nhat = "Minh"
else:
    cao_nhat = Lan
    nguoi_cao_nhat = "Lan"

print( nguoi_cao_nhat, "là người cao nhất với chiều cao:", cao_nhat, "mét")