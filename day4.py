

#normal copy (*****)


#String basic:
#Immutable data type


#Indexing: extracting single single character
#syntax: varname[position]

#slicing: extracting multiple character
#Syntax: varname[start:end+1:stepvalue]

'''
x='Ahambdabad'
print(x[5])

print(x[::-1])
print(x[0:5:2])
print(x[-1:-6:-1])
print(x[3:8:1])

print(x[1:])

'''
#o/p:

'''
d
dabadbmahA
Aab
dabad
mbdab
hambdabad
'''



#format() and f-string()
item,qty, price="pen",3,12.5

print("{}*{} ={}".format(item,qty,qty*price))
print("{0}-{1}-{0}".format("a","b"))
print(f"{item:<6}|{qty:^5}|{price:>8.2f}")

total=1234567.891
print(f"Total :{total:,.2f}")
print(f"{42}000 {0.256:.1%}")
print(f"{'left':<8} | {'right':>8}|")
print("A","B","C",sep="-",end="!\n")
#a-b-a
print("{n} is{a}".format(n="Ravi",a=21))


#op
'''
pen*3 =37.5
a-b-a
pen   |  3  |   12.50
Total :1,234,567.89
00042 25.6%
left     |    right|
A-B-C!
Ravi is21
'''
