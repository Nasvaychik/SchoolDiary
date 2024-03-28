import flet as ft
import os

width = 720 * 1.6
height = 405 * 1.6


class Sidebar(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.bgcolor = "#44000000"
        self.menubar = ft.GestureDetector(
            ft.Container(
                ft.Row([
                    ft.Container(
                        width=10,
                        height=10,
                        border_radius=360,
                        bgcolor='red',
                    ),
                    ft.Container(
                        width=10,
                        height=10,
                        border_radius=360,
                        bgcolor='yellow',
                    ),
                    ft.Container(
                        width=10,
                        height=10,
                        border_radius=360,
                        bgcolor='green',
                        blur=ft.Blur(12, 12, ft.BlurTileMode.MIRROR),
                    )
                ]),
                height=40,
                width=240,
                padding=ft.padding.only(20, 10,0,10),
                bgcolor=self.bgcolor,

            ),
            on_pan_update=self.update_pos,
        )
        self.body = ft.Container(
            ft.Column([
                self.menubar,
                ft.Container(
                   ft.Text(
                        "Menu",
                        color='#999999',
                        size=14,
                        weight='w500'
                    ),
                   padding=ft.padding.only(20),
                ),
                ft.Container(
                    ft.Column([
                        ft.ElevatedButton(text="Студенты", icon=ft.icons.PEOPLE_OUTLINE, icon_color="white", on_click=lambda _: page.go("/Students")),
                        ft.ElevatedButton(text="Оценки", icon=ft.icons.ACCOUNT_BOX_OUTLINED, icon_color="white"),
                        ft.ElevatedButton(text="Заметки", icon=ft.icons.REPORT_OUTLINED, icon_color="white"),
                    ]),
                    padding=ft.padding.only(20),
                ),
                ft.Container(
                    ft.Row([
                        ft.Icon(
                            ft.icons.LIGHT_MODE,
                            color='white',
                        ),
                        ft.Switch(
                            value=True,
                            active_color='#999999',
                            on_change=self.Mode_Change,
                        ),
                        ft.Icon(
                                ft.icons.DARK_MODE,
                                color='white',
                        ),
                    ]),
                    padding=ft.padding.only(20),
                )
            ]),
            width=240,
            height=500,
            border_radius=6,
            bgcolor=self.bgcolor,
            blur=ft.Blur(12, 12, ft.BlurTileMode.MIRROR),
        )

    def Mode_Change(self,e):
        if e.control.value == True:
            self.bgcolor = "4400000"
        else:
            self.bgcolor = "44f4f4f4"
        self.body.bgcolor = self.bgcolor
        self.body.update()

    def update_pos(self,e):
        self.body.update()

    def build(self):
        return self.body


def students():
    r = ft.Row(
        wrap=True,
        scroll=ft.ScrollMode.ALWAYS,
        spacing=10,
        run_spacing=10,
        width=width // 2,
    )

    for i in range(5000):
        r.controls.append(
            ft.Container(
                ft.Text(f"Item {i}"),
                width=100,
                height=100,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(1, ft.colors.AMBER_400),
                border_radius=ft.border_radius.all(5),
            )
        )
    return r



def evaluations():
    return ft.DataTable(
        width=700,
        bgcolor="yellow",
        border=ft.border.all(2, "red"),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(3, "blue"),
        horizontal_lines=ft.border.BorderSide(1, "green"),
        sort_column_index=0,
        sort_ascending=True,
        heading_row_color=ft.colors.BLACK12,
        heading_row_height=100,
        data_row_color={"hovered": "0x30FF0000"},
        show_checkbox_column=True,
        divider_thickness=0,
        column_spacing=200,
        columns=[
            ft.DataColumn(
                ft.Text("Column 1"),
                on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
            ),
            ft.DataColumn(
                ft.Text("Column 2"),
                tooltip="This is a second column",
                numeric=True,
                on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
            ),
        ],
        rows=[
            ft.DataRow(
                [ft.DataCell(ft.Text("A")), ft.DataCell(ft.Text("1"))],
                selected=True,
                on_select_changed=lambda e: print(f"row select changed: {e.data}"),
            ),
            ft.DataRow([ft.DataCell(ft.Text("B")), ft.DataCell(ft.Text("2"))]),
        ],
    )


def main(page: ft.Page):
    body = ft.Container(
        ft.Stack([
            ft.Image(
                src='assets/bgpic.jpg',
                width=width,
                height=height,
                left=0,
                top=0
            ),
            Sidebar(page).body,
        ]),
        width=width,
        height=height
    )

    def route_change(e: ft.RouteChangeEvent):
        page.clean()

        if e.route == '/':
            page.controls.append(
                body
            )

        elif e.route == '/Students':
            page.controls.append(
                ft.Row(
                    [
                        ft.Container(
                            Sidebar(page),
                        ),

                        ft.Container(
                            students()
                        )
                    ],
                    scroll=ft.ScrollMode.ALWAYS
                )
            )

    def view_pop(e: ft.ViewPopEvent) -> None:
        page.views.pop()
        top_view: ft.View = page.views[-1]
        page.go(top_view.route)

    page.window_max_width = width
    page.window_max_height = height
    page.window_width = width
    page.window_height = height
    page.window_resizable = False
    page.padding = 0
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go('/')
    page.update()

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("Помошник черта"),
        center_title=False,
        bgcolor='transparent',
    )


if __name__ == '__main__':
    ft.app(main)
