# a là số chia hết cho 5 nhưng KHÔNG nằm trong khoảng từ 20 - 70
a = int(input("Nhập vào a: "))
j = a
if j % 5 ==0 :
    j = not (20 <= j <= 70)
    print("True")
else:
    print("False")