'''
#Leap year or not
year=int(input("Enter a year:"))

if year%4==0:
    print(f"Leap year :{year}")

elif year%400==0:
    print(f"Leap year:{year}")

elif year%100==0:
    print(f"not leap year:{year}")

else:
    print(f"not leap year{year}")


#O/P:
Enter a year:2004
Leap year :2004'''

'''
a,b,c=7,7,10

if a+b<=c or a+c<=b or b+c<=a:
    kind="not a trianlge"

elif a==b==c:
    kind="equilateral"
    
elif a==b or b==c or a==c:
    kind="isosceles"
else:
    kind="Scalene"

print(kind)

#o/p: isosceles
'''

'''
bal,amt=650,650

if amt<=0:
    msg="Invalid amount"

elif amt>bal:
    msg="Insufficient funds"

elif amt%100!=0:
    msg ="Enter multiples of 100"

else:
    bal-=amt
    msg=f"Collect cash.Balance{bal}"
print(msg)

'''


'''
amt=eval(input("Enter amount:"))

def withdraw(amt):
    bal=10000

    if amt<=0:
        msg="Invalid amount"

    elif amt>bal:
        msg="Insufficient funds"
    else:
        bal-=amt
        msg=f"Collect cash.TotalBalance: {bal}"

    return msg

print(withdraw(amt))

#o/p:
#Enter amount:200
#Collect cash.Balance9800
'''
'''
x=5

if x>4:
    print("c")
elif x>3:
    print("D")
if x>3:
    print("B")
'''


if 0.1+0.2==0.3:
    print("Equal")
else:
    print("not equal")

if "0":
    print("non-empty string is True")

if []:
    print("Never printed")

print(bool([]),bool([0]),bool(None))
      
