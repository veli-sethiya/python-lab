#8 Given two integer numbers return their sum. If the sum is greater than 100, then return their product.
x, y  = map (int , input().split())
sum = x+y
print(sum)

if sum>100:
    print("The sum of the numbers is greater than 100 so the product of the numbers is : ", x*y)
    
    
#9 Write a Python program to calculate the sum of three given numbers, if the values are not - equal then return four times of their sum.
x, y, z = map(int, input().split())
Sum  = x+y+z

if x == y == z:
    print("All the values are equal")
    print("Sum = ",Sum)
else:
    print("All the values are not equal")
    print("Sum = ",4*Sum)

    
#10 A shop will give discount of 50% if the cost of purchased quantity is more than 10000. Ask user for quantity suppose, one unit will cost 100. Judge and print total cost for user.
x = int(input("Enter quantity to be purchased:"))
cost = x*100

if cost > 10000:
    cost/=2
    print("Cost = ",cost ) 
else:
    print("Cost = ", cost)

    
#11 To check whether a number is divisible by 8 and 12 or not.
x = int(input("Enter a number: "))

if x%8==0 & x%12==0:
    print("Yes, The number is divisible by 8 & 12")
else:
    print("No, The number is not divisible by 8 & 12")

    
#12 To check whether a given number is even or odd.
x = int(input("Enter a number: "))

if x%2==0:
    print("The number is even")
else:    
    print("The number is odd")

    
'''13 Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% :  Grade F '''
'''13 Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% :  Grade F '''

print("Enter the marks of the following Subjects")
Phy = int(input("Physics = "))
Che = int(input("Chemistry = "))
Bio = int(input("Biology = "))
Math = int(input("Mathematics = "))
Comp = int(input("Computer = "))

Per = (Phy+Che+Bio+Math+Comp)/5

print('Percentage is: ',Per)
if Per>=90:
    print('Grade A')
elif Per>=80:
    print('Grade B')
elif Per>=70:
    print('Grade C')
elif Per>=60:
    print('Grade D')
elif Per>=40:
    print('Grade E')
else:
    print('Grade F')

    
#14 Take input of age of 3 people by user and determine oldest and youngest among them.
a,b,c = map(int, input().split())
if a>b and a>c:
    print('Person first is oldest')
elif b>a and b>c:
    print('Person second is oldest')
else:
    print('Person third is oldest')
if a<b and a<c:
    print('Person first is youngest')
elif b<a and b<c:
    print('Person second is youngest')
else:
    print('Person third is youngest')

    
#15 Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

x = int(input("Enter Units of electricity: "))
cost = 0
if x - 50 > 0:
    cost = 50*(.50)
    if x - 150 > 0:
        cost = cost + 75
        if x - 250 > 0:
            cost = cost + 120 + (x-250)*1.50
        else:
            cost = cost + (x-150)*1.20
    else:
        cost = cost + (x-50)*.75
else:
    cost = x*(0.50)
cost = cost + cost/5
print("You have to Pay total amount of Rs.", cost)


#16 A student will not be allowed to sit in exam if his/her attendence is less than 80%.
#Take following input from user
#Total Number of classes held
#Total Number of classes attended. And print percentage of class attended. Is student is allowed to sit in exam or not.
Class_held = int(input("Enter the total no of class held :"))
Class_attended = int(input("Enter the no of class attended : "))

attendance = (Class_attended/Class_held)*100
print("Youe attendance is :", attendance ,"%")

if attendance < 80:
    print("Sorry, You are not allowed to sit in exam.")
else:
    print("Congrats, You are allowed to sit in exam.")

    
#17 Calculate income tax for the given income by adhering to the below rules
#Taxable Income        Rate (in %)
#First Rs.10,0000         0
#Next Rs. 10,0000       10
#The remaining           20

income = int(input("Enter your income: "))
tax= 0
print("Given income", income)

if income <= 10000:
    tax = 0
elif income <= 20000:
    x = income - 10000
    tax = x * 10 / 100
else:
    tax = 10000 * 10 / 100
    tax += (income - 20000) * 20 / 100

print("Total tax to pay is", tax)
