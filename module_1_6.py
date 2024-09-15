my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print('Dict:', my_dict)
print('Existing value:', my_dict['Masha'], " \n" 'Not existing value:', my_dict.get('Anton'))
my_dict.update({'Kamila': 1981,
                'Artem': 1915})
a = my_dict.pop('Egor')
print('Deleted value:', a)
print('Modified dictionary: ', my_dict)

my_set = {1, 3, 5, 8, 9, 1, 3, 5, 8, 'Яблоко', 'Яблоко', 42.314, 'Яблоко', (5, 6, 1.6)}
my_list = [1, 1, 1, 1, 'Яблоко', 'Яблоко', 42.314, 'Яблоко']
my_set = set(my_list)
print('Set:', my_set)
my_set.add(13)
my_set.add((5, 6, 1.6))
my_set.discard(1)
print('Modified set:', my_set)
