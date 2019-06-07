"""employees = {"name": "john", "eid":101, "email": "john@example.com", "salary":30000}
print(employees, type(employees))
print(len(employees))
print(max(employees))
print(min(employees))

employees["name"] = "john watson" #update operation
print(employees)

keys = employees.keys()
values=employees.values()

print(keys, type(keys))
print(values, type(values)) # in dictionery we have unique keys but values can be duplicated


for key in keys:
    print(key, employees[key])"""

dishes = {"dish1":100, "dish2":200, "dish3":300}
values=dishes.values()
key=dishes.keys()
n=max(values)
print(max(values))


## Dishes. -> explore mor built-ins
## explore dictionery in dictionery, set in set
## set in dictionery or vice versa