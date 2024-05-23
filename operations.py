import connect
from menu import main_menu
import datetime

class Operation:
    def __init__ (self, pBalance, pPrice, pNumber):
        accountStatus = connect.BalanceInstall(0, 0)
        pBalance, pPrice, pTax = (accountStatus.check_balance_service())
        try:
            pNumber = float(input('Введите сумму операции: '))
        except:
            print('Неверное значение. Перезапустите программу.')
            exit()
        self.date = str(datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S"))
        self.balance = pBalance
        self.price = pPrice
        self.number = pNumber
        self.tax = pTax
        self.addbalance = float(self.balance) + self.number
        self.addprice = float(self.price) + self.number
        self.addtax = float(self.tax) + self.number
        self.delbalance = float(self.balance) - self.number
        self.delprice = float(self.price) - self.number

class ReplenishClass(Operation):
    def __init__ (self, pBalance, pPrice, pNumber):
        super().__init__(pBalance, pPrice, pNumber)
    def replenish (self):
        addlist = ('Пополнение: ' + str(self.date) + ' = ' + str(self.number) + ' руб.')
        with open('data.inv', 'r', encoding='utf-8') as file:
            search = file.readlines()
        with open('data.inv', 'w', encoding='utf-8') as file:
            for line in search:
                if line.startswith('balance: '):
                    file.write('balance: ' + str(self.addbalance) + '\n')
                elif line.startswith('price: '):
                    file.write('price: ' + str(self.addprice) + '\n')
                else:
                    file.write(line)
        with open('data.inv', 'a', encoding='utf-8') as file:
            file.write(str(addlist)  + '\n')
        accountStatus = connect.BalanceInstallUser(0, 0)
        accountStatus.check_balance_user()
        print ('Добавлена финансовая операция: ', addlist)
        print ('Нажмите Enter для продолжения...')
        input()
        main_menu()

class WithdrawClass(Operation):
    def __init__ (self, pBalance, pPrice, pNumber):
        super().__init__(pBalance, pPrice, pNumber)
    def withdraw (self):
        addlist = ('Снятие: ' + str(self.date) + ' = ' + str(self.number) + ' руб.')
        with open('data.inv', 'r', encoding='utf-8') as file:
            search = file.readlines()
        with open('data.inv', 'w', encoding='utf-8') as file:
            for line in search:
                if line.startswith('balance: '):
                    file.write('balance: ' + str(self.delbalance) + '\n')
                elif line.startswith('price: '):
                    file.write('price: ' + str(self.delprice) + '\n')
                else:
                    file.write(line)
        with open('data.inv', 'a', encoding='utf-8') as file:
            file.write(str(addlist)  + '\n')
        accountStatus = connect.BalanceInstallUser(0, 0)
        accountStatus.check_balance_user()
        print ('Добавлена финансовая операция: ', addlist)
        print('Нажмите Enter для продолжения...')
        input()
        main_menu()

class DropPriceClass(Operation):
    def __init__ (self, pBalance, pPrice, pNumber):
        super().__init__(pBalance, pPrice, pNumber)
    def drop_price (self):
        addlist = ('Изменение стоимости портфеля: ' + str(self.date) + ' = ' + str(self.number) + ' руб.')
        with open('data.inv', 'r', encoding='utf-8') as file:
            search = file.readlines()
        with open('data.inv', 'w', encoding='utf-8') as file:
            for line in search:
                if line.startswith('price: '):
                    file.write('price: ' + str(self.number) + '\n')
                else:
                    file.write(line)
        with open('data.inv', 'a', encoding='utf-8') as file:
            file.write(str(addlist)  + '\n')
        accountStatus = connect.BalanceInstallUser(0, 0)
        accountStatus.check_balance_user()
        print ('Добавлена финансовая операция: ', addlist)
        print('Нажмите Enter для продолжения...')
        input()
        main_menu()
class TaxIncome(Operation):
    def __init__ (self, pBalance, pPrice, pNumber):
        super().__init__(pBalance, pPrice, pNumber)
    def tax_income(self):
        addlist = ('Налоговый вычет (доход добавлен на баланс): ' + str(self.date) + ' = ' + str(self.number) + ' руб.')
        with open('data.inv', 'r', encoding='utf-8') as file:
            search = file.readlines()
        with open('data.inv', 'w', encoding='utf-8') as file:
            for line in search:
                if line.startswith('balance: '):
                    file.write('balance: ' + str(self.addbalance) + '\n')
                elif line.startswith('price: '):
                    file.write('price: ' + str(self.addprice) + '\n')
                elif line.startswith('TaxIncome: '):
                    file.write('TaxIncome: ' + str(self.addtax) + '\n')
                else:
                    file.write(line)
        with open('data.inv', 'a', encoding='utf-8') as file:
            file.write(str(addlist)  + '\n')
        accountStatus = connect.BalanceInstallUser(0, 0)
        accountStatus.check_balance_user()
        print ('Добавлена финансовая операция: ', addlist)
        print ('Нажмите Enter для продолжения...')
        input()
        main_menu()

    def tax_income_with(self):
        addlist = ('Налоговый вычет (доход, не добавлен на баланс): ' + str(self.date) + ' = ' + str(self.number) + ' руб.')
        with open('data.inv', 'r', encoding='utf-8') as file:
            search = file.readlines()
        with open('data.inv', 'w', encoding='utf-8') as file:
            for line in search:
                if line.startswith('TaxIncome: '):
                    file.write('TaxIncome: ' + str(self.addtax) + '\n')
                else:
                    file.write(line)
        with open('data.inv', 'a', encoding='utf-8') as file:
            file.write(str(addlist)  + '\n')
        accountStatus = connect.BalanceInstallUser(0, 0)
        accountStatus.check_balance_user()
        print ('Добавлена финансовая операция: ', addlist)
        print ('Нажмите Enter для продолжения...')
        input()
        main_menu()