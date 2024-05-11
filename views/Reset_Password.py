from flet import *


def ResetPassword(page: Page):

	email = TextField(
		hint_text="Enter your email",
		
	)

	body = Stack(
		[
			Image(
				src="assets/bg_reset_password.jpg"
			),

			Container(
				Container(
					Column(
						[
							Row(
								[
									Text(
										value="Reset password",
										text_align=TextAlign.CENTER,
										style=TextStyle(
											size=24,
											weight=FontWeight.W_600,
											color=colors.DEEP_ORANGE_200
										)
									),
								],
								alignment="center"
							)
						],
						spacing=20
					),
					bgcolor="transparent",
					width=400,
					height=200,
					border_radius=35,
					border=border.all(2, colors.RED_ACCENT_700),
					blur=Blur(10, 10, BlurTileMode.MIRROR),
					alignment=alignment.center
				),
				alignment=alignment.center,
				padding=150
			)
		]
	)

	page.add(
		body
	)


app(target=ResetPassword)