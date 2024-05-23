# Импортируем функцию главного меню
from menu import main_menu
# Метод проверки наличия файла. Если его нет, он будет создан.
# Используется при обращении к классу BalanceInstall
def check_file():
    with open('data.inv', 'a', encoding = 'utf-8') as file:
        pass

class BalanceInstall:
    check_file()

    def __init__ (self, pBalance, pPrice):
        self._balance = pBalance
        self.price = pPrice
        self.tax = 0

    def check_balance_service (self):
        with open('data.inv', 'r', encoding='utf-8') as file:
            search = file.readlines()
            for line in search:
                if line.startswith('balance: '):
                    _, self._balance = line.split()
                elif line.startswith('price: '):
                    _, self.price = line.split()
                elif line.startswith('TaxIncome: '):
                    _, self.tax = line.split()
        balance = self._balance
        price = self.price
        tax = self.tax
        return balance, price, tax

class BalanceInstallUser(BalanceInstall):
    def __init__ (self, pBalance, pPrice):
        super().__init__(pBalance, pPrice)
    def check_balance_user(self):
        super().check_balance_service()
        if self._balance != 0:
            print('#################################')
            print('Вложенные средства: ' + str(self._balance) + ' руб.')
            print('Текущая стоимость портфеля: ' + str(self.price) + ' руб.')
            print('Доход в виде налогового вычета: ' + str(self.tax) + ' руб.')
            profit = float(self.tax) + float(self.price) - float(self._balance) # Вычисляем прибыль в рублях.
            percentProfit = float(self._balance)/100 # Узнаём, сколько рублей в 1 проценте.
            percentProfit = profit/percentProfit # Вычисляем прибыль в процентах.
            print('Ваша прибыль составляет: %.2f руб. или %.2f%%'%(profit, percentProfit))
            print('Нажмите Enter для продолжения...')
            input()
            main_menu()

# Если баланс равен нулю (или файл ранее не существовал), запрашиваем данные у пользователя
        if self._balance == 0:
            print('Для начала работы программы Вам следует указать вложенную Вами сумму на инвестиционный счёт')
            print('и фактическую стоимость Вашего портфеля на текущий момент.')
            print('Все суммы указываются в рублях, доли рублей указываются через точку.')
            print('Пример: 2024.05 или 12750')
            try:
                balance = input('Введите сумму, вложенную Вами на инвестиционный счёт: ')
            except:
                print('Неверное значение. Перезапустите программу.')
                exit()
            print('Вложенные средства: ' + balance + 'руб. Данные сохранены.')
            try:
                price = input('Введите общую стоимость Вашего портфеля: ')
            except:
                print('Неверное значение. Перезапустите программу.')
                exit()
            print('Стоимость портфеля: ' + price + 'руб. Данные сохранены.')
            print('Нажмите Enter для продолжения...')
            input()

            with open('data.inv', 'w', encoding='utf-8') as file:
                file.write('balance: ' + str(balance) + '\nprice: ' + str(price) + '\nTaxIncome: ' + str(self.tax) + '\n')
            self._balance = balance
            self.price = price
