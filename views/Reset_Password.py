from flet import *


def ResetPassword(page: Page) -> Stack:

	email = TextField(
		hint_text="Enter your email",
		border=InputBorder.NONE,
		bgcolor="transparent",
		filled=False,
		suffix_icon=icons.EMAIL,
		width=350,
		height=50
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
							),

							Container(
								email,
								border=border.all(2, colors.RED),
								border_radius=20,
								padding=5
							),

							Row(
								[
									IconButton(
										icon=icons.NAVIGATE_NEXT_ROUNDED,
										icon_size=30,
										hover_color=colors.RED
									)
								],
								alignment=MainAxisAlignment.END,
								width=350
							)
						],
						spacing=20,
						horizontal_alignment="center",
						alignment="center"
					),
					bgcolor="transparent",
					width=400,
					height=250,
					border_radius=35,
					border=border.all(2, colors.RED_ACCENT_700),
					blur=Blur(10, 10, BlurTileMode.MIRROR),
					alignment=alignment.center
				),
				alignment=alignment.center,
				padding=150
			),

			Row(
				[
					IconButton(
						icon=icons.NAVIGATE_BEFORE_ROUNDED,
						icon_size=30,
						padding=10,
						hover_color=colors.RED
					)
				],
				alignment=MainAxisAlignment.START
			)
		]
	)

	return body