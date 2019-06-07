name="John Watson"
print(name, type(name), hex(id(name)))
print(len(name))
print(max(name))
print("min=",min(name)) # space is printed

print(name[1])
print(name[len(name)-1])
print(name[1:3]) #slicing
print("t" in name) # membership testing

email = "john@exmple.com"
if "@" in email and ("." in email):
    print("Valid Email")
else:
    print("Invalid Email")

# Create a Program to Test a Member in a Sequence
# Your program shouuld work on tuple list and string