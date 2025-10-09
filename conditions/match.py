
t=input("enter the trafic light")
match t:
    case "RED":
        print("STOP")
    case "YELLOW":
        print("READY") 
    case "GREEN":
        print("GO") 
    case _:
        print("invalid statement")   


# Given a character check if its a vowel or not using match case.
def get_vowel_consonant (a):
    match a:
        case "A"|"a":
            print("vowel")
        case "E"|"e":
            print("vowel")    
        case "I"|"i":
            print("vowel")    
        case "O"|"o":
            print("Vowel")   
        case "U"|"u":
            print("vowel")   
        case _:
            print("not a vowel")      

get_vowel_consonant ("a")
get_vowel_consonant ("U")
get_vowel_consonant ("i")



# Write a program has a single variable, age, which is a number.
# The function should print the price of a movie ticket based on the following rules:
# If the age is less than 5, the ticket is free (print "Free").
# If the age is between 5 and 12, the ticket price is $10 (print "10").
# If the age is between 13 and 64, the ticket price is $20 (print "20").
# If the age is 65 or older, the ticket price is $15 (print"15").
age=int(input("your age is:"))
if age<=5:
    print("ticket is free")
elif age >5 and age<=12:
    print("ticket price is 10 ")
elif age>13 and age<64:
    print("ticket price is 20")    
elif age>=65:
    print("ticket price is 15")    
    
    



#  Create a program that has an integer monthNumber as a variable, where monthNumber ranges from 1 to 12. 
# The function should return the name of the corresponding month (e.g., 1 for "January", 2 for "February", etc.). 
# If the monthNumber is not between 1 and 12, return "Invalid month number". Use a match statement to implement this program.   
def get_month_name(monthNumber):
    match monthNumber:
        case 1:
            print("January")
        case 2:
            print("February")
        case 3:
            print("March")
        case 4:
            print("April")
        case 5:
            print("May")
        case 6:
            print("June")
        case 7:
            print("July")
        case 8:
            print("August")
        case 9:
            print("September")
        case 10:
            print("October")
        case 11:
            print("November")
        case 12:
            print("December")
        case _:
            print("Invalid month number")



# get_month_name(5)
t=int(input("enter tara number:"))
j=int(input("enter jyothi number"))
a = t+j
if a % 5 == 0 :
   print(1)
else:
    print(0)