from ..database.config import get_connection
from models.bobina import Bobina

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