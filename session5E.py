qoute = "Work Hard Be Luckier"
#qoute = qoute.split(" ")
#data = list(qoute)
#print(data)
#data = set(qoute)
#print(data)

print(qoute*2)
print(qoute[::-1])

for i in range(len(qoute)-1,-1,-1): # IMPORTANT
    print(qoute[i], end=" ",)
