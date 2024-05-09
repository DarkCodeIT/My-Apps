from flet import *


class InputField(UserControl):
    def __init__(self, width: int, height: int, hint_text: str, icon):
        super().__init__()
        self.width = width
        self.height = height
        self.hint_text = hint_text
        self.icon = icon

        self.field = Container(
            Row([
                TextField(
                    hint_text=self.hint_text,
                    border=None,
                    bgcolor = "transparent"
                ),
                self.icon
            ]),
            width=self.width,
            height=self.height,
            bgcolor="transparent",
            border=border.all(1, "blue")
        )



    def build(self):
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
                        size=24,
                        weight=FontWeight.BOLD
                    )
                ], horizontal_alignment="center"),

                width=400,
                height=500,
                border_radius=20,
                border=border.all(1,"blue"),
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