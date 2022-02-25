import math

#WAP to print multiplication table of entered number
from glob import escape
from re import I
from this import d
from sqlalchemy import true


def ques_1():
    n = int(input("Enter the number "))
    for i in range (1,11):
        print(n, '*', i, '=', n*i)

#WAP to count digits of an entered number
def ques_2():
    c = 1
    n = int(input("Enter the number "))
    while (n > 10):
        c += 1
        n = n // 10
    print(c)

#WAP to print roots of a quadratic equation
def ques_3():
    a = float(input("Enter the coeffecient of x^2 "))
    b = float(input("Enter the coeffecient of x "))
    c = float(input("Enter the constant "))
    x1 = ((-b) + (math.sqrt((b**2) - (4*a*c)))) / (2*a)
    x2 = ((-b) - (math.sqrt((b**2) - (4*a*c)))) / (2*a)
    print("The roots are", x1, 'and', x2)

#WAP to check leap year
def ques_4():
    y = int(input("Enter the year "))
    if y%4 == 0:
        print(y, "is a leap year")
    else:
        print(y, "is not a leap year")

#WAP to convert celsius to farhenheit
def ques_5():
    t = int(input("Enter the temperature "))
    f = (t * (9/5)) + 32
    print(f, "is the temperature in farhenheit")

#WAP to make a simple calculator
def ques_6():
    a = int(input("Enter the first number "))
    o = input("Enter the operator ")
    b = int(input("Enter the second number "))
    if o == '+':
        s = a + b
    elif o == '-':
        s = a - b
    elif o == '*':
        s = a * b
    elif o == '/':
        s = a / b
    elif o == '//':
        s = a // b
    elif o == '%':
        s = a % b
    else:
        print("Enter a vaild operator")
    print(a, o, b, "is", s)

#WAP to make a simple grading system
def ques_7():
    D = {}
    n = int(input("Enter the number of grades"))
    for i in range(0,n):
        grade = input("Enter the grade ")
        marks = int(input("Enter its minimum marks "))
        D[marks]=grade
    a = int(input("Enter the marks of student"))
    for i in D.keys():
        if a > i:
            b = D[i]
            break
    print("The grade of the student is", b)

#WAP to find the largest of three entered numbers
def ques_8():
    a = int(input("Enter the first number "))
    b = int(input("Enter the second number "))
    c = int(input("Enter the third number "))
    if a > b and a > c:
        print(a, "is the largest number")
    elif b > a and b > c:
        print(b, "is the largest number")
    elif c > a and c > b:
        print(c, "is the largest number")
    else:
        print("The numbers are equal")
