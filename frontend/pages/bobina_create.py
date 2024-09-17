# pages/bobina_create.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import flet as ft
import requests

from frontend.pages.config import BACKEND_URL

def page_bobina_creator(page: ft.Page):
    page.title = "Criar Bobina"

    id_lote_field = ft.TextField(label="Lote")
    cortina_id_codigo_field = ft.TextField(label="Código da Cortina")
    endereco_id_endereco_field = ft.TextField(label="Endereço")
    metragem_field = ft.TextField(label="Metragem")
    user_id_field = ft.TextField(label="ID do Usuário")
    criar_button = ft.ElevatedButton(
        text="Criar",
        on_click=lambda e: criar_bobina_submit(
            page,
            id_lote_field,
            cortina_id_codigo_field,
            endereco_id_endereco_field,
            metragem_field,
            user_id_field,
        ),
    )
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
                voltar_button,
            ]
        )
    )

def criar_bobina_submit(
    page: ft.Page,
    id_lote_field,
    cortina_id_codigo_field,
    endereco_id_endereco_field,
    metragem_field,
    user_id_field,
):
    data = {
        'id_lote': id_lote_field.value,
        'cortina_id_codigo': cortina_id_codigo_field.value,
        'endereco_id_endereco': endereco_id_endereco_field.value,
        'metragem': metragem_field.value,
        'user_id': user_id_field.value,
    }
    try:
        response = requests.post(f'{BACKEND_URL}/bobinas', json=data)
        response.raise_for_status()
        page.snack_bar = ft.SnackBar(ft.Text("Bobina criada com sucesso!"))
        # Limpar os campos após a criação
        id_lote_field.value = ""
        cortina_id_codigo_field.value = ""
        endereco_id_endereco_field.value = ""
        metragem_field.value = ""
        user_id_field.value = ""
        page.update()  # Atualizar a página para refletir os campos limpos
    except requests.exceptions.RequestException as e:
        page.snack_bar = ft.SnackBar(ft.Text(f"Erro ao criar bobina: {e}"))
    page.open_snack_bar()
