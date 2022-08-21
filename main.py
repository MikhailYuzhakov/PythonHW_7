# Создать телефонный справочник с возможностью импорта и экспорта данных в разных форматах.
# Функционал: 
# 1) Импорт и экспорт справочника в разных форматах (разделитель ;** и разделитель \n) +
# 2) Вывод в консоль всех контактов. +
# 3) Поиск контакта по имени/номеру телефона.
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
# возможно dataIO не нужен?
# 

while (cmd != "exit"):
    cmd = userView.Description() # выводим информацию о программе и командах и считываем команду
    
    # обработка команды на печать
    if (cmd == "print"): # если ничего не импортировано, то выдаем ошибку
        dataIO.printData(userView.userPrint(userView.cmdProcessingPrint(cmd, impFlag)))

    # обработка команды импорта
    if (cmd == "imp"):
        impConfig = userView.cmdProcessingImp(cmd)
        impFlag = impConfig[2]
        dataProcessing.dictCreate(dataIO.readContactList(impConfig[0], impConfig[1])) # выполняем импорт

    # обработка команды экспорта
    if (cmd == "exp"):
        expConfig = userView.cmdProcessingExp(cmd) # обрабатываем команду и возвращаем конфиг
        dataIO.writeContactList(expConfig[0], dataProcessing.prepareExportStr(expConfig[1])) # экспортируем