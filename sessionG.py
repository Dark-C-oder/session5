s1 = {1,2,3,'a','b'}
s2 = {1,'a','b'}
print(1 in s1)

print(s1.union(s2))
print(s2.issubset(s1))
print(s1.issuperset(s2))

print("S1 before is:", s1)
print(s1.union(s2))
print("s1 now is ", s1)

print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))