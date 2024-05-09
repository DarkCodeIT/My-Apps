from flet import *

from style.CustomField import InputField    

def Register(page: Page):
    page.padding = 0
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    body = Stack(
        controls=[
            Image(
                src="assets/bg_register.jpg"
            ),

            Container(
                Container(
                    Column(
                        [
                            Row(
                                [
                                    Text(
                                        value="Register",
                                        style=TextStyle(
                                            size=24,
                                            weight=FontWeight.W_700
                                        )
                                    )
                                ],
                                alignment="center"
                            )
                        ],
                        alignment="center",
                        horizontal_alignment="center"
                    ),
                    width=400,
                    height=500,
                    bgcolor="transparent",
                    blur=Blur(10, 10, BlurTileMode.MIRROR),
                    border_radius=30,
                    border=border.all(1, color=colors.INDIGO_500),
                    
                ),

                alignment=alignment.center,
                padding=padding.only(top=100)
            )
        ]
    )

    page.add(
        body
    )


if __name__ == "__main__":
    app(target=Register)