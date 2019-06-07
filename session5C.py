######################STRING FORMATTING#################################3

name = "Fionna"
age = 30

print("Welcome to our club %s"%(name))
print("Your age is %d"%(age))
print("Hey, %s you are %d years old"%(name, age))
print("Hey, {} you are {} years old".format(name, age))

#ADVANCED WAY OF FORMATTING

print(f"Hey, {name} You are {age} years old")



for i in range(1,11):
    print(" 2 X {} = ".format(i), 2*i)