# Strings
# In built functions -
# Function -> Repeat a task - You can use a function
# print(), input(), type(), format(), max, min, id() ....

# Strings
name = 'Amit'
print(name)
print(type(name))  # str
print(id(name))  # id -> memory address where its is stored 28949412...
print(len(name))  # length of the string starts from 1
# name = name.count('a')
# print(name)  # 0 as python is case sensitive
name = name.count('A')
print(name)
# print(name[2]) # string index out of range

# python - Immutable - that can't be changed
# name[0]='P'  # doesn't support assignment