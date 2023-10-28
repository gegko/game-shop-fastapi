import flet as ft
from data import get_products_data


class Counter(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.txt_number = ft.Container(
            ft.Text(
                value="1",
                width=25,
                height=20,
                size=15,
                color=ft.colors.BLACK,
                text_align=ft.TextAlign.CENTER,
            ),
            border=ft.Border(
                ft.BorderSide(1, 'black'),
                ft.BorderSide(1, 'black'),
                ft.BorderSide(1, 'black'),
                ft.BorderSide(1, 'black'),
            ),
            border_radius=6,
        )
        self.row = ft.Row(
            spacing=1,
            alignment=ft.MainAxisAlignment.START,
            controls=[
                ft.Container(
                    padding=ft.padding.only(right=5),
                    on_click=self.minus_click,
                    content=ft.Icon(
                        name=ft.icons.REMOVE_CIRCLE,
                        size=18
                    ),
                ),
                self.txt_number,
                ft.Container(
                    padding=ft.padding.only(left=5),
                    on_click=self.plus_click,
                    content=ft.Icon(
                        name=ft.icons.ADD_CIRCLE,
                        size=18,
                    ),
                ),
            ],
        )
        self.buy_button = ft.ElevatedButton(
            height=22,
            bgcolor=ft.colors.BLACK54,
            on_click=self.change_control,
            content=ft.Row([
                ft.Icon(
                    name=ft.icons.ADD_SHOPPING_CART,
                    color=ft.colors.WHITE,
                    size=15,
                ),
                ft.Text('Buy', color=ft.colors.WHITE)
            ]),
        )

    async def change_control(self, e: ft.ControlEvent):
        self.controls.pop()
        self.controls.append(self.row)
        await self.update_async()

    async def minus_click(self, e: ft.ControlEvent):
        txt_number = self.txt_number.content
        txt_number.value = str(int(txt_number.value) - 1)
        if int(txt_number.value) <= 0:
            txt_number.value = '1'
            self.controls.pop()
            self.controls.append(self.buy_button)
        await self.update_async()

    async def plus_click(self, e: ft.ControlEvent):
        txt_number = self.txt_number.content
        txt_number.value = str(int(txt_number.value) + 1)
        if txt_number.value != '0':
            e.control.disabled = False
            await e.control.update_async()
        await self.txt_number.update_async()

    def build(self):
        return self.buy_button


def product_container(name, image):
    return ft.Card(
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            controls=[
                ft.Image(image, border_radius=10),
                ft.Container(
                    padding=10,
                    content=ft.Column(
                        controls=[
                            ft.Text(name, weight=ft.FontWeight.BOLD),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Text(
                                        value='$25',
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.colors.BLACK54,
                                    ),
                                    Counter(),
                                ],
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )


async def product_grid(category):
    return ft.GridView(
        width=400,
        height=480,
        runs_count=2,
        padding=5,
        controls=[
            product_container(name, image)
            for name, image in await get_products_data(category)
        ],
    )