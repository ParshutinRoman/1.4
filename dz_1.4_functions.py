documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

menu = '\nЧем я могу Вам помочь? \nВведите p, если Вы знаете номер документа и хотите узнать автора \nВведите l, чтобы вывести список всех документов \nВведите s, чтобы узнать на какой полке хранится документ с известным номером \nВведите a для добавления нового документа \nВведите d для удаления документа \nВведите m, чтобы переместить документ на другую полку \nВведите as для создания новой полки'


def shelf_number_by_doc_number():
    inp = input("Введите номер документа, чтобы узнать на какой полке он находится:")
    for shelfs, content_shelf in directories.items():
        if inp in content_shelf:
            print(shelfs)
    print("не существует такого номера")
    action_choise()


def name_by_doc_number(documents):
    inp = input("Введите номер документа, чтобы узнать имя автора документа:")
    for doc in documents:
        if doc['number'] == inp:
            print(doc['name'])
    print("не существует такого номера")
    action_choise()


def list(documents):
    for doc in documents:
        print(doc['type'], doc['number'], doc['name'])
    action_choise()


def add_new_doc(documents):
    number = int(input('Введите номер нового документа'))
    type = input('Введите тип документа')
    name = input('Введите автора документа')
    shelf = input('На какой полке будет храниться новый документ?')
    documents.append({"type": type, "number": number, "name": name})
    if shelf in directories:
        directories[shelf].append(number)
    else:
        directories[shelf] = [number]
    print('Список документов', documents)
    print('Список полок', directories)
    action_choise()


def del_doc_by_number(documents, directories):
    number = input('Введите номер документа, чтобы удалить его')
    for doc in documents:
        if doc['number'] == number:
            documents.remove(doc)
    for shelf_number, content_shelf in directories.items():
        if number in content_shelf:
            content_shelf.remove(number)
    print('Список документов', documents)
    print('Список полок', directories)
    action_choise()


def move_to_shelf(directories):
    number = input('Введите номер документа, который нужно переместить на другую полку:')
    shelf_number = input('Введите номер полки, на которую нужно переместить документ:')
    for shelfs, content_shelf in directories.items():
        if number in content_shelf and shelf_number in shelfs :
            content_shelf.remove(number)
            directories[shelf_number].append(number)
    print("нет документа с таким номером, или Вы выбрали несуществующую полку")
    print('Список полок', directories)
    action_choise()


def add_shelf(directories):
    shelf_number = input('Введите номер полки, которую Вы хотите создать')
    if shelf_number in directories:
        print("полка, которую Вы хотите добавить, не существует")
    else:
        directories[shelf_number] = []
    print('Список полок', directories)
    action_choise()


def action_choise():
    print(menu)
    action_choise = input()

    if action_choise.lower() == 's':
        shelf_number_by_doc_number()
    elif action_choise.lower() == 'p':
        name_by_doc_number(documents)
    elif action_choise.lower() == 'l':
        list(documents)
    elif action_choise.lower() == 'a':
        add_new_doc(documents)
    elif action_choise.lower() == 'd':
        del_doc_by_number(documents, directories)
    elif action_choise.lower() == 'm':
        move_to_shelf(directories)
    elif action_choise.lower() == 'as':
        add_shelf(directories)


print('Здравствуйте!')
action_choise()

# при перемещении несуществующего документа он добавляется в directories, а в documents - нет. Лучше вообще не перемещать ничего не существующего, а выводить соответствующее предупреждение. При перемещении документа не несуществующую полку поведение также некорректное;

# print('Список документов', documents)
# print('Список полок', directories)


# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;
