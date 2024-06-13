def phuong_trinh (a,b):
    if a ==0 and b== 0: 
        print("Phương trình có vô số nghiệm.")
    elif a ==0 and b != 0:
        print("Phương trình không có nghiệm.")
    else:
        x = -b/a
        print(f"Phương trình có một nghiệm duy nhất: x = {x}")
a = float(input("nhập số a: "))
b = float(input("nhập số b: "))
phuong_trinh(a,b)
