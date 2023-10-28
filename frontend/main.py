import os
import flet as ft
import flet_fastapi
import uvicorn
from dotenv import load_dotenv
from tabs import tabs

load_dotenv()

WORKDIR = os.getenv("WORKDIR")


async def main(page: ft.Page) -> None:
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    await page.add_async(
        ft.Card(
            width=400,
            height=800,
            content=await tabs(),
            elevation=15,
            surface_tint_color=ft.colors.WHITE,
        )
    )

app = flet_fastapi.app(session_handler=main, assets_dir=f'{WORKDIR}/assets')

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        port=5001
    )
