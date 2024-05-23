def main_menu():
    import connect
    import operations
    import viewop
    import readme
    print('##########################################')
    print('Главное меню')
    print('1. Проверить баланс')
    print('2. Пополнение')
    print('3. Снятие')
    print('4. Изменить общую стоимость портфеля')
    print('5. Пополнить счёт налоговым вычетом')
    print('6. Указать доход в виде налогового вычета без пополнения счёта')
    print('7. Просмотр операций')
    print('8. Справка. О программе')
    print('--- Режим отладки ---')
    print('99. Удалить все данные*')
    print('*Будьте осторожны. Пункты меню, помеченные звёздочкой,')
    print('предназначены для отладки и к штатной работе программы не имеют отношения')
    try:
        action = int(input('Введите номер меню: '))
        if action == 1:
            accountStatus = connect.BalanceInstallUser(0, 0)
            accountStatus.check_balance_user()
        elif action == 2:
            act = operations.ReplenishClass(0, 0, 0)
            act = act.replenish()
        elif action == 3:
            act = operations.WithdrawClass(0, 0, 0)
            act = act.withdraw()
        elif action == 4:
            act = operations.DropPriceClass(0, 0, 0)
            act = act.drop_price()
        elif action == 5:
            act = operations.TaxIncome(0, 0, 0)
            act = act.tax_income()
        elif action == 6:
            act = operations.TaxIncome(0, 0, 0)
            act = act.tax_income_with()
        elif action == 7:
            act = viewop.ViewMenu()
        elif action == 8:
            act = readme.read_me()
        elif action == 99:
            import os
            os.rename('data.inv', 'data.tmp')
            print ('Данные программы были очищены!\n\n\n')
            input()
    except:
        print('Неверная команда. Перезапустите программу.')