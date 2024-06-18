# List - Shopping List
# milk, bread, butter, poha
# 1. add item
# 2. remove item
# 3. update item
# 4. view item
# 5. Exit

shopping_list = ['milk', 'bread', 'butter','poha']
print(shopping_list)
print(len(shopping_list))  # 4
print(shopping_list[0])  # milk
print(shopping_list[-1])  # poha

shopping_list.append("curd")  # Add item in the end
print(shopping_list)
shopping_list.insert(3, "jam")  # add item in the middle
print(shopping_list)
shopping_list.extend(["chips", "salt"])  # add multiple items in the end, adding list to another list
print(shopping_list)

shopping_list.remove("bread")
print(shopping_list)

shopping_list.reverse()  # reversing the list
print(shopping_list)
my_list = [ 1, 3.14, True, "Siri"]
print(type(my_list))  # list