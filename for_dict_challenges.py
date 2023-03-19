from collections import Counter
from numpy import inf

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

name_count = Counter(student['first_name'] for student in students)

for name in name_count:
    print(f'{name}: {name_count[name]}') 

"""
counter = {}

for person in students:
    if person['first name'] not in counter:
        counter[person['first name']] = 0
    counter[person['first name']] += 1
"""


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# ???

name_count = Counter(student['first_name'] for student in students)

most_common_name = name_count.most_common(1)

print(f'Самое частое имя среди учеников: {most_common_name[0][0]}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
# ???

grade_count = 0

for grade in school_students:
    grade_count += 1
    name_count = Counter(student['first_name'] for student in grade)
    most_common_name = name_count.most_common(1)
    print(f'Самое частое имя в классе {grade_count}: {most_common_name[0][0]}')



# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???

# Объединяем учеников одного и того же класса в один общий словарь и удаляем остающийся дубль:

classes = {}

for idx, cl in enumerate(school):
    if cl['class'] in classes:
        cl['students'] += school[classes[cl['class']]]['students']
        del school[classes[cl['class']]]
    else:
        classes[cl['class']] = idx
        
# Подсчитываем число девочек и мальчиков в каждом классе, добавляем сведения в словари и отображаем результат в консоли:

for grade in school:
    grade['boys'] = 0
    grade['girls'] = 0
    for student in grade['students']:
        if is_male[student['first_name']]:
            grade['boys'] += 1
        else:
            grade['girls'] += 1
    print(f"Класс {grade['class']}: девочки {grade['girls']}, мальчики {grade['boys']}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???

# Подсчитываем число мальчиков и девочек в каждом классе и сохраняем информацию в словарях:

for idx, cl in enumerate(school):
    cl['girls'] = 0
    cl['boys'] = 0
    for id, student in enumerate(school[idx]['students']):
        if is_male[student['first_name']]:
            cl['boys'] += 1
        else:
            cl['girls'] += 1

# Создаём функцию, определяющую наибольшее значение поля в коллекции: 

def max_num_item_comp(collect, key):
    max_num = float(-inf)
    max_num_item = 0
    for idx, it in enumerate(collect):
        if it[key] > max_num:
            max_num = it[key]
            max_num_item = idx
    return max_num_item

max_boys = school[max_num_item_comp(school, "boys")]["class"]
max_girls = school[max_num_item_comp(school, "girls")]["class"]

print(f'Больше всего мальчиков в классе {max_boys}')
print(f'Больше всего девочек в классе {max_girls}')


