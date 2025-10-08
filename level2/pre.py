
# num=int(input('enter'))
# a=num//1000 *5
# b=num//5000 *20
# total=a+b
# if num>=1000:
#     print(total)
# else:
#     print(num)
    
    
    
num = int(input("Enter a number: "))
count = 0
a=1
while num > a:
    count += 1
    # num //= 10
    a=a+1

print("Number of digits:", count)
