from requests import get
import numpy as np
import pandas as pd

# Python Requests — это библиотека, позволяющая отправлять HTTP-запросы разного уровня сложности
# веб-сервисам и получать от них соответствующие ответы.

r = get("https://api.thedogapi.com/v1/breeds")
print(r.json())

r = get('https://httpbin.org/get')
print(r.status_code)

# NumPy (расшифровывается как Numerical Python) — это библиотека для языка Python,
# которая позволяет работать с многомерными массивами и матрицами. Она предоставляет набор
# высокоуровневых математических функций для операций над этими массивами.

# последовательность из 10 элементов с границами и шагом 2
arr = np.arange(2, 10, 2)
print(arr)

# создадим нулевую матрицу размером 2 x 3
total = np.zeros((2, 3))
print(total)

# Pandas — это программная библиотека на языке Python для обработки и анализа данных.
s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
print("Фильтрация")
print(s[s > 2])

students_marks_dict = {"student": ["Студент_1", "Студент_2", "Студент_3"],
                       "math": [5, 3, 4],
                       "physics": [4, 5, 5]}
students = pd.DataFrame(students_marks_dict)
students.index = ["A", "B", "C"]
print(students)
