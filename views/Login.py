from flet import *

from style.CustomField import InputField

def login(page: Page):
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
                    ),

                    Row(
                        [
                            Checkbox(
                                label="Remember me",
                                label_style=TextStyle(
                                    size=12
                                ),
                                value=False
                                
                            ),
                            TextButton(
                                text="Forgot password?",
                                style=ButtonStyle(
                                    color={
                                        MaterialState.DEFAULT : colors.WHITE,
                                        MaterialState.HOVERED : colors.BLUE
                                    }
                                )
                            )
                        ],
                        alignment=MainAxisAlignment.SPACE_AROUND
                    ),

                    Row(
                        [
                            ElevatedButton(
                                text="Login",
                                bgcolor="transparent",
                                style=ButtonStyle(
                                    color={
                                        MaterialState.DEFAULT : colors.WHITE,
                                        MaterialState.HOVERED : colors.BLUE
                                    },
                                    shadow_color="transparent"
                                ),
                                scale=1.2
                            )
                        ],
                        alignment="center"
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
    app(target=login)