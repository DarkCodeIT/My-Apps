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