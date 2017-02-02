questions = {
    "Целочисленный тип данных :": 'int',
    "Истина в Python :": 'true',
    "Есть ли цикл с постусловием :": 'нет',
    "Функция ввода данных в программу в Python 3 :": 'input',
    "Функция для определения длины строки :": 'len',
    "Цикл с предусловием :": 'while',
    "Символ однострочного комментария :": '#',
    "Какой язык мы изучаем :-) :": 'python',
    "Тип с плавающей запятой :": 'float',
    "Функция, чтобы узнать тип объекта :": 'type'
}

r_ans, w_ans = 0,0

def victorina(qw, ans):
    global r_ans, w_ans

    s = str (input(qw))
    if str.lower(s) == ans:
        print('Правильно!\n')
        r_ans += 1
    else:
        print('Неправильно!\n')
        w_ans += 1



for key, val in questions.items():
    victorina(key, val)
print('Правильных ответов {}, неправильных ответов {}'.format(r_ans, w_ans))