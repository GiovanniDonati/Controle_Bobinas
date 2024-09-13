import flet as ft

def main(page: ft.Page):
    page.title = "Controle de Bobinas"
    page.window.maximized = False
    page.window.width = 600
    page.window.height = 800
    page.route = "/"

    page.controls.append(ft.ElevatedButton(text="Criar Bobina", on_click=lambda e: page.go("/criar_bobina")))
    page.controls.append(ft.ElevatedButton(text="Remover Bobina", on_click=lambda e: page.go("/remover_bobina")))
    page.controls.append(ft.ElevatedButton(text="Mover Bobina", on_click=lambda e: page.go("/mover_bobina")))
    page.controls.append(ft.ElevatedButton(text="Mover para Produção", on_click=lambda e: page.go("/mover_para_producao")))
    page.controls.append(ft.ElevatedButton(text="Visualizar Histórico", on_click=lambda e: page.go("/visualizar_historico")))
    page.controls.append(ft.ElevatedButton(text="Visualizar Estoque", on_click=lambda e: page.go("/vizualizar_bobinas")))
    page.update()

def criar_bobina(page: ft.Page):
    page.title = "Criar Bobina"
    page.clean()

    id_lote_field = ft.TextField(label="Lote")
    cortina_id_codigo_field = ft.TextField(label="Código da Cortina")
    endereco_id_endereco_field = ft.TextField(label="Endereço")
    metragem_field = ft.TextField(label="Metragem")
    user_id_field = ft.TextField(label="ID do Usuário")
    criar_button = ft.ElevatedButton(text="Criar", on_click=lambda e: criar_bobina_submit(page, id_lote_field, cortina_id_codigo_field, endereco_id_endereco_field, metragem_field, user_id_field))
    voltar_button = ft.ElevatedButton(text="Voltar", on_click=lambda e: page.go("/"))

    page.add(
        ft.Column(
            [
                ft.Text("Criar Bobina", size=20, weight=ft.FontWeight.BOLD),
                id_lote_field,
                cortina_id_codigo_field,
                endereco_id_endereco_field,
                metragem_field,
                user_id_field,
                criar_button,
                voltar_button
            ]
        )
    )
    page.update()

def criar_bobina_submit(page: ft.Page, id_lote_field, cortina_id_codigo_field, endereco_id_endereco_field, metragem_field, user_id_field):
    # Simula a criação da bobina
    page.snack_bar = ft.SnackBar(ft.Text("Bobina criada com sucesso!"))
    page.open_snack_bar()
    page.go("/")

def remover_bobina(page: ft.Page):
    page.title = "Remover Bobina"
    page.clean()

    lote_field = ft.TextField(label="Lote da Bobina")
    remover_button = ft.ElevatedButton(text="Remover", on_click=lambda e: remover_bobina_submit(page, lote_field))
    voltar_button = ft.ElevatedButton(text="Voltar", on_click=lambda e: page.go("/"))

    page.add(
        ft.Column(
            [
                ft.Text("Remover Bobina", size=20, weight=ft.FontWeight.BOLD),
                lote_field,
                remover_button,
                voltar_button
            ]
        )
    )
    page.update()

def remover_bobina_submit(page: ft.Page, lote_field):
    # Simula a remoção da bobina
    page.snack_bar = ft.SnackBar(ft.Text("Bobina removida com sucesso!"))
    page.open_snack_bar()
    page.go("/")

def mover_bobina(page: ft.Page):
    page.title = "Mover Bobina"
    page.clean()

    lote_field = ft.TextField(label="Lote da Bobina")
    novo_endereco_field = ft.TextField(label="Novo Endereço")
    mover_button = ft.ElevatedButton(text="Mover", on_click=lambda e: mover_bobina_submit(page, lote_field, novo_endereco_field))
    voltar_button = ft.ElevatedButton(text="Voltar", on_click=lambda e: page.go("/"))

    page.add(
        ft.Column(
            [
                ft.Text("Mover Bobina", size=20, weight=ft.FontWeight.BOLD),
                lote_field,
                novo_endereco_field,
                mover_button,
                voltar_button
            ]
        )
    )
    page.update()

def mover_bobina_submit(page: ft.Page, lote_field, novo_endereco_field):
    # Simula a movimentação da bobina
    page.snack_bar = ft.SnackBar(ft.Text("Bobina movida com sucesso!"))
    page.open_snack_bar()
    page.go("/")

def mover_para_producao(page: ft.Page):
    page.title = "Mover para Produção"
    page.clean()

    lote_field = ft.TextField(label="Lote da Bobina")
    mover_button = ft.ElevatedButton(text="Mover", on_click=lambda e: mover_para_producao_submit(page, lote_field))
    voltar_button = ft.ElevatedButton(text="Voltar", on_click=lambda e: page.go("/"))

    page.add(
        ft.Column(
            [
                ft.Text("Mover para Produção", size=20, weight=ft.FontWeight.BOLD),
                lote_field,
                mover_button,
                voltar_button
            ]
        )
    )
    page.update()

def mover_para_producao_submit(page: ft.Page, lote_field):
    # Simula a movimentação para produção
    page.snack_bar = ft.SnackBar(ft.Text("Bobina movida para produção com sucesso!"))
    page.open_snack_bar()
    page.go("/")

def visualizar_historico(page: ft.Page):
    page.title = "Visualizar Histórico"
    page.clean()

    lote_field = ft.TextField(label="Lote da Bobina")
    visualizar_button = ft.ElevatedButton(text="Visualizar", on_click=lambda e: visualizar_historico_submit(page, lote_field))
    voltar_button = ft.ElevatedButton(text="Voltar", on_click=lambda e: page.go("/"))

    page.add(
        ft.Column(
            [
                ft.Text("Visualizar Histórico", size=20, weight=ft.FontWeight.BOLD),
                lote_field,
                visualizar_button,
                voltar_button
            ]
        )
    )
    page.update()

def visualizar_historico_submit(page: ft.Page, lote_field):
    # Simula a visualização do histórico
    page.snack_bar = ft.SnackBar(ft.Text("Histórico da bobina: Lote: " + lote_field.value))
    page.open_snack_bar()
    page.go("/")

def vizualizar_bobinas(page: ft.Page):
    page.title = "Estoque de Bobinas"
    page.clean()

    visualizar_button = ft.ElevatedButton(text="Visualizar", on_click=lambda e: vizualizar_bobinas_submit(page))
    voltar_button = ft.ElevatedButton(text="Voltar", on_click=lambda e: page.go("/"))

    page.add(
        ft.Column(
            [
                ft.Text("Estoque de Bobinas", size=20, weight=ft.FontWeight.BOLD),
                visualizar_button,
                voltar_button
            ]
        )
    )
    page.update()

def vizualizar_bobinas_submit(page: ft.Page):
    # Simula a visualização do estoque
    page.snack_bar = ft.SnackBar(ft.Text("Visualizando estoque de bobinas..."))
    page.open_snack_bar()
    page.go("/")

ft.app(target=main)
