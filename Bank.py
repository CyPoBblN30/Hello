import sqlite3

conn = sqlite3.connect('bank.db')
sql = conn.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS clients (client_id INTEGER, username TEXT, nomer TEXT, balance REAL, vklad REAL);')
sql.execute('INSERT INTO clients VALUES(1, "Cherepanov", "+998935743667", 0.00, 0.00);')   # регистрация клиентов
conn.commit()
print(sql.execute('SELECT * FROM clients WHERE username="Cherepanov" and nomer="+998935743667";').fetchall())   # поиск клиентов по ФИО и номеру телефона
sql.execute('UPDATE clients SET balance=1000000.00 WHERE client_id=1;')   # пополнение баланса
conn.commit()
sql.execute('UPDATE clients SET balance=1000000.00 - 400000 WHERE client_id=1;')   # снятие денег с баланса
conn.commit()
print(sql.execute('SELECT balance FROM clients WHERE username="Cherepanov";').fetchone())   # просмотр баланса
print(sql.execute('SELECT * FROM clients;').fetchall())   # личный кабинет каждого клиента

def vklad():   # подсчет вклада
    n = float(input('Введите сумму вклада: '))
    s = int(input('Введите срок вклада: '))
    if s == 12:
        print(n * 12 * 0.2)
    elif s == 24:
        print(n * 24 * 0.2)
    else:
        print(n * 36 * 0.2)

vklad()