# Создать телефонный справочник с возможностью импорта и экспорта данных в разных форматах.
# Функционал: 
# 1) Импорт и экспорт справочника в разных форматах (разделитель ;** и разделитель \n) +
# 2) Вывод в консоль всех контактов. +
# 3) Поиск контакта по имени/номеру телефона. +
# 4) Добавление / удаление контакта.

import userView
import dataIO
import dataProcessing

cmd = ''
impFlag = False

# + реализовать обработку ошибки печати справочника до импорта
# + реализовать print без необходимости вводить фильтр 
# + импорт книги контактов type1
# + импорт книги контактов type2
# + экспорт книги контактов type1
# + экспорт книги контактов type2
# print>filter не работает
# сдвиг словаря при rm не работает

while (cmd != "exit"):
    cmd = userView.Description() # выводим информацию о программе и командах и считываем команду
    
    # обработка команды на печать
    if (cmd == "print"): #im если ничего не импортировано, то выдаем ошибку
        config = userView.cmdProcessingPrint(cmd, impFlag) # конфигурация печати (фильтры)
        usrFlags = userView.userPrint(config) # парсинг фильтра
        dictLen = len(dataProcessing.dictFirstName) # кол-во элементов в словаре
        dataIO.printData(flags=usrFlags, usrLen=dictLen) # вывод в консоль

    # обработка команды импорта
    if (cmd == "imp"):
        impConfig = userView.cmdProcessingImp(cmd)
        impFlag = impConfig[2]
        dataProcessing.dictCreate(dataIO.readContactList(impConfig[0], impConfig[1])) # выполняем импорт

    # обработка команды экспорта
    if (cmd == "exp"):
        expConfig = userView.cmdProcessingExp(cmd) # обрабатываем команду и возвращаем конфиг
        dataIO.writeContactList(expConfig[0], dataProcessing.prepareExportStr(expConfig[1])) # экспортируем

    if (cmd == "find"):
        print("Введите ключевое слово для поиска (фамилия, имя, номер телефона или комментарий): ")
        key = input()
        dataProcessing.printOneContact(dataProcessing.findContact(key)) # ищем по ключевому слову контакт и печатаем его полностью

    if (cmd == "rm"):
        print("Введите ключевое слово для удаления контакта (фамилия, имя, номер телефона или комментарий):")
        key = input()
        dataProcessing.removeContact(key)

    if (cmd == "add"):
        impFlag = True
        print("Добавление нового контакта.")
        print("Введите фамилию: ", end = '')
        firstName = input()
        print("Введите имя: ", end = '')
        lastName = input()
        print("Введите номер телефона: ", end = '')
        phoneNumber = input()
        print("Введите комментарий: ", end = '')
        comment = input()
        dataProcessing.addContact(firstName, lastName, phoneNumber, comment)