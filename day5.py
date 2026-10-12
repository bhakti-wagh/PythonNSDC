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


a,b,c=20,30,65

if a+b<=c or a+c<=b or b+c<=a:
    kind="not a trianlge"

elif a==b==c:
    kind="equilateral"
elif a==b or b==c or a==c:
    kind="isosceles"
else:
    kind="Scalene"

print(kind)
