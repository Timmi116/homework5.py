immutable_var = 1, 'Urdan', 55, True
print(immutable_var)
'''immutable_var[0] = 220
print(immutable_var)'''
# # особенность кортежа это упорядочность, неизменяемость и элементы хранящиеся внутри кортежа могут быть разные.
mutable_list = [1, 'Denis', 46, 'a']
mutable_list[0] = 220
print(mutable_list)