from menu import main_menu

class AllOperation():
    def __init__ (self):
        with open('data.inv', 'r', encoding='utf-8') as file:
            viewfile = file.readlines()
            self.viewfile = viewfile
            self.count = 0

class ViewAll(AllOperation):
    def __init__(self):
        super().__init__()
        for line in self.viewfile:
            if line.startswith('balance: '):
                pass
            elif line.startswith('price'):
                pass
            elif line.startswith('TaxIncome'):
                pass
            else:
                self.count += 1
                print(self.count, line)
                if self.count % 10 == 0:
                    print('Нажмите Enter для вывода следующих операций\n')
                    input()
        ViewMenu()

class ViewReplenish(AllOperation):
    def __init__(self):
        super().__init__()
        for line in self.viewfile:
            if line.startswith('Пополнение: '):
                self.count += 1
                print(self.count, line)
                if self.count % 10 == 0:
                    print('Нажмите Enter для вывода следующих операций\n')
                    input()
        ViewMenu()

class ViewDrop(AllOperation):
    def __init__(self):
        super().__init__()
        for line in self.viewfile:
            if line.startswith('Снятие: '):
                self.count += 1
                print(self.count, line)
                if self.count % 10 == 0:
                    print('Нажмите Enter для вывода следующих операций\n')
                    input()
        ViewMenu()

class ViewTax(AllOperation):
    def __init__(self):
        super().__init__()
        for line in self.viewfile:
            if line.startswith('Налоговый вычет'):
                self.count += 1
                print(self.count, line)
                if self.count % 10 == 0:
                    print('Нажмите Enter для вывода следующих операций\n')
                    input()
        ViewMenu()

class ViewMenu():
    def __init__(self):
        print('##########################################')
        print('Меню просмотра операций')
        print('1. Просмотреть все операции')
        print('2. Просмотреть операции пополнения')
        print('3. Просмотреть операции снятия')
        print('4. Просмотреть операции c налоговым вычетом')
        print('99. Вернуться в главное меню')
        vAction = int(input('Введите номер меню:'))

        try:
            if vAction == 1:
                ViewAll()
            if vAction == 2:
                ViewReplenish()
            if vAction == 3:
                ViewDrop()
            if vAction == 4:
                ViewTax()
            if vAction == 99:
                main_menu()
        except:
            print('Неверное значение. Перезапустите программу.')
            exit()