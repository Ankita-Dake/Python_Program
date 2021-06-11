n = int(input("enter number"))
if n % 4 == 0 and n % 100 == 0 and n % 400 ==0 :
    print(" Leap year")
else:
    print("not leap year")