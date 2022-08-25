import dataProcessing

data = [] # Len(data) вернёт кол-во строк в файле

# считывание данных из списка контактов
def readContactList(path, fileType): # привести к виду ['1', 'Иванов', 'Сергей', '8-435-342-25-34', 'Серёга рабочий'], 
    if (fileType == "type1"):
        with open(path, mode='r', encoding='utf-8') as file:
            data = file.read().split(';**') # делим строку по ключу
        data = list(enumerate(data)) # создаем кортеж (key, dataList)

    if (fileType == "type2"):
        with open(path, mode='r', encoding='utf-8') as file:
            data = file.read().split('\n\n') # делим строку по ключу
        for i in range(len(data)):
            data[i] = data[i].replace("\n", ",") # приводим данные к необходиому виду
        data = list(enumerate(data)) # создаем кортеж (key, dataList)

    return data

# записываем в файл данные
def writeContactList(path, data):
    with open(path, mode='w', encoding='utf-8') as file:
        file.write(data)
    

# вывод данных в терминал
def printData(flags, usrLen):
    for i in range(usrLen):
        if (flags[0]):
            print(" ", end='')
            print(dataProcessing.dictFirstName[i], end='')

        if (flags[1]):
            print(" ", end='')
            print(dataProcessing.dictLastName[i], end='')

        if (flags[2]):
            print(" ", end='')
            print(dataProcessing.dictPhoneNumber[i], end='')

        if (flags[3]):
            print(" ", end='')
            print(dataProcessing.dictComment[i], end='')

        print("\n", end='')
    print("Нажмите любую клавишу для продолжения...", end='')
    input()