dictFirstName = dict()
dictLastName = dict()
dictPhoneNumber = dict()
dictComment = dict()

# создаем словари для хранения данных по ключам
def dictCreate(dataTuple):  
    for item in dataTuple: # перебираем кортежи внутри списка
        splitedData = item[1].split(',') # второй элемент кортежа содержит ['1', 'Иванов', 'Сергей', '8-435-342-25-34', 'Серёга рабочий']
        dictFirstName[item[0]] = splitedData[0] # пара ключ - фамилия (первый элемент кортежа содержит ключ контакта)
        dictLastName[item[0]] = splitedData[1] # имя
        dictPhoneNumber[item[0]] = splitedData[2] # номер телефона
        dictComment[item[0]] = splitedData[3] # комментарий
    print("Импорт завершён успешно!")
    print("Нажмите любую клавишу для продолжения...", end='')
    input()

# подготоваливаем данные к экспорту (преобразуем из словарей в строку согласно формату файла)
def prepareExportStr(fileType):
    data = ''
    if (fileType == "type1"):
        for i in range(len(dictFirstName)): # вытаскиваем по ключю все данные из словарей
            data += dictFirstName[i] + ','
            data += dictLastName[i] + ','
            data += dictPhoneNumber[i] + ','
            if (i < len(dictFirstName) - 1): # если элемент последний, то разделитель не ставим
                data += dictComment[i] + ';**'
            else:
                data += dictComment[i]

    if (fileType == "type2"):
        for i in range(len(dictFirstName)): # вытаскиваем по ключю все данные из словарей
            data += dictFirstName[i] + '\n'
            data += dictLastName[i] + '\n'
            data += dictPhoneNumber[i] + '\n'
            if (i < len(dictFirstName) - 1): # если элемент последний, то разделитель не ставим
                data += dictComment[i] + '\n\n'
            else:
                data += dictComment[i]

    print("Экспорт завершён успешно!")
    print("Нажмите любую клавишу для продолжения...", end='')
    input()
    return data

# Поиск контакта по фамилии/номеру телефона
def findContact(key):
    for keyDict, value in dictFirstName.items(): # возвращает кортеж (ключ, значение) из словаря
        if value == key:
            return keyDict
    
    for keyDict, value in dictLastName.items(): # возвращает кортеж (ключ, значение) из словаря
        if value == key:
            return keyDict

    for keyDict, value in dictPhoneNumber.items(): # возвращает кортеж (ключ, значение) из словаря
        if value == key:
            return keyDict
    
    for keyDict, value in dictComment.items(): # возвращает кортеж (ключ, значение) из словаря
        if value == key:
            return keyDict

# печать одного контакта
def printOneContact(key):
    print(chr(27) + "[2J")
    print("Контакт найден: ")
    print(dictFirstName.get(key), end = ' ')
    print(dictLastName.get(key), end = ' ')
    print(dictPhoneNumber.get(key), end = ' ')
    print(dictComment.get(key))
    print("Нажмите любую клавишу для продолжения...", end='')
    input()

# обновляем все словари после удаления контакта
def refreshContanctList(rmKey):
    dictFirstName.setdefault(rmKey, dictFirstName[len(dictFirstName)])
    dictFirstName.pop(len(dictFirstName)-1)
    
    dictLastName.setdefault(rmKey, dictLastName[len(dictLastName)])
    dictLastName.pop(len(dictLastName)-1)

    dictPhoneNumber.setdefault(rmKey, dictPhoneNumber[len(dictPhoneNumber)])
    dictPhoneNumber.pop(len(dictPhoneNumber)-1)

    dictComment.setdefault(rmKey, dictComment[len(dictComment)])
    dictComment.pop(len(dictComment)-1)

# функция для удаления контакта
def removeContact(key):
    rmKey = findContact(key)
    dictFirstName.pop(rmKey)
    dictLastName.pop(rmKey)
    dictPhoneNumber.pop(rmKey)
    dictComment.pop(rmKey)
    refreshContanctList(rmKey)
    print("Контакт удалён")
    print("Нажмите любую клавишу для продолжения...", end='')
    input()

# функция добавления контакта
def addContact(firstName, lastName, phoneNumber, comment):
    key = len(dictFirstName)
    dictFirstName.setdefault(key, firstName)
    dictLastName.setdefault(key, lastName)
    dictPhoneNumber.setdefault(key, phoneNumber)
    dictComment.setdefault(key, comment)
    print("Контакт добавлен")
    print("Нажмите любую клавишу для продолжения...", end='')
    input()
    