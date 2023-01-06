from capitalize import capitalize

if capitalize('hello') != 'Hello': # Если 'Hello' заменить н алюбую другую строку, то тест работает правильно, и, соответственно выдаёт строку 'Функция работает неверно!'.
    raise Exception('Функция работает неверно!')

if capitalize('') != '':
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')    