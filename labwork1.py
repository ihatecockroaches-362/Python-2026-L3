import numpy as np
import math
def ex1():
    r = float(input("enter circle radius: "))
    area = round(math.pi * (r**2),1)
    print(f"Circle area = {area}")
    
def ex2():
    c = float(input("enter the temperature in celcius: "))
    f = c*1.8 + 32
    print(f"{c} (C) = {f} (F)")
    
def ex3():
    p = int(input("Enter prime number: "))
    is_prime = True
    if p < 2:
        is_prime = False
    else:
        for i in range ( 2,math.sqrt(p)+1):
            if p%i == 0:
                is_prime = false
                break
    if is_prime:
        print("This is prime number") 
    else:
        print("this is not prime number")
def ex4():
    total = 0
    p_num = int(input("nhap so tu nhien: "))
    for i in range(1, p_num):
        if (p_num % i == 0):
            total += i
    if ( total == p_num):
        print("This is perfect number!")
    else:
        print("This is not perfect number!")
        
def ex5():
    s = ["red", "blue","green","white","black"]
    index = -1
    word = input("What is your favorite color?: ")
    for i in range(0,len(s)):
        if (word == s[i]):
            index = i
        break
    if (index != -1) :
        print(f"Your color is at index {i} in my list")
    else:
        print("can not found")
def ex6():
    range1 = list(range(7))
    print("range1:",range1)
    range2 = list(range(1,10,3))
    print("range2:",range2)
    range3 = list(range(5,1,-1))
    print("range3:",range3)
    range4 = list(range(6,-3,-2))
    print("range4:",range4)

def ex7(s):
    arr = list(s)
    for i in range(len(arr)):
        if (arr[i] == "$"):
            arr[i] = ""
    new_s = "".join(arr)
    print(f"{new_s}")
    
def ex8(I):
    n = len(I)
    new_I = []
    for i in range(n):
        if(I[i] % 2 == 0):
            m = I[i]
            new_I.append(m)
    for i in range(len(new_I)):
        print(f"new_I[i]") 

def ex9(num):
    total = 1
    if (num < 0):
        print("error")
    elif( num == 0) :  
        print("0! = 1") 
    else:    
        for i in range (1,num+1):
            total *= i
        print(total)

def ex10(d_num):
    for i in range (1,d_num +1):
        if (d_num % i == 0):
            print(i, end =" ")
            
            
def ex11():
    distance = float(math.sqrt(((p1[0]-p2[0])**2) +((p1[1]-p2[1])**2)))
    print(f"{distance:.2f}")

def ex12():
    m = input("enter row m: ")
    n = input("enter column n: ")
    for i in range (1,int(m) + 1):
        if (i == 1 or i == int(m)):
            print(int(n) * "*")
        else:
            print("*"+(int(n)-2) * " "+"*")  
            
#remove the comment to run each exercises                      
        
#ex1()
#ex2()
#ex3()
#ex4()
#ex5()
#ex6()
#ex7("$$$BACH$$$$$$ds$hd$hsah")
#ex8(12)
#ex9(18)
#ex10(10)
'''
p1 = [12,13]
p2 = [14,15]
ex11()
'''
#ex12()