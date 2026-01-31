# WAP to check if a number entered by user is Odd or Even.

num= int(input("Enter a number:"))
if(num%2==0):
    print("Even")
else:
    print("Odd")

#WAP to find the greatest of 3 numbers entered by user.

a= int(input("Enter first number:"))
b= int(input("Enter second number:"))
c= int(input("Enter third number:"))
if(a>=b and a>=c):
    print("first number is greater",a)
elif(b>c):
    print("second number is greater",b)
else:
    print("third number is greater",c)

# WAP to check if a number is multiple of 7 or not.

x= int(input("Enter number:"))
if(x%7==0):
    print("multiple of 7")
else:
    print("not multiple of 7")


















