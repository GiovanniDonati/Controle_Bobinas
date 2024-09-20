from ..database.config import get_connection

class Cortina:
    def __init__(self, id_codigo, descricao):
        self.id_codigo = id_codigo
        self.descricao = descricao

    @classmethod
    def obter_cortina(cls, id_codigo):
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM cortina WHERE id_codigo = %s"
            cursor.execute(sql, (id_codigo,))
            result = cursor.fetchone()
        connection.close()
        if result:
            return cls(**result)
        return None
    
    @classmethod
    def  todas_cortinas(cls):
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM cortina"
            cursor.execute(sql)
            results = cursor.fetchall()
        connection.close()
        return [cls(**result) for result in results]