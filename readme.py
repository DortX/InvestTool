def read_me():
    text = """
    "InvestTool by A. Chernov" v. 0.99

    1. ОПИСАНИЕ ПРОГРАММЫ.
    Программа предназначена для помощи инвесторам в расчёте доходов/убытков, преимущественно для индивидуального
    инвестиционного счёта. Пользуясь, к примеру, приложением или web-версией "Инвестиции" от АО «Тинькофф Банк» Вы
    наверняка замечали, что доход в "Инвестициях" рассчитывается по формуле:
                           "текущая стоимость портфеля - средняя закупочная стоимость портфеля"
    При этом, отображение дохода не учитывает уже зафиксированный доход. То есть, когда Вы фиксируете прибыль путём
    продажи ценных бумаг, из отображаемого дохода вычитается разность:
                            "закупочная стоимость проданных бумаг - текущая стоимость проданных бумаг"
    Подобное происходит и вследствие некоторых других финансовых операций. К примеру, если Вы используете ИИС
     (индивидуальный инвестиционный счёт) и полученным налоговым вычетом пополнили ИИС, то "Инвестиции" воспринимают
     эту операцию как обычное пополнение счёта, а не как доход запушенный в оборот. Подсчитать реальный доход от
     операции с ценными бумагами можно вручную, так как в "Инвестициях" можно отыскать информацию о пополнениях. Но
     для ручного подсчёта всё равно требуется помнить или записывать некоторые цифры. К примеру, те же дивиденды, купоны,
     налоговый вычет.
     Программа "InvestTool by A. Chernov" сделает эти подсчёты за Вас. И для этого программе достаточно всего лишь
     получить несколько цифр от Вас (нет, не ту цифру, которая расположена на обратной стороне банковской карты).
     "InvestTool by A. Chernov" является консольной программой и не имеет графического интерфейса.
     В текущей версии "InvestTool by A. Chernov" работает только с одним инвестиционным счётом. В более поздних версиях
     программы возможно добавление функции работы с несколькими счетами.

    2. СИСТЕМНЫЕ ТРЕБОВАНИЯ.
    ПК, установленный Python последней версии.

    3. ПЕРВЫЙ ЗАПУСК.
    Итак, Вы скачали программу. Разместить её лучше в отдельной папке (каталоге), так как она создаст в текущей папке
    дополнительный файл, в котором будет хранить все вводимые Вами данные.

    Во всех случаях, когда программа просит Вас ввести какие-либо данные, после ввода данных их требуется подтвердить
    нажатием клавиши Enter. Любые цифры вводятся без каких-либо обозначений единиц ('рублей', 'метров' и т. д.).
    Если требуется указать сумму с дробными числами, то дробь следует указать через точку. То есть, '10 рублей 15 копеек'
    следует указывать как '10.15' без кавычек.

    В большинстве случаев неправильно введённые данные приведут к остановке работы программы. Это вынужденная мера нужна
    для того, чтобы Вы случайно не повредили введённые Вами же данные, которые хранятся в файле data.inv.
    Файл data.inv, в котором хранятся все введёные Вами данные, также можно открыть программой "Блокнот", при необходимости
    внести правки или же просто просмотреть все записи.

    При первом запуске "InvestTool by A. Chernov" запросит у Вас размер общей суммы, на которую Вы пополняли счёт. Если Вы
    используете "Инвестиции" от АО "Тинькофф Банк", то узнать размер суммы пополнения можно в меню "Аналитика" выбранного
    Вами счёта (не всего портфеля!). К примеру, открываем ИИС, заходим в раздел "Аналитика" и в разделе
    "Статистика движения" средств Вы увидите сумму пополнения.

    Важно! Если Вы пополняли ИИС налоговым вычетом и помните/знаете сумму налогового вычета, отнимите её от суммы
    пополнения. Добавить налоговый вычет к расчёту прибыли можно будет позднее. Впрочем, это замечание носит
    рекомендательный характер. Всё зависит от того, с какого момента Вы хотите начать подсчитывать доход.

    В случае обычного брокерского счёта всё немного сложнее (инвестиции это вообще сложная тема). Если Вы точно помните
    разницу между суммой пополнения и суммой вывода указывайте её. Если не помните, отнимите доход, отображаемый в
    "Инвестициях" от стоимости Вашего портфеля и введите эту цифру в "InvestTool by A. Chernov". Тогда сегодняшний день
    будет отправной точкой рассчёта Ваших доходов. К сожалению, "InvestTool by A. Chernov" не знает о Ваших предыдущих
    финансовых операциях с ценными бумагами, потому сумму вложенных средств она может узнать только от Вас.

    Итак, Вы ввели сумму, вложенную Вами на инвестиционный счёт. Далее следует программа запросит у Вас общую стоимость
    портфеля (стоимость счёта с ценными бумагами). Тут всё гораздо проще - эта цифра всегда на виду. В "Инвестициях"
    заходим на интересующий счёт и раздел "Стоимость в рублях". Эта именна та цифра, которую "InvestTool by A. Chernov"
    просит Вас ввести, когда пишет "Введите общую стоимость Вашего портфеля: ".

    После подтверждения введёных данных программа будет готова к работе. Вы можете спокойно закрыть её и продолжить работу
    с "InvestTool by A. Chernov" позже. Все данные сохранены и сохраняются автоматически при дальнейшей работе.

    4. ПОСЛЕДУЮЩИЕ ЗАПУСКИ.
    При последующих запусках "InvestTool by A. Chernov" Вы увидите сумму вложенных средств, текущую стоимость портфеля,
    доход в виде налогового вычета (далее - НВ) и рассчёт прибыли в рублях и процентах. Расчёт прибыли - это и есть
    основной результат работы программы. После нажатия клавиши Enter Вы попадёте в Главное меню программы.

    В главном меню Вы можете проверить баланс, сообщить программе о новых финансовых операциях, совершённых Вами.

    4.1. ГЛАВНОЕ МЕНЮ.
    Переход по меню осуществляется вводом номера меню и нажатием клавиши Enter.
    № 1. Проверить баланс - отображает сумму вложенных средств, текущую стоимость портфеля, доход от НВ и прибыль.
    № 2. Пополнение - используйте для ввода информации о пополнении счёта. Далее следуйте подсказкам программы.
    № 3. Снятие - используйте для ввода информации о выводе средств со счёта (неактуально для ИИС).
    № 4. Изменить общую стоимость портфеля - Вы можете обновлять эти данные в любой удобный промежуток времени: ежедневно/
    ежемесячно, регулярно/нерегулярно, в любой момент, когда Вам требуется рассчитать доход от инвестиций на текущий момент.
    Рекомендуется изменять это значение в тот момент, когда торговля на бирже закрыта, так как в момент открытой торговли
    стоимость бумаг непостоянна.
    № 5. Пополнить счёт налоговым вычетом - если Вы получили налоговый вычет за использование ИИС и пополнили полученными
    средствами счёт, для которого используете программу, то используйте это меню. Программа суммирует НВ с вложенными
    средствами, стоимостью портфеля и предыдущими пополнениями средствами НВ. Дополнительных действий с Вашей стороны не
    потребуется.
    № 6. Указать доход в виде налогового вычета без пополнения счёта - для случая, если Вы получили НВ но не стали пускать
    eго в оборот, а пустили на другие цели (совершили покупку, пополнили банковский счёт). В этом случае программа суммирует
    НВ только с уже существующим (или нулевым) значением НВ и будет учитывать новое значение при расчёте прибыли. Однако
    сумму вложенных средств и текущую стоимость портфеля введённое Вами значение не повлияет.
    № 7. Просмотр операций - аналог ручного просмотра файла data.inv с удобной сортировкой по типу операций и с нумерацией.
    № 99. Удалить все данные* - используйте этот пункт только если хотите очистить программу ото всех введённых данных и
    привести её к состоянию первого запуска. Программа переименовывает файл data.inv в файл data.tmp и создаёт новый файл
    data.inv. Это нужно для того, чтобы при желании Вы могли восстановить предыдущие записи. Но при повторном использовании
    пункта 99 файл data.tmp будет перезаписан вновь и Вы потеряете хранящиеся в нём данные навсегда. Будьте аккуратны и не
    используйте этот пункт, если не понимаете, как он работает. Делайте резервные копии указанных файлов перед любыми
    операциями с ними.

    5. ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ.
    5.1. Программа распространяется "Как есть", разработчик не несёт никакой ответственности за её использование или за
    последствия её использования.
    5.2. При размещении "InvestTool by A. Chernov" на сторонних ресурсах пользователь/распространитель программы обязуется
    указывать ссылку на профиль автора в ВК https://vk.com/dort_x и указывать его в качестве разработчика программы.

    6. ПРИМЕЧАНИЯ.
    Программа разрабатывалась для личного пользования и под личные нужды, в т. ч. для использованиия в портфолио. Готов
    выслушать предложения по её улучшению. По всем вопросам пишите в ВК: https://vk.com/dort_x

    В дальнейшем планирую пути развития программы "InvestTool by A. Chernov" - графическую версию для ПК, адаптацию под
    Web-сервис и мобильное приложение. Без указания сроков исполнения.
    """
    print (text)
    print('Нажмите Enter для продолжения...')
    input()
    main_menu()