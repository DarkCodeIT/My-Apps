import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 350
    page.window_height = 650

    first_name = ft.TextField(label="First name", width=225, autofocus=True)
    last_name = ft.TextField(label="Last name", width=225)
    email = ft.TextField(label="Email", width=225)
    password = ft.TextField(label="Password", width=225, password=True, can_reveal_password=True)

    view = ft.Container(content=ft.Column(controls=[
        first_name,
        last_name,
        email,
        password
    ],
    alignment=ft.MainAxisAlignment.CENTER),
    width=300,
    height=400,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=[ft.colors.DEEP_PURPLE_50, ft.colors.AMBER_100]
    ),
    alignment=ft.alignment.center,
    border_radius=35,
    )

    page.add(
        view
    )
    page.update()


if __name__ == "__main__":
    ft.app(target=main)