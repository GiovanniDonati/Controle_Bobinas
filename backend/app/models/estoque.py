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
        tipo_endereco = []

        for letra in 'ABCD':
            for number in range(1, 96):
                enderecos.append(f'{letra}{number}')
                tipo_endereco.append('Prateleira')

        for number in range(17, 96):
            enderecos.append(f'E{number}')
            tipo_endereco.append('Prateleira')


        for number in range(47, 96):
            enderecos.append(f'F{number}')
            tipo_endereco.append('Prateleira')

        for number in range(82, 96):
            enderecos.append(f'G{number}')
            tipo_endereco.append('Prateleira')

        for letra in 'ABCDE':
            for number in range(1, 5):
                enderecos.append(f'G1-{letra}{number}')
                tipo_endereco.append('Grupos')

        for letra in 'ABCD':
            for number in range(1, 6):
                enderecos.append(f'G2-{letra}{number}')
                tipo_endereco.append('Grupos')

        for letra in 'AB':
            for number in range(1, 12):
                enderecos.append(f'G3-{letra}{number}')
                tipo_endereco.append('Grupos')
                
        for letra in 'AB':
            for number in range(1, 7):
                enderecos.append(f'R-{letra}{number}')
                tipo_endereco.append('Grupos')
        
        for letra in 'AB':
            for number in range(1, 4):
                enderecos.append(f'N-{letra}{number}')
                tipo_endereco.append('Grupos')
        
        def inserir_enderecos():
            try:
                connection = get_connection()
                for endereco, tipo in zip(enderecos, tipo_endereco):
                    with connection.cursor() as cursor:
                        sql = "INSERT INTO endereco (id_endereco, tipo_endereco) VALUES (%s, %s)"
                        cursor.execute(sql, (endereco, tipo)) 
                connection.commit()
                connection.close()
            except ValueError as e:
                print(e)
            
        return enderecos, tipo_endereco

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
            'bobina Nova',
            bobina.metragem
        )

    def remover_bobina(self, lote, user_id):
        bobina = Bobina.get(lote)
        if bobina:
            Historico.create(
                bobina.id_lote,
                user_id,
                bobina.endereco_id_endereco,
                datetime.now().strftime("%Y-%m-%d"),
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
        bobina = Bobina.get(lote)
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
        bobina = Bobina.get(lote)
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
        return Bobina.get(lote)

    def obter_historico(self, lote):
        bobina = Bobina.get(lote)
        if bobina:
            return Historico.get_by_bobina(bobina.id_lote)
        return []

    def obter_bobinas(self):
        return Bobina.get_all()