#Operator
#:-> A symbol that use to perform task (+,-,*,/)

#Operand
#:-> a value that operator works on

#Unary :-> uses one operand
#Binary:-> uses two operand



#Arithmetic operator:-> +,-,*,/,//,%
#unary:-> +x,-x
#assignment:-> =,+=,-=,/=,%=,//%,**==
#comparison:-> ==,!=,>,<,>=,<=
#Logical:-> and , or , not
#identify:-> is , is not  # same object in memory
#Containment:-> in , not in  #is value inside a sequence




'''
#Last digit :-> n%10
#Remove last digit:-> n//10

n=24
print(n%2==0)#True
print(n%3==0)#False
print(n%7) #3
print(n//7)#3

hours=5
print(hours%24)#5


print()
x=153
print(x%10) #3
print(x//10)#15
'''
'''
x=20
print(-x) #-20
print(+x) #20
print(-(-x)) #20
print(-x**2) #-400
print(10- -2) #12

y=-4
print(abs(y),-y)# 4 4

'''


'''
a=75
b=50
print(a==b, a!=b) #False True
print(a>b, a<b) #True False
print(a>=10, b<=4) #True False
print(1<b<10) #False
print(7==7.0)#True
print(7=="7") #False

print("apple"<"banana") #true
print("a" == "A") #False
'''


#short
'''
print(1 and 3)#3
print(5 and 8)#8
print("" or "guest")#guest
print(4 or 1/0) #4
print(0 and 1/0)#0
print(not 0 , not "hi") #True False
name=""
print(name or "Unknown") #Unknown)
'''


#Lab1
'''
print(16+4*2) #24
print((16+4)*2)#40
print(16/4)#4.0
print(16//4)#4
print(16%4)#0
print(2**5)#32
print(-16//4)#-4
print(16.0//4)#4.0
print(25/5)#5.0
print(7+3*2**2-1)#18
'''


#simple calculator

a=float(input("Enter number:"))
b=float(input("Enter number:"))
print("Add:",a+b)
print("sub:",a-b)
print("mul:",a*b)
print("divide:",a/b)
print("Floor div:",a//b)
print("rem:",a%b)
print("power:",a**b)

#o/p:
'''
Enter number:20
Enter number:5
Add: 25.0
sub: 15.0
mul: 100.0
divide: 4.0
Floor div: 4.0
rem: 0.0
power: 3200000.0

'''
