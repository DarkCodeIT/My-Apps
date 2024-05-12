from flet import *

from style.CustomField import InputField


def Verify_email(page: Page) -> Stack:
	

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
										value="Enter your email"
									)
								]
							)
						]
					),
					width=400,
					height=500,
					bgcolor="transparent",
					blur=Blur(10, 10, BlurTileMode.MIRROR),
					border=border.all(2, colors.RED),
					border_radius=30
				),
				alignment=alignment.center,
				padding=100
			)
		]
	)
	page.add(
		body
	)

app(target=Verify_email)