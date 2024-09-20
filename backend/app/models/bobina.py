from datetime import datetime
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from ..database.config import get_connection

class Bobina:
    def __init__(self, id_lote, cortina_id_codigo, endereco_id_endereco, data_cadastro, metragem):
        self.id_lote = id_lote
        self.cortina_id_codigo = cortina_id_codigo
        self.endereco_id_endereco = endereco_id_endereco
        self.data_cadastro = data_cadastro
        self.metragem = metragem

    @classmethod
    def criar_bobina(cls, id_lote, cortina_id_codigo, endereco_id_endereco, data_cadastro, metragem):
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO bobina (id_lote, cortina_id_codigo, endereco_id_endereco, data_cadastro, metragem) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (id_lote, cortina_id_codigo, endereco_id_endereco, data_cadastro, metragem))
            connection.commit()
            bobina_id = cursor.lastrowid
        connection.close()
        return cls(bobina_id, cortina_id_codigo, endereco_id_endereco, data_cadastro, metragem)

    @classmethod
    def buscar_bobina(cls, id_lote):
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM bobina WHERE id_lote = %s"
            cursor.execute(sql, (id_lote,))
            result = cursor.fetchone()
        connection.close()
        if result:
            return cls(**result)
        return None

    @classmethod
    def buscar_todas_bobinas(cls):
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM bobina"
            cursor.execute(sql)
            results = cursor.fetchall()
        connection.close()
        return [cls(**result) for result in results]
    
    @classmethod
    def deletar_bobinas(cls, id_lote):
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "DELETE FROM bobina WHERE id_lote = %s"
            cursor.execute(sql, (id_lote,))
            connection.commit()
        connection.close()

    @classmethod
    def atualizar_endereco(cls, id_lote, novo_endereco):
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "UPDATE bobina SET endereco_id_endereco = %s WHERE id_lote = %s"
            cursor.execute(sql, (novo_endereco, id_lote))
            connection.commit()
        connection.close()
