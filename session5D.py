############ BUILT-INs ON STRING ###########################

#STRINGS ARE IMMUTABLE
name = " rahul sharma"
name.upper() #output will be same
newName= name.upper() # now it will be changed
print(newName)

anotherName = "chetan Pant"
anotherName=anotherName.capitalize()
print(anotherName)

names= "John, jenny, jim, jack, joe, John, JOHN"
idx = names.index("h")
idx = names.index("jenny")
print(idx)

newName=names.replace('J','K')
print(name)
print(newName)

num = names.count("John", 0, len(names))
print(num)

data=names.split(",")
print(data, type(data))

print()
for n in data:
    print(n.strip())

quote = "Search the candle you want to search cursing the darkness"
data=quote.split(" ")
print(data, len(data))
print(len(quote))
##########################################CONCATENATION################################3

salutation = "MR."
fname = "George"

name= salutation + fname
print(name)




#??????????????????????????? explore other built in functions ???????????????????
number="hundred"
print(type(number))

if number.isdigit():
    n=int(number)
    print("N = ",n ,type(n))


songName="Hello.mp3"
print(songName)
if songName.endswith(".mp3"):
    print("Play the audio file")



