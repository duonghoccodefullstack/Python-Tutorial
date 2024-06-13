#Nhập n (n>0)
while True: #vòng lặp vô hạn
    try:
        n = int(input("Nhập n > 0: "))
        if n > 0:
            break
        else:
            print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    except ValueError: #khối mã xử lý ngoại lệ
        print("Vui lòng nhập một số nguyên hợp lệ.")
        
# chuyển từ thập phân sang nhị phân
x = n
ketQua = ""
while x > 0:
    ketQua = str(x % 2) + ketQua
    print("x % 2 =", x % 2)
    x = x // 2
    print("x =", x)
print("Kết quả:", ketQua)

