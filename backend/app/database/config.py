import pymysql

DATABASE = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Libertyme_007',
    'db': 'app_cortinas',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

def get_connection():
    return pymysql.connect(
        host=DATABASE['host'],
        user=DATABASE['user'],
        password=DATABASE['password'],
        db=DATABASE['db'],
        charset=DATABASE['charset'],
        cursorclass=DATABASE['cursorclass']
    )