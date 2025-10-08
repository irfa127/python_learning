# Question 1:
# A cinema charges:
# * ₹150 for ages under 18
# * ₹250 for ages 18–60
# * ₹100 for ages above 60
# Write a program that asks for age and prints the ticket price.
# Sample Input:
# 65
# Sample Output:
# 100

# a=int(input('enter your age'))
# if a<=18:
#     print(150)
# elif a>=18 and a<=60:
#     print(250)
# else:
#     print(100)    
    
        
# Question 2:
# A stadium sells entry passes with the following rules:
# * If age < 12 → Ticket = ₹50
# * If age between 12–59 → Ticket = ₹120
# * If age ≥ 60 → Ticket = ₹80
# Additionally, if the person’s age is a Even number, give a ₹5 discount.
# Get the input from the user and return the final discounted stadium ticket price.
# Sample Input:
# 59
# Sample Output:
# 120

# age = int(input('enter your age:'))
# if age <= 12:
#     price = 50
# elif age >= 12 and age <= 59:
#     price = 120
# else:
#     price = 80

# if age % 2 == 0:
#     price = price - 5

# print(price)
   



    
# # Question 3:
# # A shopkeeper has n mangoes.
# # He wants to pack them into baskets, with 5 mangoes in each basket.
# # Write a program to calculate:
# # * How many full baskets can be made
# # * How many mangoes will be left
# # Sample Input:
# # 23
# # Sample Output:
# # Full Basket is 4
# # Left Over mangoes is 3

# m = int(input('enter your total mangoes: '))
# full = m // 5
# left = m % 5
# print(full)
# print(left)



# # Question 4:
# # A child has n candies and eats one candy each day until all are finished.
# # Write Python program to print how many candies the child ate and how many are left each day.
# # Sample Input:
# # 3
# # Sample Output:
# # Day 1 = 2 left
# # Day 2 = 1 left
# # Day 3 = 0 left


# n=int(input('enter'))
# for i in range(1,n):
#     print(n-i)

# n=int(input('enter how many candies the chid are eating'))
# a=n // 1
# b=n%1
# print(a)
# print(b)
# # Question 5:
# # An employee gets a monthly salary.
# # * If sales ≥ 100 units → bonus = 10%
# # * 50–99 units → bonus = 5%
# # * <50 → no bonus
# # Write a program that asks for salary and sales and prints total salary including bonus.
# # Sample Input:
# # Enter your salary 40000
# # Enter your sales 120
# # Sample Output:
# # Bonus = 4000
# # Total Salary = 44000
# salary=int(input('enter'))
# sales=int(input('rfg'))
# if sales>=100:
#     c=salary * 10
#     print(c)
# elif sales>=50 and salary<=99:
#       d=salary *5
#       print(d)
# else:
#     print('no bonus')      
      

# Question 6:
# Earnings of a Salesperson:
# * 5% commission for sales ≤ ₹5000
# * 10% for sales 5001–10000
# * 15% for sales > 10000
# Input weekly sales of the salesperson and calculate commission.
# Test Cases with their output:
# 7000 -> 700
# 12000 -> 1800
# 11000 -> 1650
# s=int(input('enter the'))
# a=5/100
# b=10/100
# c=15/100
# d=s*a
# e=s*b
# f=s*c
# if s<=5000:
#     print(d)
# elif s>=5001 and s<10000:
#     print(e) 
# elif s>=10000:
#     print(f)       

# Question 7:
# Multi-Item Shopping Discount
# * Price > 100 → 10% discount
# * Price 50–100 → 5% discount
# * Price <50 → no discount
# Print discounted price per item
# Test cases with their output:
# 200 → 180
# 80 → 76
# 40 → 40
# 150 → 135

# price=int(input('enter'))
# if price>=100:
#    a=price -(price/10)
#    print(a)
# elif price>=50 and price<100:
#     b=price-(price/5)
#     print(b)   
# else:
#     print('no discount')    
# A file manager needs to classify files based on their extension.
# .csv  → print output as "This is an Excel File"
# .jpg  → print output as "This is a JPEG File"
# .doc  → print output as "This is a Word File"
# .pdf → print output as "This is a PDF File"
# .py → print output as "This is a Python File"
# .Any other input, print output as "Unknown File Type"
# Print the result based on the input
# Sample Input:
# .csv
# Sample Output:
# This is an Excel file
# Sample input:
# .py
# Sample Output:
# This is a Python File

# file=input('enter your file type')
# if file =='.csv':
#     print("This is an Excel File")
# elif file ==  '.jpg':
#     print("This is a JPEG File")  
# elif file == '.doc ':
#     print("This is a Word File")   
# elif file == '.py ' :
#     print("This is a Python File")  
# else:  
#     print("Unknown File Type")   
# Question 9:
# Taxi charges:
# * First 10 km → ₹15/km
# * Next 20 km → ₹12/km
# * Beyond 30 km → ₹10/km
# Estimate the Taxi charges based on the input and print the output.
# Sample Input:
# 15  → 180
# 35 → 350
# 10 → 150
    
      
    
# a=int(input('enter idly'))
# b=a*15
# b=a*12
# c=a*104
# if a<=10:
#     print(a)
# elif a>10 and a<=20:
#     print(b)  
# else:
#     print(c)      
  
    
# Question 10:
# Lily is N years old.
# On every odd birthday (1, 3, 5, …) → she gets 1 toy.
# On every even birthday (2, 4, 6, …) → she gets money.
# The money starts at ₹10 on her 2nd birthday.
# On each next even birthday, it increases by ₹10 more:
# 2nd birthday → ₹10
# 4th birthday → ₹20
# 6th birthday → ₹30
# and so on.
# At the end, print the following:
# * Number of toys Lily has.
# * Total money she has (money from even birthdays after brother takes ₹1).
# Input
# * Lily’s age (N)
# * Nothing else (price of toys is not needed because we are not selling)
# Output
# * Number of toys
# * Total money (formatted with 2 decimal places)
# Sample TestCase:
# Input
# 10
# Output
# 5
# 150.00
# Explanation:
# Toys → 1,3,5,7,9 → 5 toys.
# Money → 10 + 20 + 30 + 40 + 50 = ₹150. 


n =int(input("enter the value"))
count = 0
toy = 0
for i in range (1,n+1):
    if i % 2 == 0:
        count = count + 10 * (i // 2)
        print(count)
    else:
        toy = toy + 1
print(toy)

        

