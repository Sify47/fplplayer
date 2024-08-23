import flet as ft
from flet import *
import requests
import json


url1 = "https://fantasy.premierleague.com/api/bootstrap-static/"

t = requests.get(url1)

response_dict = t.json()
def main(page):
    page.scroll = "auto"

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your ID"
            page.update()
        else:
            
            name = txt_name.value
            url = f"https://fantasy.premierleague.com/api/entry/{name}/event/1/picks/"
            r = requests.get(url)
            data = r.json()
            page.clean()
            def bt(e):
                page.clean()
                main(page)
            page.add(ft.ElevatedButton("Back", on_click=bt ))
            # page.add(ft.Text(f"Id Is: {name}!"))
            for i in data['picks']:
                # print(i['element'])
                for u in response_dict['elements']:
                    if u['id'] == i['element']:
                        imga = u['photo'][:-4]
                        # print(imga)
                    # print(i)
                        img = ft.Image(
                            src=f"https://resources.premierleague.com/premierleague/photos/players/250x250/p{imga}.png",
                            width=100,
                            height=100,
                        )
                        page.add(img)
                        page.add(ft.Text(u['web_name']))
                        # print(u['web_name'])
                        page.add(ft.Text(u['event_points']))
                        page.add(ft.Text(u['now_cost'] / 10))
                        page.update()


            
    txt_name = ft.TextField(label="Your ID")

    page.add(txt_name, ft.ElevatedButton("Show Team", on_click=btn_click))

ft.app(target=main , view=ft.AppView.WEB_BROWSER)
