from flet import *
import flet
import os

width = 720 * 1.6
height = 405 * 1.6

class MenuButton(UserControl):
    def __init__(self,icon,text,width, hover_color):
        super().__init__()
        self.icon = icon
        self.text = text
        self.hover_color = hover_color
        self.button = Container(
            Row([
                Icon(
                  self.icon,
                    color='white',
                    size=16,
                ),
                Text(
                    self.text,
                    color='white',
                    size=16,
                    weight='w600'
                )
            ]),
            width=width,
            bgcolor = self.hover_color,
            padding=padding.only(15,10,0,10),
            border_radius=6,
            #on_hover=self.Hover,
            #animate=Animation(400)
        )

    def build(self):
        return self.button

class Sidebar(UserControl):
    def __init__(self):
        super().__init__()
        self.bgcolor = "#44000000"
        self.menubar = GestureDetector(
            Container(
                Row([
                    Container(
                        width=10,
                        height=10,
                        border_radius=360,
                        bgcolor = 'red',
                    ),
                    Container(
                        width=10,
                        height=10,
                        border_radius=360,
                        bgcolor='yellow',
                    ),
                    Container(
                        width=10,
                        height=10,
                        border_radius=360,
                        bgcolor='green',
                        blur=Blur(12, 12, BlurTileMode.MIRROR),
                    )
                ]),
                height = 40,
                width = 240,
                padding=padding.only(20, 10,0,10),
                bgcolor = self.bgcolor,

            ),
            on_pan_update=self.update_pos,
        )
        self.body = Container(
            Column([
               self.menubar,
               Container(
                   Text(
                        "Menu",
                        color='#999999',
                        size=14,
                        weight='w500'
                    ),
                   padding=padding.only(20),
               ),
                Container(
                    Column([
                        ElevatedButton("Студенты", icons.PEOPLE_OUTLINE, icon_color="white", ),
                        ElevatedButton("Оценки", icons.ACCOUNT_BOX_OUTLINED, icon_color="white"),
                        ElevatedButton("Заметки", icons.REPORT_OUTLINED, icon_color="white"),
                    ]),
                    padding=padding.only(20),
                ),
                Container(
                    Row([
                        Icon(
                            icons.LIGHT_MODE,
                            color='white',
                        ),
                        Switch(
                            value=True,
                            active_color='#999999',
                            on_change=self.Mode_Change,
                        ),
                         Icon(
                                icons.DARK_MODE,
                                color='white',
                        ),
                    ]),
                    padding=padding.only(20),
                )
            ]),
            width = 240,
            height = 500,
            border_radius = 6,
            bgcolor=self.bgcolor,
            blur=Blur(12,12,BlurTileMode.MIRROR),
        )

    def Mode_Change(self,e):
        if e.control.value == True:
            self.bgcolor = "4400000"
        else:
            self.bgcolor="44f4f4f4"
        self.body.bgcolor=self.bgcolor
        self.body.update()

    def update_pos(self,e):
        self.body.update()

    def build(self):
        return self.body

body = Container(
    Stack([
       Image(
           src='assets/bgpic.jpg',
           width = width,
           height = height,
           left=0,
           top=0
       ),
        Sidebar(),
    ]),
    width= width,
    height = height
)

def Students(page:Page):
    r = flet.Row(wrap=True, scroll="always", expand=True)
    page.add(r)

    for i in range(5000):
        r.controls.append(
            flet.Container(
                flet.Text(f"Item {i}"),
                width=100,
                height=100,
                alignment=flet.alignment.center,
                bgcolor=flet.colors.AMBER_100,
                border=flet.border.all(1, flet.colors.AMBER_400),
                border_radius=flet.border_radius.all(5),
            )
        )
    page.update()

def Evaluations(page:Page):
    page.add(
        flet.DataTable(
            width=700,
            bgcolor="yellow",
            border=flet.border.all(2, "red"),
            border_radius=10,
            vertical_lines=flet.border.BorderSide(3, "blue"),
            horizontal_lines=flet.border.BorderSide(1, "green"),
            sort_column_index=0,
            sort_ascending=True,
            heading_row_color=flet.colors.BLACK12,
            heading_row_height=100,
            data_row_color={"hovered": "0x30FF0000"},
            show_checkbox_column=True,
            divider_thickness=0,
            column_spacing=200,
            columns=[
                flet.DataColumn(
                    flet.Text("Column 1"),
                    on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
                ),
                flet.DataColumn(
                    flet.Text("Column 2"),
                    tooltip="This is a second column",
                    numeric=True,
                    on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
                ),
            ],
            rows=[
                flet.DataRow(
                    [flet.DataCell(flet.Text("A")), flet.DataCell(flet.Text("1"))],
                    selected=True,
                    on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                ),
                flet.DataRow([flet.DataCell(flet.Text("B")), flet.DataCell(flet.Text("2"))]),
            ],
        ),
    )

def main(page:Page):
    page.window_max_width = width
    page.window_max_height = height
    page.window_width = width
    page.window_height = height
    page.window_resizable = False
    page.padding = 0
    page.add(
        body
    )

    def route_change (route):
        page.views.clear()
        page.views.append(
            flet.View(
                "/",
                [
                    flet.Sidebar()
                ]
            )
        )

        page.views.append(
            View(
                route='/',
                controls=[
                    ElevatedButton(on_click=lambda _: page.go('/Студенты'))
                ]
            )
        )

    #Студенты
    if page.route == '/Студенты':
        page.views.append(
            View(
                route='/Студенты',
                controls=[
                    ElevatedButton(on_click=lambda _: page.go('/'))
                ]
            )
        )

    page.update()

    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    page.appbar = flet.AppBar(
        leading=flet.Icon(flet.icons.PALETTE),
        leading_width=40,
        title=flet.Text("Помошник черта"),
        center_title=False,
        bgcolor='transparent',
    )
    page.add(flet.Text("Body!"))

flet.app(main)