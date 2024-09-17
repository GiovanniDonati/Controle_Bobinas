# pages/bobina_move.py
import flet as ft
import requests

# Importe BACKEND_URL do arquivo principal (main.py)
from frontend.pages.config import BACKEND_URL

def page_bobina_mover(page: ft.Page):
    page.title = "Mover Bobina"

    lote_field = ft.TextField(label="Lote da Bobina")
    novo_endereco_field = ft.TextField(label="Novo Endereço")
    mover_button = ft.ElevatedButton(
        text="Mover",
        on_click=lambda e: mover_bobina_submit(
            page, lote_field, novo_endereco_field
        ),
    )
    voltar_button = ft.ElevatedButton(text="Voltar", on_click=lambda e: page.go("/"))

    page.add(
        ft.Column(
            [
                ft.Text("Mover Bobina", size=20, weight=ft.FontWeight.BOLD),
                lote_field,
                novo_endereco_field,
                mover_button,
                voltar_button,
            ]
        )
    )

def mover_bobina_submit(page: ft.Page, lote_field, novo_endereco_field):
    data = {'novo_endereco': novo_endereco_field.value}
    try:
        response = requests.put(
            f'{BACKEND_URL}/bobinas/{lote_field.value}', json=data
        )
        response.raise_for_status()
        page.snack_bar = ft.SnackBar(ft.Text("Bobina movida com sucesso!"))
        lote_field.value = ""  # Limpar os campos após mover
        novo_endereco_field.value = ""
        page.update()  # Atualizar a página para refletir os campos limpos
    except requests.exceptions.RequestException as e:
        page.snack_bar = ft.SnackBar(ft.Text(f"Erro ao mover bobina: {e}"))
    page.open_snack_bar()

