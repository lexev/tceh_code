#2.4Написать функцию, которая принимает два словаря, сравнивает их ключи,
# выдает в консоль сколько у них общих ключей

def two_dict (dict1, dict2):
    if isinstance(dict1, dict) and isinstance(dict2, dict):
       s = set(dict1.keys()) & set(dict2.keys())
       return (len(s))
    else:
        print ('Неверный формат данных')
        return None

d = {"qwerty":1, "assss":23, "dddd":45, "qw":34}
d1 = {"qwerty":1, "assss":23, "dddd":45, }

print ("Кол-во общих ключей словарей: ", two_dict (d, d1))
