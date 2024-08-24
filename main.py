import flet as ft
from flet import *
import requests
import json

players_data_url = "https://fantasy.premierleague.com/api/bootstrap-static/"
players_data = requests.get(players_data_url)
players_data = players_data.json()

def main(page : Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.scroll = "auto"
    
    page.add(
        Row(
            [
                Text("HeLLLLLLLLLO")
            ]
        )
    )
if __name__ == "__main__":
    ft.app(target=main)
