﻿#2.6 Написать функцию, которая принимает на вход список списков (матрицу)
#и выводит ее в виде матрицы (один ряд на одной строке) в консоль

def matrix (list_of_lists):
    for row in list_of_lists:
        print (row)

matrix([[1,3,4,5],[2,3,5,6,8],[5,7,8,'ddd'],['eee','ffff']])