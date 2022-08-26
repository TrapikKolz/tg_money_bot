import psycopg2
connect = psycopg2.connect(dbname='expenses_control', user='postgres',
                        password='striffemen2001', host='localhost')
cursor = connect.cursor()

def register_sql(chat_id, username, first_name, last_name, OSN_percent, DOP_percent, OTK_percent, INV_percent):
    print('Типо добавили в базу))))ыыы))')

def check_chat_id_regester(chat_id):
    print('Проверка пройдена')
    return [True, 'Макс']

cursor.close()
connect.close()
