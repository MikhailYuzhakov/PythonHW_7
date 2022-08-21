# функция вывода описания команд и их считывания
def Description():
    print(chr(27) + "[2J")
    print("Телефонный справочник v1.0")
    print("Основные функции:\n1.Импорт и экспорт телефонной книги (cmd => imp/exp)")
    print("2.Добавление и удаление контактов (cmd => add/rm)")
    print("3.Печать телефонной книги в консоль с поддержкой фильтров или полностью (cmd => print => filter/all)")
    print("4.Поиск контакта по ключам (cmd => find)")
    print("Для завершения программы введите cmd => exit")
    print("cmd> ", end='')
    cmd = input()
    print(chr(27) + "[2J")
    return cmd

# функция для вывода справочника в терминал
def userPrint(config):
    if (config[0] == '+'):
        flagFN = True
    else:
        flagFN = False

    if (config[1] == '+'):
        flagLN = True
    else:
        flagLN = False

    if (config[2] == '+'):
        flagPN = True
    else:
        flagPN = False

    if (config[3] == '+'):
        flagCT = True
    else:
        flagCT = False
    return flagFN, flagLN, flagPN, flagCT

# обработка команды на печать контактов в консоль
def cmdProcessingPrint(cmd, impFlag):
    config = '    ' # пустой конфиг
    if (impFlag): # если ничего не импортировано, то выдаем ошибку
        print("Для печать всего телефонного справочника: cmd => all")
        print("Для выборочной печати телефонного справочника cmd => filter")
        print("cmd>", end=' ')

        mode = input() # режим печать
        if (mode == "all"): # распечататать всё
            print(chr(27) + "[2J")
            config = "++++"

        if (mode == "filter"): # выборочная печать
            print(chr(27) + "[2J")
            print("Последовательность столбцов: Фамилия | Имя | Номер телефона | Комментарий")
            print("Комманда для печати фамилии и номера телефона: filter>+-+-")
            print("cmd>filter>", end='')
            config = input()
            print(chr(27) + "[2J")
    else: # обработчик ошибки при отсутствии импорта
        print(chr(27) + "[2J")
        print("Невозможно выполнить команду. В телефонном справочнике нет ни одной записи.")
        print("Выполните импорт телефонного справочника (cmd => imp) или добавьте контакт вручную (cmd => add).")
        print("Нажмите любую клавишу для продолжения...", end='')
        input()
    return config

# обработка импорта контактов 
def cmdProcessingImp(cmd):
    print("Укажите полный путь к файлу для импорта:")
    print("cmd>imp> ", end='')
    path = input() # запрос на импорт контактов от пользователя
    print(chr(27) + "[2J")
    print("Введите формат файла (imp => type1 или imp => type2)")
    print("cmd>imp> ", end='')
    fileType = input() # считываем формат файла, заданный пользователем
    impFlag = True # поднимаем флаг при завершении импорта
    return path, fileType, impFlag

# обработка экспорта контактов
def cmdProcessingExp(cmd):
    print("Укажите формат файла при экспорте (exp => type1 или exp => type2):")
    print("cmd>exp> ", end='')
    fileType = input()
    print(chr(27) + "[2J")
    print("Укажите имя экспортируемого файла с расширением:")
    print("cmd>exp>name> ", end='')
    fileName = input()
    return fileName, fileType
