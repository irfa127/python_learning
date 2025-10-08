# "Positive Even" if the number is positive and even

# def positive_even(n):
#     if n%2==0:
#             print('even')
#     else:
#         print('odd')    
# positive_even(8)


# Write a Python program that takes a number as input and prints:

# "Positive Even" → if number is positive AND even

# "Positive Odd" → if number is positive AND odd

# "Negative Even" → if number is negative AND even

# "Negative Odd" → if number is negative AND odd

# "Zero" → if number is 0

# Examples:

# Input: 8 → Output: "Positive Even"

# Input: 3 → Output: "Positive Odd"

# Input: -4 → Output: "Negative Even"

# Input: -5 → Output: "Negative Odd"

# Input: 0 → Output: "Zero"

# def pos_nav(a):
#   if a>0:
#       if a% 2==0:
#         print('even')
#       elif a% 2!=0:
#           print('odd')
#   elif a<0:
#           if a%2==0:
#               print('Negative Even')   
#           elif a % 2!=0:
#                print('Negative Odd')         
#   else:
#     print('zero')   
# pos_nav(8)     
# pos_nav(3)  
# pos_nav(-4)  
# pos_nav(-3) 
# pos_nav(0) 
       
 
# Write a Python program that takes three numbers as input and prints the largest number among them.

# Example:

# Input: 5, 8, 3 → Output: 8

# Input: -2, -5, -1 → Output: -1

# Input: 7, 7, 7 → Output: All numbers are equal


# def three_num(a,b,c):
#     if a==b==c:
#         print('all numbers or equal')
#     elif a>=b and  b>=c:
#         print(a)
#     elif b>=a and  b>=c:
#         print(b)    
#     else:
#         print(c)   
        
         
# three_num(5,8,3) 
# three_num(-2,-5,-1)  
# three_num(7,7,7)
        
        
#         Question 1: Positive, Negative or Zero

# Write a program that takes a number as input and prints:

# "Positive" if number > 0

# "Negative" if number < 0

# "Zero" if number = 0
# def pos_nav(a):
#     if a>0:
#         print('positive')
#     elif a<0:
#         print('negative')
#     else:
#         print('zero')        
        
# pos_nav(8)
# pos_nav(-8) 
# pos_nav(0)      


# Question 2: Even or Odd

# Write a program that takes a number and prints:

# "Even" if number divisible by 2

# "Odd" if number not divisible by 2


# def even_odd(a):
#     if a%2==0:
#         print('even')
#     else:    
#         print('odd')
        
# even_odd(6)
# even_odd(9)        


# Question 3: Largest of Two Numbers

# Write a program that takes two numbers as input and prints the largest number.

# If both numbers are equal → print "Both numbers are equal"

# def two_input(a,b):
#     if a == b:
#         print('both number are equal')   
#     elif a>=b:
#         print(a)   
#     else:
#         print(b) 
# two_input(5,8) 
# two_input(5,8)  
# two_input(8,8)     

# Question 4: Grade Checker

# Write a program that takes marks (0-100) and prints grade:

# 90 and above → "A"

# 75 to 89 → "B"

# 50 to 74 → "C"

# Below 50 → "Fail"

# def st_mark(a):
#     if a>=90:
#         print('A')
#     elif a>=75 and a<=89:
#         print('B')  
#     elif a>=50 and a<=74:
#         print('c') 
#     else:
#         print('fail')     

# st_mark(78)  
# st_mark(45)  
# st_mark(90)  
# st_mark(74) 


# Question 5: Age Category

# Write a program that takes age as input and prints:

# 0-12 → "Child"

# 13-19 → "Teenager"

# 20-59 → "Adult"

# 60+ → "Senior Citizen"


# def input_child(a):
#     if a>=0 and a<=12:
#         print('child')
#     elif a>=13 and a<=19:
#         print("Teenager")  
#     elif a>=20 and a<=59:
#         print("Adult")      
#     else:
#         print("Senior Citizen")    
        
# input_child(5)  
# input_child(15) 
# input_child(25) 
# input_child(65)            


# Question 1: Leap Year Checker

# Write a program that takes a year as input and prints:

# "Leap Year" if the year is divisible by 4 and (not divisible by 100 or divisible by 400)

# "Not a Leap Year" otherwise

# Example:

# 2020 → Leap Year

# 1900 → Not a Leap Year

# 2000 → Leap Year
    
        
# def leap_year(a):
#     if a%4 ==0 and (a%400 ==0 or a%100!=0):
#         print('leap year')
#     else: 
#         print('not leap year') 
      
# leap_year(2020)
# leap_year(1900)
# leap_year(2000)

# Question 2: Vowel or Consonant

# Write a program that takes a single alphabet as input and prints:

# "Vowel" if the letter is a, e, i, o, u (case insensitive)

# "Consonant" otherwise

def vow_con(a):
    if a=='A' or a=='a':
        print('vowel')
    elif a=='E' or a=='e':
        print('vowel')
    elif a=='I' or a=='i':
        print('vowel') 
    elif a=='O' or a=='o':
        print('vowel')
    elif a=='U' or a=='u':
        print('vowel') 
    else:
        print('consonate')              
        
vow_con('a') 


# Question 3: Triangle Type

# Write a program that takes three sides of a triangle and prints:

# "Equilateral" if all sides are equal

# "Isosceles" if exactly two sides are equal

# "Scalene" if all sides are different

# "Not a triangle" if the sum of any two sides ≤ third side

def triangle_type(a, b, c):
   
    if a + b <= c or b + c <= a or a + c <= b:
        print("Not a triangle")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")


triangle_type(3, 4, 5)  
triangle_type(5, 5, 5)  
triangle_type(5, 5, 8)  
triangle_type(1, 2, 5)  


# Units consumed → calculate bill:

# First 100 units → ₹5/unit

# Next 100 units (101–200) → ₹7/unit

# Above 200 units → ₹10/unit

def unit_abo(n):
    if n<=100:
        print(n*5)
    elif n>=100 and n<=200:
        print((100 * 5) + (n - 100) * 7  )
    else:
        print (100 * 5 + 100 * 7 + (n - 200) * 10) 
        
        
unit_abo(87)    
unit_abo(117) 
unit_abo(250) 

  

    