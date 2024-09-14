from flet import *
import requests

def main(page : Page):
    page.title = "FPL"
    page.scroll = 'auto'
    # page.window.top = 1
    # page.window.left = 960
    page.window.width = 390
    page.window.height = 740
    
    
    ID = TextField(label="Your ID" , input_filter=NumbersOnlyInputFilter() , border_color=colors.BLACK , border_width=2 , focused_border_color=colors.YELLOW_ACCENT)
    players_url = "https://fantasy.premierleague.com/api/bootstrap-static/"

    p = requests.get(players_url)
    
    Players_data = p.json()
    
    def btn_click(e):
            if not ID.value:
                ID.error_text = "Please enter your ID"
                page.update()
            
            else:
                
                name = ID.value
                manger = f"https://fantasy.premierleague.com/api/entry/{name}"
                ru = requests.get(manger)
                manger_data = ru.json()
                ev = manger_data['current_event']
                picks = f"https://fantasy.premierleague.com/api/entry/{name}/event/{ev}/picks/"
                r = requests.get(picks)
                picks_data = r.json()
                tt=[]
                for i in picks_data['picks']:
                    for u in Players_data['elements']:
                        if u['id'] == i['element']:
                            if i['multiplier'] == 0:
                                continue
                            if i['multiplier'] == 2:
                                tt.append(u['event_points'] *2)
                                continue
                            tt.append(u['event_points'])
                                
                page.clean()
                
                def bt(e):
                    page.clean()
                    pages(e)
                page.add(
                    Container(
                        Row(
                            [
                                ElevatedButton("Back", on_click=bt)
                            ],
                            alignment=MainAxisAlignment.START
                        ),
                    ),
                )
                page.add(
                        Card(
                                        content=Container(
                                            content=Column(
                                                [
                                                    ListTile(
                                                        title=Text(manger_data['name'] , size=32),
                                                        subtitle = Text(f"Rank: {manger_data['summary_overall_rank']}" , size=14),
                                                        title_alignment=ListTileTitleAlignment.CENTER,
                                                        horizontal_spacing =2
                                                    ),
                                                    Row(
                                                        [Text(
                                                            f"Points: {sum(tt)}",
                                                            size=25,
                                                        )],
                                                        alignment=MainAxisAlignment.CENTER,
                                                    ),
                                                ]
                                            ),
                                            border=border.all(1 , colors.YELLOW_ACCENT),
                                            width=400,
                                            padding=10,
                                            gradient=LinearGradient(
                                                begin=alignment.bottom_left,
                                                end=alignment.top_right,
                                                colors=["#1e293b" , "#475569"]
                                            ),
                                            border_radius=15
                                        )
                                    )
                                )

                page.add(
                    Row(
                        [
                            Text("START" , size=20),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    )
                )
                for i in picks_data['picks']:
                    for u in Players_data['elements']:
                        if u['id'] == i['element'] and (i['multiplier'] == 1 or i['multiplier'] == 2):
                            imga = u['photo'][:-4]
                            if i['multiplier'] == 2:
                                page.add(
                                    Card(
                                        content=Container(
                                            content=Column(
                                                [
                                                    ListTile(
                                                        leading=Icon(icons.CYCLONE_ROUNDED),
                                                        title=Image(src=f"https://resources.premierleague.com/premierleague/photos/players/250x250/p{imga}.png" , width=250 , height=250),
                                                        title_alignment=alignment.center,
                                                        horizontal_spacing =2
                                                    ),
                                                    Row(
                                                        [Text(
                                                            u['web_name'],
                                                            size=40,
                                                        )],
                                                        alignment=MainAxisAlignment.CENTER,
                                                    ),
                                                    Row(
                                                        [Text(
                                                            f"{u['event_points'] * 2}  |  {u['now_cost'] / 10}",
                                                            size=30,
                                                        )],
                                                        alignment=MainAxisAlignment.CENTER,
                                                    ),
                                                ]
                                            ),
                                            width=400,
                                            padding=10,
                                            gradient=LinearGradient(
                                                begin=alignment.bottom_left,
                                                end=alignment.top_right,
                                                colors=["#1e293b" , "#475569"]
                                            ),
                                            border_radius=15
                                        )
                                    )
                                )
                                continue
                            page.add(
                                    Card(
                                        content=Container(
                                            content=Column(
                                                [
                                                    ListTile(
                                                        # leading=Icon(icons.CYCLONE_ROUNDED),
                                                        title=Image(src=f"https://resources.premierleague.com/premierleague/photos/players/250x250/p{imga}.png" , width=250 , height=250),
                                                        title_alignment=alignment.center,
                                                        horizontal_spacing =2
                                                    ),
                                                    Row(
                                                        [Text(
                                                            u['web_name'],
                                                            size=40,
                                                        )],
                                                        alignment=MainAxisAlignment.CENTER,
                                                    ),
                                                    Row(
                                                        [Text(
                                                            f"{u['event_points']}  |  {u['now_cost'] / 10}",
                                                            size=30,
                                                        )],
                                                        alignment=MainAxisAlignment.CENTER,
                                                    ),
                                                ]
                                            ),
                                            # border=border.all(2 , colors.YELLOW_ACCENT),
                                            width=400,
                                            padding=10,
                                            gradient=LinearGradient(
                                                begin=alignment.bottom_left,
                                                end=alignment.top_right,
                                                colors=["#1e293b" , "#475569"]
                                            ),
                                            border_radius=15
                                        )
                                    )
                                )
                            page.update()
                page.add(
                    Row(
                        [
                            Text("Substiutes" , size=20),
                        ],
                        alignment=MainAxisAlignment.CENTER
                    )
                )
                for i in picks_data['picks']:
                    for u in Players_data['elements']:
                        if u['id'] == i['element'] and i['multiplier'] == 0:
                            imga = u['photo'][:-4]
                            page.add(
                                Card(
                                    content=Container(
                                        content=Column(
                                            [
                                                ListTile(
                                                    leading=Icon(icons.HIDE_SOURCE_OUTLINED),
                                                    title=Image(src=f"https://resources.premierleague.com/premierleague/photos/players/250x250/p{imga}.png" , width=250 , height=250),
                                                    title_alignment=alignment.center,
                                                    horizontal_spacing =2
                                                ),
                                                Row(
                                                    [Text(
                                                        u['web_name'],
                                                        size=40,
                                                    )],
                                                    alignment=MainAxisAlignment.CENTER,
                                                ),
                                                Row(
                                                    [Text(
                                                        f"{u['event_points']}  |  {u['now_cost'] / 10}",
                                                        size=30,
                                                    )],
                                                    alignment=MainAxisAlignment.CENTER,
                                                ),
                                            ]
                                        ),
                                        width=400,
                                        padding=10,
                                        gradient=LinearGradient(
                                            begin=alignment.bottom_left,
                                            end=alignment.top_right,
                                            colors=["#1e293b" , "#475569"]
                                        ),
                                        border_radius=15
                                    )
                                )
                            )
                            page.update()
                
    def btn(e):
        page.clean()
        name = ID.value
        manger = f"https://fantasy.premierleague.com/api/entry/{name}"
        ru = requests.get(manger)
        manger_data = ru.json()
        ev = manger_data['current_event']
        picks = f"https://fantasy.premierleague.com/api/entry/{name}/event/1/picks/"
        r = requests.get(picks)
        picks_data = r.json()
        page.clean()
        def back(e):
            page.clean()
            pages(e)
        page.add(
                    Container(

                        content=Column(
                            [TextButton(text="Back" , on_click=back , icon_color=colors.YELLOW_ACCENT)]
                        ),
                        width=390,
                        height=30,
                        alignment=alignment.top_left,
                    ),
        )
        page.add()
        page.add(
                        Card(
                                        content=Container(
                                            content=Column(
                                                [
                                                    ListTile(
                                                        title=Text(manger_data['name'] , size=35),
                                                        subtitle = Text(f"Rank: {manger_data['summary_overall_rank']}" , size=14),
                                                        title_alignment=ListTileTitleAlignment.CENTER,
                                                        horizontal_spacing =2
                                                    ),
                                                ]
                                            ),
                                            border=border.all(1 , colors.YELLOW_ACCENT),
                                            width=400,
                                            padding=10,
                                            gradient=LinearGradient(
                                                begin=alignment.bottom_left,
                                                end=alignment.top_right,
                                                colors=["#1e293b" , "#475569"]
                                            ),
                                            border_radius=15
                                        )
                                    )
)
        for i in manger_data['leagues']['classic']:
                page.add(
                Card(
                    content=Container(
                        content=Column(
                            [
                                ListTile(
                                    leading=Icon(icons.SPORTS_SOCCER_OUTLINED),
                                    title=Text(i['name'] , size=30),
                                    subtitle=Text(
                                        f"Rank : {i['entry_rank']}" , size=13
                                    ),
                                    title_alignment=alignment.center,
                                    data=i['id']
                                ),
                            ]
                        ),
                        width=400,
                        padding=10,
                        gradient=LinearGradient(
                            begin=alignment.bottom_left,
                            end=alignment.top_right,
                            colors=["#1e293b" , "#475569"]
                        ),
                        border_radius=15
                    ),
                )
            )
        page.update()
    def pages(e):
        page.clean()
        def back(e):
            page.clean()
            main(page)

        page.add(Container(
            Column(
                alignment="center",
                controls=[
                            
                            Row(
                                [
                                    ElevatedButton("Back", on_click=back)                                
                                ],
                                alignment=MainAxisAlignment.START
                            )
                ],
                
            ),
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.bottom_right,
                colors=["#1e293b" , "#475569"]
            ),
            width = 430,
            # height = 700,
            margin=margin.only(bottom=-10)
        ))
        c = Container(
            Column(
                alignment="center",
                controls=[
                            
                            Row(
                                [
                                    ElevatedButton("Show Team", on_click=btn_click , width=300 , height=50 , bgcolor=colors.BLACK87 , color=colors.YELLOW_ACCENT)
                                ],
                                alignment=MainAxisAlignment.CENTER
                            ),
                            Row(
                                [
                                    ElevatedButton("Show Leauge", on_click=btn , width=300 , height=50 , bgcolor=colors.BLACK87 , color=colors.YELLOW_ACCENT)
                                ],
                                alignment=MainAxisAlignment.CENTER
                            ),
                ],
                # alignment=MainAxisAlignment.SPACE_BETWEEN
                
            ),
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=["#1e293b" , "#475569"]
            ),
            width = 430,
            height = 935,
            # margin=margin.all(-10)
        )
        # page.add(
        #         Card(
        #             content=Container(
        #                 content=Column(
        #                     [
        #                         ListTile(
        #                             leading=Icon(icons.SPORTS_SOCCER_OUTLINED),
        #                             title=Text('name', size=30),
        #                             subtitle=Text(
        #                                 f"Rank : " , size=13
        #                             ),
        #                             title_alignment=alignment.center,
        #                             # on_click=pages
        #                         ),
        #                     ]
        #                 ),
        #                 width=400,
        #                 padding=10,
        #                 gradient=LinearGradient(
        #                     begin=alignment.bottom_left,
        #                     end=alignment.top_right,
        #                     colors=["#1e293b" , "#475569"]
        #                 ),
        #                 border_radius=15
        #             ),
        #         ),
        #         Card(
        #             content=Container(
        #                 content=Column(
        #                     [
        #                         ListTile(
        #                             leading=Icon(icons.SPORTS_SOCCER_OUTLINED),
        #                             title=Text('name', size=30),
        #                             subtitle=Text(
        #                                 f"Rank : " , size=13
        #                             ),
        #                             title_alignment=alignment.center,
        #                             # on_click=pages
        #                         ),
        #                     ]
        #                 ),
        #                 width=400,
        #                 padding=10,
        #                 gradient=LinearGradient(
        #                     begin=alignment.bottom_left,
        #                     end=alignment.top_right,
        #                     colors=["#1e293b" , "#475569"]
        #                 ),
        #                 border_radius=15
        #             ),
        #         )
        # )
        page.add(c)
    
    
    
    c = Container(
        Column(
            alignment="center",
            controls=[
                        Row(
                            [
                                ID
                            ],
                            alignment=MainAxisAlignment.CENTER
                        ),
                        Row(
                            [
                                ElevatedButton("Next" , width=300 , height=40 , bgcolor=colors.BLACK87 , color=colors.YELLOW_ACCENT , on_click=pages)
                            ],
                            alignment=MainAxisAlignment.CENTER
                        ),
                        
                        Container(
                            content=Column(
                                
                            )
                        )
            ],
        ),
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=["#1e293b" , "#475569"]
        ),
        alignment=alignment.center,
        width = 430,
        height = 925,
        margin=margin.all(-10)
        # width = 390,
        # height = 700,
        # margin=margin.all(-10)
    )
    
    page.add(c)
    page.update()
    
app(main)
