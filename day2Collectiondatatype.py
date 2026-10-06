#List_tuple

mixed=[1,"Hello",3.14,True]
mixed.append("New")
print(mixed)

t=(10,50,60)
print(t[1])#50
single=(42,)
print(t[0])#10
#t[0]=5 #assing operator we can't use into tuple
print(t)


#Set_dict
u={1,2,3,4,3,4,2}

print(u)#{1,2,3,4}

st={"name":"bhakti","age":22}
print(st["name"])#bhakti
print(st.get("rollno","rollno not found")) #rollno not found
print(type(st))#<class,"dict">
