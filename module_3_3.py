def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(12, 'urban')
print_params(b = 25)
print_params(c = [1,2,3])


values_list_2 = [25, 12, 'cat']
values_dict = {'a': 33, 'b': "dog", 'c': False}
print_params(*values_list_2)
print_params(**values_dict)


values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)