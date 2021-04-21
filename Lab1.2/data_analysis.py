#!/usr/local/bin/python3

#импортируем модули
from matplotlib import pyplot
from openpyxl import load_workbook

#определяем функцию значения ячейки
def getvalue(x):
    return x.value

#извлекаем таблицу из файлы MS Excel в переменную
wb = load_workbook('data_analysis_lab.xlsx')

#извлекаем конкретный лист из таблицы
sheet = wb['Data']

#извлекаем несколько столбцов из листа
years = list(map(getvalue, sheet['A'][51:]))
temperature = list(map(getvalue, sheet['C'][51:]))
activity = list(map(getvalue, sheet['D'][51:]))

#рисуем график без показа
pyplot.plot(years, temperature, label='Температура')
pyplot.plot(years, activity, label='Солнечная активность')

#добавляем надписи на график
pyplot.xlabel('Годы')
pyplot.ylabel('Активность солнца, Температура')
pyplot.legend(loc='upper left')

#рисуем финальный график
pyplot.show()