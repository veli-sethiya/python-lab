import math
def area (a,b,c):
    s=(a+b+c)/2
    ar=math.sqrt(s*(s-a)*(s-b)*s-c)
    print("area triangle=",ar)
area(4,3,2)


def li_as_arg(li):
    for i in li:
        print(i)

list=[1,2,3,4,7,5,6]
li_as_arg(list) #passing list as an argument

def fact(n): #recursion function
    if(n==1):
        return n
    else:
        return (n*fact(n-1))

n=5
print("factorial of {0} is {1}".format(n,fact(n)))

x = "good" # here x is global variable
def myfunc():
  x = "fantastic" # here x is local variable
  print("x with value {0} is local here ".format(x))

myfunc()
print("x with value {0} is global ".format(x))

x = "veli" # here x is global variable
def myfunc():
    global x   #making x global
    x = "Veli Sethiya" # here x is local variable
    print("x with value {0} is also accessing global variable here ".format(x))

myfunc()
print("x with value {0} is global ".format(x))
