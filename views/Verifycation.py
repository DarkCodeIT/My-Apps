from flet import *


def Verify_email(page: Page) -> Stack:

	def go_verify_code(e):
		page.go("/verification/email/code")

	def validate(e):
		
		if all([email_field.value]):
			next_btn.disabled = False
			page.update()

		else:
			next_btn.disabled = True
			page.update()
	
	email_field = TextField(		
								hint_text="email",
								width=350,
								height=50,
								border_color=colors.ORANGE,
								border_width=2,
								border_radius=20,
								hint_style=TextStyle(
									color=colors.ORANGE_ACCENT
								),
								filled=False,
								text_style=TextStyle(
									color=colors.ORANGE_ACCENT
								),
								on_change=validate)
	
	next_btn = IconButton(
										icon=icons.NAVIGATE_NEXT_ROUNDED,
										icon_color=colors.WHITE,
										icon_size=30,
										on_click=go_verify_code,
										disabled=True
									)

	body = Stack(
		[
			Image(
				src="assets/bg_verify_email.jpg"
			),

			Container(
				Container(
					Column(
						[
							Row(
								[
									Text(
										value="Enter your email",
										weight=FontWeight.W_700,
										style=TextStyle(
											size=24,
											color=colors.ORANGE
										)
									)
								],
								alignment="center"
							),

							email_field,

							Row(
								[
									next_btn
								],
								alignment=MainAxisAlignment.END,
								width=350
							)
						],
						horizontal_alignment="center",
						spacing=50
					),
					width=400,
					height=300,
					bgcolor="transparent",
					blur=Blur(10, 10, BlurTileMode.MIRROR),
					border=border.all(2, colors.RED),
					border_radius=30
				),
				alignment=alignment.center,
				padding=100
			),

			Row(
				[
					IconButton(
						icon=icons.NAVIGATE_BEFORE_ROUNDED,
						icon_size=30,
						icon_color=colors.WHITE
					)
				]
			)
		]
	)
	return body

def Verify_email_code(page: Page) -> Stack:

	next_btn = IconButton(
		icon=icons.NAVIGATE_NEXT_ROUNDED
	)

	code_field = TextField(
								hint_text="896758",
								border=InputBorder.UNDERLINE,
								width=150,
								border_color=colors.BLACK,
								border_width=2,
								border_radius=2,
								hint_style=TextStyle(
									color=colors.WHITE
								)
							)

	body = Stack(
		[
			Image(
				src="assets/bg_verify_email.jpg"
			),

			Container(
				Container(
					Column(
						[
							Row(
								[
									Text(
										value="We send code on your email.",
										color=colors.ORANGE,
									  style=TextStyle(
											size=24,
											weight=FontWeight.BOLD
										)
									)
								],
								alignment="center"
							),

							Row(
								[
									Text(
										value="Please enter your code.",
										color=colors.ORANGE,
										style=TextStyle(
											size=24,
											weight=FontWeight.BOLD
										)
									)
								],
								alignment="center",
							),
							
							code_field,

							Row(
								[
									next_btn
								]
							)
						],
						alignment="center",
						spacing=30,
						horizontal_alignment="center"
					),
					width=400,
					height=300,
					bgcolor="transparent",
					border_radius=35,
					blur=Blur(10, 10, BlurTileMode.MIRROR)
				),
				alignment=alignment.center,
				padding=150
			)	
		]
	)

	return body
