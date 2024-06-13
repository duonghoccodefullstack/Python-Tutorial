import math
a = float(input("nhập số a: "))
b = float(input("nhập số b: "))
c = float(input("nhập số c: "))

delta = b**2 - 4*a*c
if delta == 0:
    x = -b / (2*a)
    print(f"Phương trình nhiệm kép.")
    print(f"x= {x}")
elif delta >0 :
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print(f"Phương trình 2 nhiệm phân biệt.")
    print(f"x1= {x1}")
    print(f"x2= {x2}")
else:
    print("Phương trình vô nhiệm. ")


     

