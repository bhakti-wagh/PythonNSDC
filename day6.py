#Function:-> function is set of stmt or block of code that executes when we call the function
#Function:-> help for write once , use many times
#Syntax:

'''
def function(parameter):

    //Block of code
    return

print(function(argument))

'''

'''
pass1="bhakti123"


def checkPass(pass1):

    attemt=3

    for i  in range(attemt):
        password=eval(input("Enter password"))

        if password==pass1:
            print("verfied password")
            break

        else:
            attemt_left = attemt-i-1

            print(f"remaing attemts{attemt_left}")

            if attemt<0:
                print(f"no attemt left")

checkPass(pass1)


'''
#o/p:
'''
Enter password1234
remaing attemts2
Enter password524
remaing attemts1
Enter password122
remaing attemts0'''
        

'''
def min_max(nums):
    return min(nums),max(nums)

lo,hi=min_max([4,9,1,7])
print(lo,hi,type(min_max([1])).__name__)

def early(n):
    if n<0:
        return "negative"

    return "non-negative"

print(early(-1),early(5))
'''

#o/p:
'''
1 9 tuple
negative non-negative'''


'''

def order(item,qty=1,express=False):
    kind="express" if express else "normal"

    return f"{qty}*{item}({kind})"


print(order("Bat"))
print(order("Bat",5,True))
print(order("bottle",express=True))
'''

#o/p:
'''
1*Bat(normal)
5*Bat(express)
1*bottle(express)

'''

'''
square=lambda x:x**2
print(square(6)) #36

words=["pear","fig","banana"]

print(sorted(words,key=lambda w:len(w))) #['fig', 'pear', 'banana']
print(list(map(lambda n:n*2,[1,2,3])))#[2, 4, 6]

print(list(filter(lambda n:n%2==0,range(7))))#[0, 2, 4, 6]

def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)

print(factorial(5))#120
'''
#o/p:
'''
36
['fig', 'pear', 'banana']
[2, 4, 6]
[0, 2, 4, 6]
120'''

'''
x="Hello world"
count=0
i=len(x)-1

while i >= 0 and x[i] == ' ':
             i -= 1



while i<=0 and x[i] !=' ':
    count+=1
    i-=1
    
'''
s



    
    


