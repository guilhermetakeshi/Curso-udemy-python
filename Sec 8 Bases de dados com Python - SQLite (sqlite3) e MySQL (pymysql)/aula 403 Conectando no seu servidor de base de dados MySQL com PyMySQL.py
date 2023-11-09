MYSQL_ROOT_PASSWORD = 'CHANGE-ME'
MYSQL_DATABASE = 'CHANGE-ME'
MYSQL_USER = 'CHANGE-ME'
MYSQL_PASSWORD = 'CHANGE-ME'
MYSQL_HOST = 'CHANGE-ME'

# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='usuario',
    password='senha',
    database='base_de_dados',
)

with connection:
    with connection.cursor() as cursor:
        # SQL
        print(cursor)