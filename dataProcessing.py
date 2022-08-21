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

