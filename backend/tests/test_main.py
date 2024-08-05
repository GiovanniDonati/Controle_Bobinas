from datetime import datetime
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from backend.app.models.estoque import Estoque
from backend.app.models.bobina import Bobina

estoque = Estoque()

def criar_bobina():
    id_lote = input("Digite o número do lote: ")
    cortina_id_codigo = input("Digite o código da cortina: ")
    endereco_id_endereco = input("Digite o endereço da bobina: ")
    metragem = float(input("Digite a metragem da bobina: "))
    data_cadastro = datetime.now().strftime("%Y-%m-%d")
    user_id = int(input("Digite o ID do usuário que está cadastrando: "))

    try:
        nova_bobina = Bobina(id_lote, cortina_id_codigo, endereco_id_endereco, data_cadastro, metragem)
        estoque.adicionar_bobina(nova_bobina, user_id)
        print("Bobina criada com sucesso!")
    except ValueError as e:
        print(f"Erro ao criar bobina: {e}")

def remover_bobina():
    lote = input("Digite o lote da bobina a ser removida: ")
    user_id = int(input("Digite o ID do usuário que está removendo: "))
    try:
        estoque.remover_bobina(lote, user_id)
        print("Bobina removida com sucesso!")
    except ValueError as e:
        print(f"Erro ao remover bobina: {e}")

def mover_bobina():
    lote = input("Digite o lote da bobina a ser movida: ")
    novo_endereco = input("Digite o novo endereço da bobina: ")
    user_id = int(input("Digite o ID do usuário que está movendo: "))
    try:
        estoque.mover_bobina(lote, novo_endereco, user_id)
        print("Bobina movida com sucesso!")
    except ValueError as e:
        print(f"Erro ao mover bobina: {e}")

def mover_para_producao():
    lote = input("Digite o lote da bobina a ser movida para produção: ")
    user_id = int(input("Digite o ID do usuário que está movendo: "))
    try:
        estoque.mover_para_producao(lote, user_id)
        print("Bobina movida para produção com sucesso!")
    except ValueError as e:
        print(f"Erro ao mover bobina para produção: {e}")

def visualizar_historico():
    lote = input("Digite o lote da bobina para visualizar o histórico: ")
    historico = estoque.obter_historico(lote)
    if not historico:
        print("Histórico não encontrado")
    else:
        for mov in historico:
            print(f"{mov.tipo_mov} em {mov.date_mov} de {mov.endereco_antigo}")

def main():
    while True:
        print("\n1. Criar Bobina")
        print("2. Remover Bobina")
        print("3. Mover Bobina")
        print("4. Mover Bobina para Produção")
        print("5. Visualizar Histórico de Bobina")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_bobina()
        elif opcao == '2':
            remover_bobina()
        elif opcao == '3':
            mover_bobina()
        elif opcao == '4':
            mover_para_producao()
        elif opcao == '5':
            visualizar_historico()
        elif opcao == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
