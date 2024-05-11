from flet import *

from style.CustomField import InputField    

def Register(page: Page):
    # page.padding = 0
    # page.vertical_alignment = "center"
    # page.horizontal_alignment = "center"

    def validate(e):
        if all([username_field.field.value,
               email_field.field.value,
               password_field.field.value
               ]) and checkbox.value:
            register_btn.disabled = False
            page.update()

        else:
            register_btn.disabled = True
            page.update()

    def go_login(e):
        page.go(route="/login")

    def open_dialog(e):
        page.dialog = dialog_policy
        dialog_policy.open = True
        page.update()

    def close_dialog(e):
        dialog_policy.open = False
        page.update()
    
    def confirm_dialog(e):
        dialog_policy.open = False
        checkbox.value = True
        page.update()
    
    #Elements with handler events
    checkbox = Checkbox(
        value=False,
        on_change=validate
    )

    register_btn = ElevatedButton(
        text="Register",
        bgcolor="transparent",
        style=ButtonStyle(
            surface_tint_color={
            MaterialState.DEFAULT : "transparent",
            MaterialState.HOVERED : colors.CYAN_ACCENT_700
            },
            shadow_color="transparent"
        ),
        scale=1.2,
        disabled=True
    )

    username_field = InputField(
        width=350,
        height=50,
        hint_text="username",
        icon=icons.PERSON,
        on_change=validate
        )
    
    email_field = InputField(
        width=350,
        height=50,
        hint_text="email",
        icon=icons.MAIL,
        on_change=validate
        )
    
    password_field = InputField(
        width=350,
        height=50,
        hint_text="password",
        password=True,
        icon=icons.LOCK_CLOCK_ROUNDED,
        on_change=validate
        )
    
    dialog_policy = AlertDialog(
        modal=True,
        title=Text(value="App policy"),
        content=Text(
            value="We can collect all your data.\nAnd sell it other people.\nAre you sure?"
        ),
        actions=[
            TextButton(
                text="Confirm",
                on_click=confirm_dialog
            ),
            TextButton(
                text="Cancel",
                on_click=close_dialog
            )
        ],
        actions_alignment=MainAxisAlignment.END
    )

    #View of register
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
                            ),

                            Row(
                                [
                                    Text(
                                        value='You have account?',
                                        size=17,
                                        weight=FontWeight.W_600
                                    ),

                                    TextButton(
                                        text="Login",
                                        style=ButtonStyle(
                                            color={
                                                MaterialState.DEFAULT : colors.WHITE,
                                                MaterialState.HOVERED : colors.BLUE
                                            },
                                            shadow_color="transparent",
                                            overlay_color="transparent",
                                            padding=0
                                        ),
                                        scale=1.2,
                                        on_click=go_login
                                    )
                                ],
                                alignment="center",
                                spacing=5
                            ),

                            username_field,
                            email_field,
                            password_field,

                            Row(
                                [
                                    checkbox,

                                    TextButton(
                                        text="Do you accept the app's policy?",
                                        style=ButtonStyle(
                                            color={
                                                MaterialState.DEFAULT : colors.WHITE,
                                                MaterialState.HOVERED : colors.BLUE
                                            },
                                            shadow_color="transparent",
                                            overlay_color="transparent"
                                        ),
                                        on_click=open_dialog
                                    )
                                ],
                                alignment=MainAxisAlignment.CENTER
                            ),

                            register_btn
                        ],
                        alignment="center",
                        horizontal_alignment="center",
                        spacing=20
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

    return body