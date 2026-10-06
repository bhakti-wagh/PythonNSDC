#Type conversion(Casting):->

#Convert one data type into another type of data

'''
print(int("10")) #str-> int 10
print(str(20)) # int-> str "20"
print(int(3.9)) #float-> int 3
print(float("3.5")) #str->float 3.5
print(list("abc")) # str->list ['a','b','c']
print(bool("hello")) #str->bool True


#input() :-> by default always return str

name=(input("Enter your name:"))
age=int(input("Enter your age:"))
price=float(input("Enter price:"))

print(f"name:{name}, age:{age}, price:{price}")

'''


#lab1 :-> Guess data type
print(type(100)) #<class,'int'>
print(type(-3.5)) #<class,'Float'>
print(type("100")) #<class,'str'>
print(type(True)) #<class,'bool'>
print(type(10/5)) #<class,'float'>
print(type(10//5)) #<class,'int'>
print(type("a"*2))#<class,'str'>
print(type(1>0))#<class,'bool'>


#lab2:-> temperature convertor
c=float(input("celsius:"))#20.5
f=(c*9/5)+32
k=c+273.15
print("Fahrenheit:",f)#68.9
print("Kelvin:",k)#293.5
print(type(f))#float


#lab3:->
print(int("25")+5)#30
print(int(float("12.5")))#12
print("age:"+str(20))#age:12
#print("Age:"+20) #concate only str
