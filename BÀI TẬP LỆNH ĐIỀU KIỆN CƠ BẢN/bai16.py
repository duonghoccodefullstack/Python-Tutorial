a = int(input("nhập số a: "))
b = int(input("nhập số b: "))
c = float(input("nhập số c: "))
if a == b:
    print("Tam giác cân")
elif a != b != c :
    print("Tam giác thường")
elif  a == b and a**2 + b**2 == c**2  : 
    print("Tam giác vuông cân")
elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 :
    print("tam giác vuông")

   
    