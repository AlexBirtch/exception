"""
Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

    p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
    Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.


Задача №2. Дополнительная (не обязательная)

    d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
    m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
    as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;


"""

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "5"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': ['5']
}


def lists():
    for document in documents:
        try:
            # print(document.get("type"), document.get("number"), document.get("name"))
            print(f"{document['type']} \"{document['number']}\" \"{document['name']}\"")

        except KeyError:
            print(f'[ОШИБКА] у документа № {document["number"]} отсутствует поле "name"')

def people():
    number_document = input('Введите номер документа: ')
    try:
        # for document in documents:
        #     if document.get("number") == number_document:
        #         print(f"'\n' {document.get('name')}")
        #         break
        # else:
        #     print('Такого документа нет в каталоге, создайте его ')
        #     add()
        for document in documents:
            for item in document:
                if number_document == document[item]:
                    return document['name']
        return 'Такого документа нет'
    except KeyError:
        return 'У данного документа нет поля "name"'
    except Exception as e:
        return f'[ОШИБКА] {e}'



def shelf():
    number_document = input('Введите номер документа: ')
    for directorie, shelfs in directories.items():
        for n_d in shelfs:
            if n_d == number_document:
                return f'Документ лежит на полке № {directorie}'

    else:
        print('Такого документа не существует, давайте создадим его')
        add()


def add_shelf():
    new_shelf = input('Введите номер новой полки: ')
    if new_shelf in directories.keys():
        return f'Полка № {new_shelf} уже существует.'
    else:
        directories[new_shelf] = []
        return f'Полка с номером {new_shelf} создана.'



def add():
    directorie = input('Введите номер полки куда положить документ: ')
    types = input('Введите тип документа: ')
    number = input('Введите номер документа: ')
    name = input('Введите фамалию и имя владельца документа: ')
    new_dict = {"type": types, "number": number, "name": name}
    documents.append(new_dict)
    for directorie_1 in directories.keys():
        if directorie_1 == directorie:
            directories[directorie_1].append(str(number))
            break
    else:
        if directorie_1 != directorie:
            directories[directorie] = [number]

    print(directories)


def main():
    while True:
        ask = input('Ведите желаемую команду:\n\
     p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;\n\
     l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";\n\
     s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;\n\
     a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.\n\
     as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;\n\
     q - quit - команда для завершения программы.''\n\n-->')
        if ask == 'p':
            print(people())
            continue
        if ask == 'l':
            lists()
        if ask == 's':
            print(shelf())
        if ask == 'a':
            add()
            continue
        if ask == 'as':
            print(add_shelf())
        if ask == 'q':
            break
        elif ask != 'a' and ask != 'l' and ask != 's' and ask != 'a' and ask != 'q' and ask != 'as':
            print('Данная команда не найдена, попробуйте еще раз!')

main()
