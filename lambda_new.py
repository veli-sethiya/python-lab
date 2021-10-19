from functools import reduce
list1=[2,3,4,5,6]
list2=[4,5,6,7,8]
print(list(map (lambda x,y:x+y,list1,list2)))

list2=[4,5,6,7,8,6]
print(list(map (lambda x,y:x+y,list1,list2)))

l=['12345','veli','avni']
print(list(map(list,l)))

sq=lambda y:y**2
sq(3)

sq(30)

table=[lambda x=x: x*2 for x in range(1,11)]
for i in table:
	print(i())

list(table)

sum=reduce(lambda x,y:x+y,list1)
print( sum)

max=reduce (lambda x,y: x if x>y else y,list1)
print(max)
print("veli".upper())

def func1(x):
  return x+5

print(func1(5))

print(list(map(lambda x:pow(x,3), list1)))

str1= ['dog', 'cat']
print(list(map(lambda x: x.upper(), str1)))

age=[5,6,7,8,9,10,11]
print(list(filter(lambda x: x<10, age)))

mylist = map(lambda x : x*2, [x for x in range(1,11)])
print(list(mylist))
