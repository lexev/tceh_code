#2.2.Написать функцию для определения НОК для двух чисел.

aa =  eval (input('Введите первое число: ' ))
bb = int (input ('Введите второе число: '))
print (type (aa))
def nok (a, b):
    m = a * b
    while a!=0 and b!=0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return m // (a + b)
nk = nok (aa, bb)
print ("НОК чисел {} и {} равно {}".format (aa, bb, nk))