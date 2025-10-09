
# Input: number 1–7

# Output: day name
def dat_day(a):
    match a:
        case  1:
            print('sunday')
        case  2:
            print('monday')    
        case _:
            print('invalid_input')    
dat_day(2)            



# Question 2: Simple Calculator

# Take two numbers and an operator as input (+, -, *, /)

# Use match-case to perform the operation and print the result

def match_py(a,b, op):
    match op:
        case '+':
            print(a+b)
        case '-':
            print(a-b) 
        case _:
            print('invalid input')  
            
match_py(5,10 ,'+')                 
match_py(10,15,'-')                 