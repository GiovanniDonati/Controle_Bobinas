from datetime import datetime
from .bobina import Bobina
from .historico import Historico
from .cortina import Cortina
from ..database.config import get_connection

class Estoque:
    def __init__(self):
        pass
        # self.__enderecos_validos = self.__gerar_enderecos_validos()
    
    def __endereco_ocupado(self, endereco):
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "SELECT COUNT(*) AS count FROM bobina WHERE endereco_id_endereco = %s"
            cursor.execute(sql, (endereco,))
            result = cursor.fetchone()
        connection.close()
        return result['count'] > 0

    def __lote_existente(self, lote):
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "SELECT COUNT(*) AS count FROM bobina WHERE id_lote = %s"
            cursor.execute(sql, (lote))
            result = cursor.fetchone()
        connection.close()
        return result['count'] > 0

    def __endereco_valido(self, endereco):
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM endereco WHERE id_endereco = %s"
            cursor.execute(sql, (endereco,))
            endereco = cursor.fetchone()
        connection.close()
        return endereco

    def adicionar_bobina(self, bobina: Bobina, user_id):
        if not self.__endereco_valido(bobina.endereco_id_endereco):
            raise ValueError(f"Endereço {bobina.endereco_id_endereco} não é válido.")
        if self.__endereco_ocupado(bobina.endereco_id_endereco):
            raise ValueError(f"Endereço {bobina.endereco_id_endereco} já está ocupado por outra bobina.")
        if self.__lote_existente(bobina.id_lote):
            raise ValueError(f"Lote {bobina.id_lote} já existe.")
        bobina = Bobina.create(
            bobina.endereco_id_endereco,
            bobina.cortina_id_codigo,
            bobina.id_lote,
            bobina.metragem,
            bobina.data_cadastro
        )
        Historico.adicionar_historico(
            bobina.id_lote,
            user_id,
            bobina.endereco_id_endereco,
            'Cadastro',
            'bobina Nova',
            bobina.metragem
        )

    def remover_bobina(self, lote, user_id):
        bobina = Bobina.buscar_bobina(lote)
        if bobina:
            Historico.create(
                bobina.id_lote,
                user_id,
                bobina.endereco_id_endereco,
                'Baixa',
                bobina.metragem,
                "Baixa da bobina"
                )
            bobina.delete(lote)
        else:
            raise ValueError(f"Bobina com lote {lote} não encontrada.")

    def mover_bobina(self, lote, novo_endereco, user_id):
        if not self.__endereco_valido(novo_endereco):
            raise ValueError(f"Endereço {novo_endereco} não é válido.")
        if self.__endereco_ocupado(novo_endereco):
            raise ValueError(f"Endereço {novo_endereco} já está ocupado por outra bobina.")
        bobina = Bobina.buscar_bobina(lote)
        if bobina:
            Historico.create(
                bobina.id_lote,
                user_id,
                bobina.endereco_id_endereco,
                datetime.now().strftime("%Y-%m-%d"),
                'Movimentação de estoque',
                bobina.metragem,
                bobina.metragem
            )
            Bobina.update_endereco(bobina.id_lote, novo_endereco)
        else:
            raise ValueError(f"Bobina com lote {lote} não encontrada.")

    def mover_para_producao(self, lote, user_id):
        bobina = Bobina.buscar_bobina(lote)
        if bobina:
            Historico.create(
                bobina.id_lote,
                user_id,
                bobina.endereco_id_endereco,
                datetime.now().strftime("%Y-%m-%d"),
                'Produção',
                bobina.metragem,
                bobina.metragem
            )
            Bobina.update_endereco(bobina.id_lote, 'Produção')
        else:
            raise ValueError(f"Bobina com código {lote} não encontrada.")

    def buscar_bobina(self, lote):
        return Bobina.buscar_bobina(lote)

    def obter_historico(self, lote):
        bobina = Bobina.buscar_bobina(lote)
        if bobina:
            return Historico.get_by_bobina(bobina.id_lote)
        return []

    def obter_bobinas(self):
        return Bobina.buscar_todas_bobinas()
    
    def sugerir_endereço():
        # procura nos endereços, qual o primeiro que está vazio, em ordem crescente
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "SELECT id_endereco FROM endereco WHERE id_endereco NOT IN (SELECT endereco_id_endereco FROM bobina)"
            cursor.execute(sql)
            result = cursor.fetchone()
        connection.close()
        if result:
            return result['id_endereco']
        else:
            return None