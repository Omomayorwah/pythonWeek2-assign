my_list = [ ]
my_list.append(10, 20, 30, 40)
my_list.insert(1, 15)
new_list = [50, 60, 70]
my_list.extend(new_list)
del my_list[-1]
my_list.sort()
print(my_list.index(30))
