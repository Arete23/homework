immutable_var = (1, 2, 'a', 'b')
print('Immutable tuple:', immutable_var)

# immutable_var[0] = 5
# TypeError: 'tuple' object does not support item assignment
# Значения элементов кортежа нельзя изменить, т.к. это неизменяемый  список.
# Сделано это для защиты данных, которые не должны изменяться

mutable_list = [1, 'two', 'a', 'b', True]
mutable_list[4] = 'Modified'
mutable_list[1] = 2
print('Mutable list:', mutable_list)