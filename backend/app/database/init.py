import pymysql

def restaurar_banco_de_dados():
    conexao = pymysql.connect(
        host="localhost",
        user="root",
        password="**********"
    )
    cursor = conexao.cursor()
    with open('C:/Users/Donati/Desktop/VsCode/Controle_Cortinas/backend/app/database/database.sql','r') as arquivo:
        comandos_sql = arquivo.read()
        for comando in comandos_sql.split(';'):
            if comando.strip():
                cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()

if __name__ == "__main__":
    restaurar_banco_de_dados()
    