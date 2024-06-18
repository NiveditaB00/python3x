# Take the 2 int numbers from the user and add them.
# we need to use the input() function

num1 = input("Enter the first number")
num2 = input("Enter the second number")
result = num1 + num2
print(result)  # 60, 67 -> 6067 as it is taking as str

# type conversion -str -> int
result1 = int(num1) + int(num2)
print(result1)  # 60,67 ->127

# + -> int sum operation
# + -> str concatenation
# int to str -> str()
# str to int -> int()

print(type(int(num1)))