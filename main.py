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
    
    def p():
            txt_name = ft.TextField(label="Your ID")

            page.add(txt_name, ft.ElevatedButton("Show Team"))
    def _top():
        def btn_click(e):
            TextField(label="Your IDewfs")
        top = Container(
            gradient=LinearGradient(
                                begin=alignment.bottom_left,
                                end=alignment.top_right,
                                colors=['lightblue660' , 'lightblue900']
                            ),
            border_radius=35,
            content=Column(
                alignment='center',
                controls=[
                    Row(
                        alignment='center',
                        controls=[
                            TextField(label="Your ID")
                        ]
                    )
                ]
            )
        )
        return top
    
    _c = Container(
                    width=310,
                    height=660,
                    border_radius=35,
                    bgcolor='black',
                    padding=10,
                    content=Stack(
                        width=300,controls=[_top()]
                    )
    )
    page.add(_c)
if __name__ == "__main__":
    ft.app(target=main)
