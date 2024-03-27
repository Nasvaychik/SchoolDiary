from flet import *
import flet

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
    #def Hover(self,e):
        #if self.button.bgcolor != self.hover_color:
           #self.button.bgcolor = self.hover_color
            #self.button.blur=Blur(12, 12, BlurTileMode.MIRROR)
        #else:
            #self.button.bgcolor = 'transparent'
            #self.button.blur = None
        #self.button.update()

    def build(self):
        return self.button

class Sidebar(UserControl):
    def __init__(self):
        super().__init__()
        #self.width = 300
        #self.height = 500
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
                        MenuButton(icons.DASHBOARD_OUTLINED, "Приборные панели", 240,self.bgcolor),
                        MenuButton(icons.PEOPLE_OUTLINE, "Студенты", 240, self.bgcolor),
                        MenuButton(icons.ACCOUNT_BOX_OUTLINED, "Оценки", 240, self.bgcolor),
                        MenuButton(icons.REPORT_OUTLINED, "Проебы", 240, self.bgcolor),
                        MenuButton(icons.SETTINGS_OUTLINED, "Настройки", 240, self.bgcolor)
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
            left = 50,
            top = 50,
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
        self.body.top = max(0, self.body.top + e.delta_y)
        self.body.left = max(0, self.body.top + e.delta_x)
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

    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    page.appbar = flet.AppBar(
        leading=flet.Icon(flet.icons.PALETTE),
        leading_width=40,
        title=flet.Text("NavBar"),
        center_title=False,
        bgcolor='transparent',
        actions=[
            flet.PopupMenuButton(
                items=[
                    flet.PopupMenuItem(text="Item 1"),
                    flet.PopupMenuItem(),  # divider
                    flet.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )
    page.add(flet.Text("Body!"))

flet.app(main)