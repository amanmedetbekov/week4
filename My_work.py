""""""""""""""""""""""открытие файла"""""""""""""""""""""""""""


# инструкция .open() для открытия файла
# инструкция .close() для закрытия файла

# f = open('/home/aman/Desktop/makers/week4/text_files/text_ex', 'rt')
# print(f.read())
# f.close()   #файл закрыт

# print(f.read())   #ошибка, так как файл уже был закрыт. Прочитать не получиться (ValueError: I/O operation on closed file.)

'''закрытие с помощью try/finally'''

# f = open('/home/aman/Desktop/makers/week4/text_files/text_ex', 'rt')
# try:
#     v = f.read()
#     print(v)
# finally:    #используется для закрытия файла, потому что finally срабатывает в любом случае
#     f.close()


'''инструкция with'''
#для этой инструкции инструкция close() не нужнаб потому что with автоматически закроет файл

# with open('/home/aman/Desktop/makers/week4/text_files/text_ex', 'wt+') as f:
#     print(f.write('Hello World'))







"""""""""""""""""""""""""""Функции"""""""""""""""""""""""""""""""""""""""



""""""""""""""""""""""""""""""""""""""""""""
'''для чтения (после открытия в режиме 'r') '''
#.read()  #используется для чтения файла
# .readline() #используется для чтения только одной строки
# .readlines()  #используется для чтения всех строк 
              # возвращает содержимое всего файла в виде списка строк, где каждый элемент в списке представляет одну строку файла.



""".read()"""  #Внутри скобок можно указать размер прочитаемого текста, если не указать то прочитает целиком
#есть файл с текстом:
# >>> "Hello World! Today is a sunny day!"
# >>> "I'm study in the Makers"

# f = open('/home/aman/Desktop/makers/week4/text_files/text_ex', 'r')
# print(f.read())  #принтуется: Hello World! Today is a sunny day!
# f.close() 


# f = open('/home/aman/Desktop/makers/week4/text_files/text_ex', 'r')
# print(f.read(8))  #принтуется чтение 8 символов файла: Hello Wo
#                                                #12345678
# print(f.read(3))  #принтуется чтение последующих 3 символов: rld
# f.close()




""".readline()"""
#прочитает только одну строку (последующее чтение начнется с того места где было остановлено)
#если указать размер внутри скобок например: .redline(5), считывает 5 символов, а последующее чтение начнется с последующих символов после указанного 3
#если достигает конца файла возвращает пустую строку

# f = open('/home/aman/Desktop/makers/week4/text_files/text_ex', 'r')
# print(f.readline())  #Hello World! Today is a sunny day!
# print(f.readline())  #I'm study in the Makers
# f.close()


""".readlines()"""
#считывает все строки и возвращает список из строк

# f = open('/home/aman/Desktop/makers/week4/text_files/text_ex', 'r')
# print(f.readlines()) #принтуется: ['Hello World! Today is a sunny day!\n', "I'm study in the Makers"]
# #                                                                  >>>\n здесь конец строки
# f.close()



""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'''для записи (после открытия в режиме 'w', 'w+', 'a')'''
#.write()
#









def func():
    return 'Я Аман и я изменил здесь, добавил функцию'
    
