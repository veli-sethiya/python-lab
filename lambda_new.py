#multiplication using lambda

y= (lambda a,b:a*b)(4,2)
print(y)

#function to find  cube  of a number
x=(lambda a:a*a*a)(2)
print(x)

#add 2 list
x=[90,80,70,60,50]
y=[50,60,70,80,90]
z=list(map(lambda a,b:a+b,x,y))
print(z)

#use of lamda function

list_1 = [1,2,3,4,5]

filter( lambda x: x%2==0 , list_1 )
print( list( filter( lambda x: x%2==0 , list_1 )))

# Use with map()

list1 = [1, 3, 5, 7, 9]
list2 = list(map(lambda x: x * 2 , list1))
print(list2)

# Use with reduce

from functools import reduce
li = [1, 2, 3, 4, 5, 6]
sum = reduce((lambda x, y: x + y), li)
print (sum)

#print table of 5 using lambda functions
            
table=[lambda j=x:6*j for x in range(1,11)]

#print(table)

for i in table:
    print(i())

#find smallest number

Min = lambda a,b: y if (a > b) else a
print("Minimum number is - ",Min(10,33))    


