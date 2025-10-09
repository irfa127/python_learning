
# 🔹 1. print() basics

# Write a Python program to print the area of a square whose side length is 8.
def sq_area(a,b):
    print(a*b)
sq_area(8,8)   

# 🔹 2. Operators

# Write a Python program to find the remainder when 57 is divided by 6.
def div_rem(n):
    print(n%6)
div_rem(57)    

# 🔹 3. Conditions (if / else)

# Write a Python program to check if a given number is positive or negative.
def if_else(a):
    if a>=0:
        print('positive')
    else:
        print('negative')    
if_else(5)    

# 🔹 4. match case

# Write a Python program that takes a symbol (+, -, *, /) and two numbers, then performs the correct operation using match case.
def match_case(a,b,op):
    match op:
        case '+':
            print(a+b)
        case '-':
            print(a-b) 
        case '*':
            print(a*b) 
        case '/':
            print(a/b)  
        case _:
            print('invalid input')            
match_case(5,8,'*')
match_case(5,8,'+')
match_case(5,8,'-')
# 🔹 5. Loops

# (a) While loop: Print numbers from 1 to 10 using a while loop.

def while_loop(a):
    while a<=10:
        print(a)
        a=a+1
while_loop(1)        
# (b) For loop: Print the multiplication table of 7 using a for loop.

def for_loop(a):
    for i in range(a,10+1):
        print(a,'x7',i*7)
        
for_loop(1)    

# 🔹 6. Swap

# Write a Python program to swap the values of two variables a = 5 and b = 10.
# def swap_py(a,b):
#     a,b=b,a
#     print(a,b)
    
# swap_py(5,10)    

# sum while loop

# a=int(input("enter the value"))
# 2	b=20
# 3	sum=0
# 4	while a<=b:
# 5	    sum=sum+a
# 6	    a=a+1
# 7	print(sum)


# sum squrae
# a=int(input('enter'))
# 2	b=6
# 3	sum=0
# 4	while a<=b:
# 5	    sum=sum+a**2
# 6	    print(a**2)
# 7	    a=a+1
# 8	print('sum',sum)

# fabinoice serias

# n=int(input("enter the value"))
# 2	a=1
# 3	while n>0:
# 4	     print(a**2+1)
# 5	     a=a+1
# 6	     n= n-1

# break & continue

# i = 1
# while i <= 10:
#     if i == 5:
#         i += 1        
#         continue     
#     if i == 8:
#         break         
#     print(i)
#     i += 1


# 1️⃣ Counting Numbers 1 to N
# N = 10
# for i in range(1, N+1):
#     print(i)

# 2️⃣ Sum of Numbers 1 to N
# N = 5
# total = 0
# for i in range(1, N+1):
#     total += i
# print("Sum =", total)

# 3️⃣ Factorial of a Number
# N = 5
# fact = 1
# for i in range(1, N+1):
#     fact *= i
# print("Factorial =", fact)

# 4️⃣ Even Numbers 1 to N
# N = 10
# for i in range(1, N+1):
#     if i % 2 == 0:
#         print(i)

# 5️⃣ Odd Numbers 1 to N
# N = 10
# for i in range(1, N+1):
#     if i % 2 != 0:
#         print(i)

# 6️⃣ Fibonacci Series (First N Terms)
# N = 7
# a, b = 0, 1
# for _ in range(N):
#     print(a)
#     a, b = b, a + b

# 7️⃣ Break and Continue Example
# for i in range(1, 11):
#     if i == 5:
#         continue  # skips 5
#     if i == 8:
#         break     # stops loop at 8
#     print(i)


# Output:

# 1 2 3 4 6 7

# 8️⃣ Multiplication Table
# N = 5
# for i in range(1, 11):
#     print(N, "x", i, "=", N*i)

# 9️⃣ Nested Loop / Pattern
# rows = 3
# for i in range(1, rows+1):
#     for j in range(i):
#         print("*", end="")
#     print()


# Output:

# *
# **
# ***

# 🔟 Loop with Else
# for i in range(1, 4):
#     print(i)
# else:
#     print("Done")


# Output:

# 1
# 2
# 3
# Done