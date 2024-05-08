import flet as ft


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    first_name = ft.TextField(label="First name", width=300)
    last_name = ft.TextField(label="Last name", width=300)
    email = ft.TextField(label="Email", width=300)
    password = ft.TextField(label="Password", width=300, password=True)

    page.add(
        ft.Column(controls=[
            first_name,
            last_name,
            email,
            password
        ]
        )
    )
    page.update()


if __name__ == "__main__":
    ft.app(target=main)