import random

#Real-world :
#quize,selecting random numbers

print("Random integer:",random.randint(1,10))
print("Random decimal:",random.random())

students=["Aman","Riya","Rahul","Priya","Karan"]

print("Selected student:",random.choice(students))

random.shuffle(students)
print("shuffled list:",students)

selected_students=random.sample(students,2)
print("Two selected students:",selected_students)



#o/p:
'''Random integer: 8
Random decimal: 0.4164455682161017
Selected student: Aman
shuffled list: ['Rahul', 'Aman', 'Riya', 'Priya', 'Karan']
Two selected students: ['Rahul', 'Karan']'''