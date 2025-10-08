
x=int(input())
y=int(input())

if x>0 and y>0:
    print("quadrant 1")
elif x<0 and y>0:
    print("quadrant 2")  
elif x<0 and y<0:
    print("quadrant 3")  
elif x>0 and y<0:
    print("quadrant 4") 
else:
    print("pointed exited 0,0")           