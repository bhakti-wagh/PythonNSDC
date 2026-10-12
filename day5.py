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
      
'''

'''
text="Your time is limited , So don't waste it leaving someonelse's life"
clean= text.strip().lower()

vowels=(clean.count("a")+clean.count("e")+clean.count("i")+clean.count("o")+clean.count("u"))
#23

words=clean.split()

print("Words:",len(words))
print("Vowels:",vowels)
print("longest word:",max(words,key=len))
print("Title case", clean.title())
print("snake case:",clean.replace(" ","_"))
print("Starts with 'the':",clean.startswith("the"))
'''

#o/p:
'''
Words: 12
Vowels: 23
longest word: someonelse's
Title case Your Time Is Limited , So Don'T Waste It Leaving Someonelse'S Life
snake case: your_time_is_limited_,_so_don't_waste_it_leaving_someonelse's_life
Starts with 'the': False
'''


#Loops:

#for:-> repeats once for each item of sequence
#while:-> repeats as long as the condition is True
'''
total=0
for n in range(1,10):
    total+=n
print(total)

count=0
while count<5:
    print("count is",count)
    count+=1
'''
#o/p
'''
45
count is 0
count is 1
count is 2
count is 3
count is 4'''


print(list(range(5)),list(range(2,10,3)),list(range(5,0,-2)))

for i in range(10):
    if i==3:
        continue

    if i==6:
        break
    print(i,end=" ")
print()

#o/p
'''
[0, 1, 2, 3, 4] [2, 5, 8] [5, 3, 1]
0 1 2 4 5 '''
