x=int(input("enter price : ")) # this is input command
print("x is ",x)  #this is simple output command

print("The price is {} dollars".format(x)) # this is format command

print("The price is {:.2f} dollars in two places of decimal".format(x))

y=x*70
print("The price is {0} dollars or {1} rupee".format(x,y))# format with indexing

string = "welcome-to-the jungle" #split function
print(string.split("-")) #having "-" than split

print(string.split("-",1)) # split in two elements