from datetime import datetime
from .bobina import Bobina
from .historico import Historico
from .cortina import Cortina
from ..database.config import get_connection

class Estoque:
    def __init__(self):
        self.__enderecos_validos = self.__gerar_enderecos_validos()

    def __gerar_enderecos_validos(self):
        enderecos = []

        for letra in 'ABCD':
            for number in range(1, 96):
                enderecos.append(f'{letra}{number}')

        for number in range(17, 96):
            enderecos.append(f'E{number}')

        for number in range(47, 96):
            enderecos.append(f'F{number}')

        for number in range(82, 96):
            enderecos.append(f'G{number}')

        for letra in 'ABCDE':
            for number in range(1, 5):
                enderecos.append(f'G1-{letra}{number}')

        for letra in 'ABCD':
            for number in range(1, 6):
                enderecos.append(f'G2-{letra}{number}')

        for letra in 'AB':
            for number in range(1, 12):
                enderecos.append(f'G3-{letra}{number}')

        return enderecos

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
            cursor.execute(sql, (lote,))
            result = cursor.fetchone()
        connection.close()
        return result['count'] > 0

    def __endereco_valido(self, endereco):
        return endereco in self.__enderecos_validos

    def adicionar_bobina(self, bobina: Bobina, user_id):
        if not self.__endereco_valido(bobina.endereco_id_endereco):
            raise ValueError(f"Endereço {bobina.endereco_id_endereco} não é válido.")
        if self.__endereco_ocupado(bobina.endereco_id_endereco):
            raise ValueError(f"Endereço {bobina.endereco_id_endereco} já está ocupado por outra bobina.")
        if self.__lote_existente(bobina.id_lote):
            raise ValueError(f"Lote {bobina.id_lote} já existe.")
        bobina = Bobina.create(
            bobina.id_lote,
            bobina.cortina_id_codigo,
            bobina.endereco_id_endereco,
            bobina.data_cadastro,
            bobina.metragem
        )
        Historico.create(
            bobina.id_lote,
            user_id,
            bobina.endereco_id_endereco,
            datetime.now().strftime("%Y-%m-%d"),
            'Cadastro',
            bobina.metragem
        )

    def remover_bobina(self, codigo):
        bobina = Bobina.get(codigo)
        if bobina:
            bobina.delete()
        else:
            raise ValueError(f"Bobina com código {codigo} não encontrada.")

    def mover_bobina(self, codigo, novo_endereco, user_id):
        if not self.__endereco_valido(novo_endereco):
            raise ValueError(f"Endereço {novo_endereco} não é válido.")
        if self.__endereco_ocupado(novo_endereco):
            raise ValueError(f"Endereço {novo_endereco} já está ocupado por outra bobina.")
        bobina = Bobina.get(codigo)
        if bobina:
            Historico.create(
                bobina.id_lote,
                user_id,
                bobina.endereco_id_endereco,
                datetime.now().strftime("%Y-%m-%d"),
                'Movimentação de estoque',
                bobina.metragem
            )
            Bobina.update_endereco(bobina.id_lote, novo_endereco)
        else:
            raise ValueError(f"Bobina com código {codigo} não encontrada.")

    def mover_para_producao(self, codigo, user_id):
        bobina = Bobina.get(codigo)
        if bobina:
            Historico.create(
                bobina.id_lote,
                user_id,
                bobina.endereco_id_endereco,
                datetime.now().strftime("%Y-%m-%d"),
                'Produção',
                bobina.metragem
            )
            Bobina.update_endereco(bobina.id_lote, 'Produção')
        else:
            raise ValueError(f"Bobina com código {codigo} não encontrada.")

    def buscar_bobina(self, codigo):
        return Bobina.get(codigo)

    def obter_historico(self, codigo):
        bobina = Bobina.get(codigo)
        if bobina:
            return Historico.get_by_bobina(bobina.id_lote)
        return []
