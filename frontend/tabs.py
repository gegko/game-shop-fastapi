import flet as ft
from data import get_categories_data
from product_grid import product_grid


async def fake_tabs(selected: int = 0) -> ft.Tabs:
    categories_count = len(await get_categories_data())

    async def on_change(e: ft.ControlEvent):
        tab = e.page.controls[0]
        tab.content.selected_index = e.control.selected_index
        await e.page.update_async()

    return ft.Tabs(
        width=400,
        height=30,
        label_color=ft.colors.BLACK,
        unselected_label_color=ft.colors.GREY_300,
        divider_color=ft.colors.TRANSPARENT,
        indicator_color=ft.colors.TRANSPARENT,
        selected_index=selected,
        on_change=on_change,
        tabs=[
            ft.Tab(
                tab_content=ft.Icon(
                    name=ft.icons.MINIMIZE_ROUNDED,
                    size=400 / (categories_count * 2) + 5,
                )
            )
            for _ in range(categories_count)
        ],
    )


async def tab_content(
    tab_id: int,
    category_image_path: str,
    category_name: str
) -> ft.Container:
    return ft.Container(
        width=400,
        height=200,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.START,
            spacing=20,
            controls=[
                ft.Container(
                    ft.Image(category_image_path),
                    alignment=ft.alignment.center,
                    height=180,
                    width=400,
                ),
                ft.Column(
                    spacing=10,
                    controls=[
                        # await fake_tabs(tab_id),
                        ft.Divider(
                            thickness=1, color=ft.colors.BLACK54, opacity=.1
                        ),
                        await product_grid(category_name),
                    ],
                )
            ],
        ),
    )


async def tabs() -> ft.Tabs:
    tabs = ft.Tabs(
        tabs=[
            ft.Tab(
                text=category_name,
                content=await tab_content(
                    tab_id=tab_id,
                    category_image_path=category_image_path,
                    category_name=category_name,
                )
            )
            for tab_id, (category_name, category_image_path)
            in enumerate(await get_categories_data())
        ],
    )
    return tabs
