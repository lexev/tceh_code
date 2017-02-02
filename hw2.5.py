#2.5 Написать функцию, которая принимает любое количество аргументов,
#она вернуть список типов, принятых аргументов find_types(1, 's', []) -> [<class 'int'>, <class 'str'>, <class 'list'>]
def type_list_item(*lst):
    result_type = set()
    for item in lst:
        result_type.add(str(type(item)))
    return list(result_type)

lst_types = type_list_item([1,3], (1,), 'qwerty', 1, 3, 1.34)

print ("Список типов принятых аргументов:", lst_types)
