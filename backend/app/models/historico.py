from datetime import datetime
from ..database.config import get_connection

class Historico:
    def __init__(self, id_historico, bobina_id_lote, user_id_user, endereco_antigo, tipo_mov, metragem_antiga, nova_metragem):
        self.id_historico = id_historico
        self.bobina_id_lote = bobina_id_lote
        self.user_id_user = user_id_user
        self.endereco_antigo = endereco_antigo
        self.tipo_mov = tipo_mov
        self.metragem_antiga = metragem_antiga
        self.nova_metragem = nova_metragem

    @classmethod
    def adicionar_historico(cls, bobina_id_lote, user_id_user, endereco_antigo, tipo_mov, metragem_antiga, nova_metragem):
        connection = get_connection()
        date_mov = datetime.now().strftime("%Y-%m-%d")
        with connection.cursor() as cursor:
            sql = "INSERT INTO historico (bobina_id_lote, user_id_user, endereco_antigo, date_mov, tipo_mov, metragem_antiga, nova_metragem) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (bobina_id_lote, user_id_user, endereco_antigo, date_mov, tipo_mov, metragem_antiga, nova_metragem))
            connection.commit()
            historico_id = cursor.lastrowid
        connection.close()
        return cls(historico_id, bobina_id_lote, user_id_user, endereco_antigo, date_mov, tipo_mov, metragem_antiga, nova_metragem)

    @classmethod
    def buscar_historico(cls, bobina_id_lote):
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM historico WHERE bobina_id_lote = %s"
            cursor.execute(sql, (bobina_id_lote,))
            results = cursor.fetchall()
        connection.close()
        return [cls(**result) for result in results]