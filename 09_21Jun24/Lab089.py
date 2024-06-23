#Unpaking of the tuple
a, b, c = (12,34,56)

t=(12,34,56)
#t.append()#append is  not works in the tuple because tuples are immutable in nature
new_t =t+(4,)
print(new_t)

my_list = list(t)
print(my_list)
my_list.append(5)
new_t2=tuple(my_list)
print(new_t2)

