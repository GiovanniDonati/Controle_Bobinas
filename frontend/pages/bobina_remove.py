# pages/bobina_remove.py
import flet as ft
import requests

# Importe BACKEND_URL do arquivo principal (main.py)
from frontend.pages.config import BACKEND_URL

def page_bobina_remover(page: ft.Page):
    page.title = "Remover Bobina"

    lote_field = ft.TextField(label="Lote da Bobina")
    remover_button = ft.ElevatedButton(
        text="Remover", on_click=lambda e: remover_bobina_submit(page, lote_field)
    )
    voltar_button = ft.ElevatedButton(text="Voltar", on_click=lambda e: page.go("/"))

    page.add(
        ft.Column(
            [
                ft.Text("Remover Bobina", size=20, weight=ft.FontWeight.BOLD),
                lote_field,
                remover_button,
                voltar_button,
            ]
        )
    )

def remover_bobina_submit(page: ft.Page, lote_field):
    try:
        response = requests.delete(f'{BACKEND_URL}/bobinas/{lote_field.value}')
        response.raise_for_status()
        page.snack_bar = ft.SnackBar(ft.Text("Bobina removida com sucesso!"))
        lote_field.value = ""  # Limpar o campo após a remoção
        page.update()  # Atualizar a página para refletir o campo limpo
    except requests.exceptions.RequestException as e:
        page.snack_bar = ft.SnackBar(ft.Text(f"Erro ao remover bobina: {e}"))
    page.open_snack_bar()
