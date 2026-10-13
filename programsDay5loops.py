#sum of prime numbers in a range
'''
sump=0
total=0
for i in range(10,100):
    count=0

    for j in range(1,i+1):
        

        if i%j==0:
            count+=1      

    if count==2:
        print(i,end=" ")
        sump+=i
        total+=1

print()
print(f"Totla prime number:{total}")
print(f"Sum :{sump}")
'''

#o/p
'''
11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
Totla prime number:21
Sum :1043
'''

#find the second largest unique number
'''
numbers=[45, 12, 89, 34, 89, 67, 23, 67]
large=numbers[0]
small=numbers[0]

for i in numbers:
    if i>large:
        small=large
        large=i

    elif i>small or i!=large:
        small=i

print(f"Largest number:{large}")
print(f"Second largest number:{small}")

'''
#o/p
'''
Largest number:89
Second largest number:67
'''


#Number pattern with nested for loop
'''
n=5

for i in range(1,6,1):
    for j in range(1,i+1):

        i-=1
        print(j,end=" ")

    print()
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")

    print()
        
'''
#o/p:
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''


#Student marks analysis
'''
marks=[78, 45, 92, 33, 67, 88, 29, 56]

high=marks[0]
low=marks[0]
passt=0
fail=0
total=0
avg=0

for i in marks:
    
    total+=i
    
    if i>=40:
        passt+=1

    else:
        fail+=1

    avg=total/len(marks)

    if i>high:
    
        high=i
    if i<low :
        low=i

print(f"Passes Student:{passt}")
print(f"Fail Student:{fail}")
print(f"Highest marks:{high}")
print(f"Lowest marks:{low}")
print(f"Avgerage marks:{avg}")
 '''           

#o/p:

'''
Passes Student:6
Fail Student:2
Highest marks:92
Lowest marks:29
Avgerage marks:61.0'''

#function with for loop- armstrong number
'''
def is_armstrong(number):

    total=0
    num=str(number)

    power=len(num)

    for i in num:
        total=total+int(i)**power
        

    if total==number:
        return True
    else:
        return False
    
print("Armstrong numbers:")

for n in range(100,999):
    if is_armstrong(n):
        print(n,end=" ")
'''
#o/p:
'''
Armstrong numbers:
153 370 371 407'''


#Section B While loop

#reverse a number and check palindrome

'''
num=12321
number=num

rev=0

while num>0:

    temp= num%10
    rev = rev*10+temp
    num=num//10

if rev==number:
    print("Palindrome :Yes")
print(f"Originl number:{number}")

print(f"Reversed number:{rev}")
    
'''

#o/p:
'''
Palindrome :Yes
Originl number:12321
Reversed number:12321
'''


#sum of digits unitl a single digit

'''
number = 9875
print("Original Number:", number)

step = 1

while number >= 10:
    total = 0
    temp = number

    while temp > 0:
        digit = temp % 10
        total += digit
        temp = temp // 10

    number = total
    print(f"Step {step}: {number}")
    step += 1

print("Final Single Digit:", number)
'''
#o/p:
'''
Original Number: 9875
Step 1: 29
Step 2: 11
Step 3: 2
Final Single Digit: 2
'''


#Fibonacci series with while loop
'''
num=100
a=0
b=1
count=0

while  a<=num:
    print(a,end=" ")
    
    c=a+b
    a=b
    b=c

    count+=1

print()

print(f"Total Tersms:{count}")
'''
#o/p:
'''
0 1 1 2 3 5 8 13 21 34 55 89 
Total Tersms:12'''


#Atm withdrawl simulation
'''
bal=10000

choice=eval(input("Enter choice:"))

while choice!=0:

    if choice==1:
        print(f"Total balance:{bal}")
        break
    elif choice==2:
        Amt=eval(input("Enter amount:"))
        bal= bal+Amt
        print(f"Total balance:{bal}")
        break
    elif choice==3:
        WithAmt=eval(input("Enter amount for withdrawl:"))

        if WithAmt>bal:
            print("Insufficient balance")

        else:
            bal-=WithAmt
            print("Withdrawl Successful!")
            print(f"Remaining Balance :{bal}")
        break

    elif choice==4:
        print("Thank you for using ATM!")
        break

    else:
        print("Enter valid choice")

'''
#o/p:
'''
Enter choice:3
Enter amount for withdrawl:500
Withdrawl Successful!
Remaining Balance :9500

Enter choice:4
Thank you for using ATM!

'''

#Function with while loop-> decimal to binary converter


def decimal_to_binary(number):

    
    decimal=0

    i=0

    while number>0:
        rem=number%2
        number=number+rem*2(2**i)
        binary=binary//2

        i+=1


    print(f"decimal :{decimal}")

decimal_to_binary(25)
