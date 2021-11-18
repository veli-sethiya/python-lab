#Program to find digital sum of a given Number ex: n=123 Digital sum----->1+2+3=6

n = int(input())
sum = 0
while n>0 :
  sum = sum + n%10
  n= n//10
print("Digital sum of given number is ",sum)


#Program to find the digital product of a given number ex: n=43 Digital product ----->4*3=12

n = int(input())
p = 1
while n>0 :
  p = p * (n%10)
  n= n//10
print("Digital product of given number is ",p)


#Find the sum of the series 3 +33 + 333 + 3333 + .. n terms

n=int(input("Enter the range of number:"))
sum=0
p=3
for i in range(0,n):
    sum += p
    p=(p*10)+3
print("The sum of the series = ",sum)
Enter the range of number:4
The sum of the series =  3702
Print the following pattern
for i in range(1,6):
  for j in range (i):
    print("* ",end="")
  print()
rows = 4
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end='')
    print()
 
#Program to reverse a given Number. ex: n=123 Reversed no is 321

n = int(input())
rev = 0
while n>0 :
  rev = rev*10 + n%10
  n= n//10
print("Reversed number is ",rev)

#23.Program to check whether a given number is a palindrome or not

n = int(input())
c = n
rev = 0
while n>0 :
  rev = rev*10 + n%10
  n= n//10
if c==rev:
  print(c," number is palindrome.")
else:
  print(c," number i not palindrome.")
101
101  number is palindrome.
Program to check whether a given number is an Armstrong number or not.
num = int(input("Enter any number: "))
temp = num
l = len(str(num))
sum = 0
while temp > 0:
   sum = sum + (temp % 10) ** l
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#Program to find factorial of a given number.

n = int(input(" Enter a number "))
fact = 1
for i in range(1,n+1):
  fact = fact * i
print("Factorial of ",n ," is ", fact)

#Program to find whether a given number is a strong number or not. e.g. n=145 1!+4!+5!==145

def factn(x):
  fact = 1
  for i in range(1,x+1):
    fact = fact * i
  return fact
n = int(input(" Enter a number "))
c = n 
sum = 0
while n>0 :
  sum = sum + factn(n%10)
  n= n//10
if sum == c:
  print(c," is strong number.")
else:
  print(c," is not a strong number.")

#Program to find whether a given number is a unique number. For example, 20, 56, 9863, 145, etc. are the unique numbers while 33, 121, 900, 1010, etc. are not unique numbers

n = list(map(int, input('Enter a number:').split()))
n1 = []
for i in n:
  if i not in n1:
    n1.append(i)
if len(n) == len(n1):
  print("Number is a unique number. ")
else:
  print("Number is not a unique number")

#Program to find whether a given number is a perfect number or not.

n = int(input("Enter any number "))
sum = 0
for i in range(1, n):
    if(n % i == 0):
        sum = sum + i
if (sum == n):
    print(n," is a Perfect number")
else:
    print(n," is not a Perfect number")

#Program to find whether a given number is a prime number or not.

num = int(input("Enter any number: "))
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num," is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

#Print downward Half-Pyramid Pattern with Star (asterisk)

rows = 5
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end='')
    print()
 
#Print following pattern: 1 22 333 4444 55555 666666 7777777 88888888 999999999

for i in range(1,10):
  for j in range (i):
    print(i ,end="")
  print()

#Print following pattern: 1 12 123 1234 12345 123456 1234567 12345678 123456789

for i in range(1,10):
  for j in range (1,i+1):
    print(j ,end="")
  print()

#Print following pattern: A BB CCC DDDD EEEEE FFFFFF GGGGGGG FFFFFFFF

alp = 65
for i in range(1,9):
  for j in range (i):
    print("%c" %(alp), end="")
  alp += 1
  print()
