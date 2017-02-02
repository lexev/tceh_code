#2.3. Написать функцию, которая принимает список, и возвращает словарь в формате:
#"тип данных: количество объектов" count_types([1, 4, 'd']) -> {<class 'int'>: 2, <class 'str'>: 1}
def count_types (lst):
    sl = {}
    for i in lst:
        if str(type(i)) not in sl:
            sl[str (type(i))] = 1
        else:
            sl[str(type(i))] += 1
    return sl

print (count_types([1,'ssss',2,4, (1,4,6), 'stroka']))