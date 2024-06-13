a = int(input("Nhập a:"))
if a<=0:
    print("vui lòng nhập ngdương")
else:
    for i in range(1,10):
        ket_qua = a * i
        print(f"{a} * {i} = {ket_qua}")