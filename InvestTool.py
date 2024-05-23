print('#################################')
print('# Контроль инвестиций v 0.99   #')
print('#################################')
print('#                by A Chernov   #')
print('#################################')
import connect # Импорт connect.py
# Создание экземпляра BalanceInstallUser. Посылаем в подкласс нулевые значения,
# так как позднее мы найдём значения в файле data.inv
accountStatus = connect.BalanceInstallUser(0, 0)
# Выполняем метод, который читает data.inv и выводит их на экран
accountStatus.check_balance_user()

from menu import main_menu # Импорт функции main_menu из файла menu
main_menu() # Импортируемая функция вызова главного меню.