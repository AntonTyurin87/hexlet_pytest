def capitalize(text):
    if text == '':      # Закоментить эту строку    
        return ''       # И вот эту строку
    first_char = text[0].upper()
    rest_substring = text[1:]
    return f'{first_char}{rest_substring}'

# Если изменить выше указанные строки, то при выполнеии тестирования по команде PYTHONPATH=hexlet_pytest python3 tests/test_capitalize.py
# выдаёт такое:
'''
Traceback (most recent call last):
  File "tests/test_capitalize.py", line 6, in <module>
    if capitalize('') != '':
  File "/home/anton/hexlet_lessons/hexlet_pytest/hexlet_pytest/capitalize.py", line 4, in capitalize
    first_char = text[0].upper()
IndexError: string index out of range
''' 
 