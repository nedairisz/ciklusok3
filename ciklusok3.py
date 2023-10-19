import math
"""
1.	Írj programot, mely bekér a felahsználótól egy pozitív egész számot, 
és kiírja az egész számokat a képernyőre eddig a számig, egymástól pontosvessszővel elválasztva! 
Az utolsó szám után ne legyen pontosvessző! 
"""
def feladat1(szam:int):
    i = 1
    while i <= szam:
        if i == szam - 1:
            print(i)
        else:
            print(i, end=", ")
        i += 1

"""2.	Írj programot, mely beolvas egy pozitív egész számot, 
és kiírja az osztóit, valamint az osztóinak az összegét! """

def feladat2(a:int):
    i = 1
    osszeg = 0
    while i <= a:
        if a % i == 0:
            print(f"{i}", end=", ")
            osszeg += 1
        i += 1
    print(f"\nAz osztók összege: {osszeg}")

"""3.	Írj programot, amely kiírja két bekért szám között a páros számokat!"""
def feladat3(a:int, b:int):
    i: int = a
    while i <= b:
        if i % 2 == 0:
            print(f"{i}", end=", ")
        i += 1

"""4.	Írj programot, amely kiírja az első 20  négyzetszámot!"""
def feladat4():
    i = 0
    negyzet = 0
    while i <= 20:
        print(f"{i}", end=", ")
        negyzet = i ** 2
        i += 1
        print(f"\nAz első 20 négyzetszám: {negyzet}")