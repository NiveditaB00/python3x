# Strings
# Bunch of Char
name = 'harry'
print(name)
name = "harry"
print(name)
name = """Harry, is a good persom
he love to walk alone
...
"""
print(name)

dir = 'C:\nomedir\some dir'  #printed in 2 lines C: and new line
print(dir)

# Raw string
dir = r'C:\nomedir\some dir'  # o/p in single line as given
print(dir)

# Format of string
first_name = 'Harry'
last_name = 'Potter'
print(first_name + " " + last_name)
print(first_name, last_name)
# f -> formatting - it will replace the values of the variables
# {} -> placeholder
print(f'Your Full name is {first_name} {last_name}')