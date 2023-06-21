#Задание 1

name = ['Вова', 'Петя', 'Галя', 'Женя', 'Саша']
city = ['Оренбург', 'Псков', 'Воронеж', 'Ростов', 'Москва']
car = ['Niva', 'Lada', 'Volvo', 'Bmw', 'Gaz']

# Объединяем списки с помощью функции zip
data = zip(name, city, car)

# Открываем файл для записи
file = open('Задание1.txt', 'w',encoding='utf-8')
    # Обрабатываем каждую запись данных
for i in data:
        # Распаковываем данные
    name, city, car = i
        # Форматируем строку с данными
    result = f"{name} живет в {city} и ездит на {car}\n"
        # Записываем результаты в файл
    file.write(result)
file.close()

#Задание2

file1 = open('Задание2.txt','r',encoding='utf-8')
cont = file1.read()
cont1 = cont.split()
contt = 0

for i in cont1:
    if len(i) > 7:
        print(i)
        contt+= 1
        if contt % 4 == 0:
            print()
file1.close()
