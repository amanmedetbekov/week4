#Файлы



#Файлы бывают текстовые и бинарные (картинка, аудио, видео и тд )


# f = open(путь, режим)



# 'r' чтение 

# 'w' перезапись 

# 'x' запись в новый файл

# 'a' добавление 



# t - текст 
# b - бинарный файл



# '+' - разрешает чтение и запись



# открывать для чтения 


# f = open('test1.txt', 'rt')
# f = open('test1')
# f = open('/home/aman/Desktop/makers/week4/test1.txt')
# f = open('test1.txt', 'a+')



"""методы чтения"""
# read   прочитывет весь файл в виде одной большой строки

# f = open('test1.txt', 'rt')
# contet = f.read()
# print(type(contet))
# f.close


""""""
# readline  считывает по одной строчке

# f = open('test1.txt', 'rt')
# contet = f.readline()
# print(contet)
# f.close


""""""
# readlines  возвращает строки в списке

# f = open('test1.txt', 'rt')
# contet = f.readlines()
# print(contet)
# f.close



"""методы записи"""

""""""
# write(str) записывает одну строку
# f = open('test1.txt', 'wt')
# f.write('Hello\n') #перезаписали в файле teast1.txt
# f.write('World\n')
# f.close


# f = open('test2.txt', 'xt') #создали новый файл test2.txt
# f.close


# f = open('test1.txt', 'at') #дозапись
# f.write('Line1\n')
# f.write('Line2\n')
# f.close



""""""
# writelines(list) записывает несколько строк (в листе)

# f = open('test1.txt', 'wt')
# f.writelines(['Hello\n', 'world'])
# f.close




''''''
# f = open('test2.txt', 'at+')
# f.write('AmanAmanAman dfa')
# f.seek(0)
# print(f.read())
# f.close()

# f = open('test2.txt', 'at+')
# f.write('AmanAmanAman dfa')
# position = f.tell()
# print(position)
# f.close()


''''''
# f = open('f1.py', 'rt')
# content = f.read()
# print(repr(content))
# f.close()


''''''
# f = open('f1.py', 'rt')
# try:
#     content = f.read()
    
    
# except:
#     f.close()



# """with"""
# with open('f1.py', 'rt') as f:
#     content = f.read()


''''''
# html, xml, yaml

# JSON (JavaScript Object Notation)

# projector = {'brand': 'Acer', 'color': 'black',
#              'full_hd': True, 'price': 100000, 
#              'accessories': ('case', 'cable'), "sensor": None}



# import json

"""dumps()"""
# dumps(python_obj)  преобразует в Python объект в строку в формате json

# res = json.dumps(projector)
# print(res)


#Все кавычки становятся двойными
# Все объекты, присущие Python (кортежи, True, False, None) переводятся в соответствующие в JS

# 'a' -> "a"
# 10 -> 10
# True, False -> true, false 
# [1, 2, 3] -> [1, 2, 3]
# {'a': 10} -> {"a": 10}
# (1, 2, 3) -> [1, 2, 3]
# None      -> null




"""loads"""
# loads(json_str) - преобразует json строку в Python объект


# input = '{"brand": "Acer", "color": "black", "full_hd": true, "price": 100000, "accessories": ["case", "cable"], "sensor": null}'
# res1 = json.loads(input)
# print(res1)



''''''
# from json import dumps
# phones = [{'Model':'Apple', 'color': 'black'},
#     {'Model':'Nokia', 'color': 'black'},
#     {'Model':'Samsung', 'color': 'black'}
# ]

# res = dumps(phones)
# print(res)


# with open()


''''''
# import json
# открытие JS файла


# with open('f.json', 'rt') as file:
#     con = file.read()
#     human = json.load(con)
#     print(type(human))


# load 
# with open('f.json', 'rt') as f:
#     stu = json.load(f)
#     print(stu)




''''''
# import json
# phones = [{'Model':'Apple', 'color': 'black'},
#     {'Model':'Nokia', 'color': 'black'},
#     {'Model':'Samsung', 'color': 'black'}
# ]

# with open('phone.json', 'wt') as f:      #перезапись переменная phones в файле phone.json методом dumps
#     res = json.dumps(phones)
#     f.write(res)

# with open('phone.json', 'wt') as g:
#     json.dump(phones, g)               #перезапись переменная phones в файле phone.json методом dump





