a = int(input("enter no. a"))
b = int(input("enter no. b"))
c = int(input("enter no. c"))
if a > b and a >c:
    print("largest number is", a)
elif b > a and b > c:
    print("largest no. is",b)
else:
    print("largest no. is",c)