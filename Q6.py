a=int(input("Enter coefficient of x^2 : ")) #Coeff of  x**2
b=int(input("Enter coefficient of x : "))   #Coeff of  x
c=int(input("Enter constant : "))  #constant
d=((b**2)-(4*a*c))
x1 = (-b + (d**0.5))/2*a
x2 = (-b - (d**0.5))/2*a


if d<0: #Check if roots are Imaginary
    print("Imaginary Equation")
elif d==0:  #Check f roots are equal
    x1=(-b)/(2*a)
    x1=x2
else:   #If roots are unequal
    x1=(-b+(d**(0.5)))/(2*a)
    x1=(-b-(d**(0.5)))/(2*a)
print("Roots of the equation are",x1,x2)