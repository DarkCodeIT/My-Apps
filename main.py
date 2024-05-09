from flet import *


class InputField(Stack):
    def __init__(self, width: int = 0, height: int = 0, hint_text: str = "", icon: icons = None, password: bool = False):
        super().__init__()
        self.width = width
        self.height = height
        self.hint_text = hint_text
        self.password = password
        self.icon = icon

        self.field = Container(
            Row([
                TextField(
                    hint_text=self.hint_text,
                    border=InputBorder.NONE,
                    suffix_icon=self.icon,
                    bgcolor = "transparent",
                    color = "white",
                    filled=False,
                    password=self.password,
                    cursor_color=colors.CYAN_ACCENT_200,
                    hint_style=TextStyle(
                        color="blue"
                    ))
                ],
                alignment=MainAxisAlignment.SPACE_AROUND),
            width=self.width,
            height=self.height,
            bgcolor="transparent",
            border=border.all(1, colors.BLUE_400),
            border_radius=20
        )

    def build(self) -> Container:
        return self.field


def main(page: Page):
    # page.window_width = 420
    # page.window_height = 640
    page.window_resizable = False
    page.padding = 0
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    body = Stack([
        Image(
            src="assets/bg_login.jpg"
        ),
        Container(
            Container(
                Column([
                    Text(
                        value="Login",
                        size=30,
                        weight=FontWeight.W_500,
                        color= colors.WHITE70
                    ),

                    InputField(
                        width=350,
                        height=50,
                        hint_text="username | email",
                        icon=icons.PERSON_ROUNDED
                    ),

                    InputField(
                        width=350,
                        height=50,
                        hint_text="password",
                        password=True,
                        icon=icons.LOCK_ROUNDED
                    )
                ],
                    horizontal_alignment="center",
                    alignment="center",
                    spacing=20),

                width=400,
                height=400,
                border_radius=20,
                border=border.all(1, colors.CYAN_ACCENT_400),
                bgcolor="transparent",
                blur=Blur(10,10 ,BlurTileMode.MIRROR)

            ),
            alignment=alignment.center,
            padding=padding.only(top=100)
        )
    ])

    page.add(
        body
    )


if __name__ == "__main__":
    app(target=main)