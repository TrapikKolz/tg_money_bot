import psycopg2
connect = psycopg2.connect(dbname='expenses_control', user='postgres',
                        password='striffemen2001', host='localhost')
cursor = connect.cursor()

cursor.close()
connect.close()
