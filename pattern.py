# * * * *
# * * * *
# * * * *
# * * * *
def squarepatt(n):
    for i in range(0, n):
        for j in range(0, n):
            print("* ", end=" ")
        print("\r")


n = int(input("enter no."))
squarepatt(n)


# *
# * *
# * * *
# * * * *
def patt(n1):
    for i in range(0, n1):
        for j in range(0,i+1):
            print("* ", end=" ")
        print("\r")


n1 = int(input("enter no."))
patt(n1)


# * * * *
# * * *
# * *
# *
def pattern(n2):
    for i in range(0, n2):
        for j in range(0, n-i):
            print("* ", end=" ")
        print("\r")


n2 = int(input("enter no."))
pattern(n2)