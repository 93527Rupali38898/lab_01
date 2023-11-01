a = float(input("enter length 1 of triangle in cm:"))
b = float(input("enter length 2 of triangle in cm:"))
c = float(input("enter length 3 of triangle in cm:"))
s = (a+b+c)/2
area = ((s*(s-a)*(s-b)*(s-c))**0.5)
print("area of triangle is", area)