from flet import *

from views.Register import Register
from views.Login import Login
from views.Reset_Password import ResetPassword
from views.Verifycation import Verify_email, Verify_email_code

def run_app(page: Page):
	page.title = "App"
	page.padding = 0
	page.vertical_alignment = "center"
	page.horizontal_alignment = "center"
	page.window_resizable = False

	def change_route(route) -> None:
		page.views.clear()

		if page.route == "/verification/email":
				page.views.append(
					View(
						route="/verification/email",
						controls=[
							Verify_email(page=page)
						]
					)
				)
				page.update()

		elif page.route == "/verification/email/code":
			page.views.append(
				View(
					route="/verification/email/code",
					controls=[
						Verify_email_code(page=page)
					]
				)
			)
			page.update()

		elif page.route == "/login":
			page.views.append(
				View(
					route="/login",
					controls=[
						Login(page=page)
					]
				)
			)
			page.update()
		
		elif page.route == "/register":
			page.views.append(
				View(
					route="/register",
					controls=[
						Register(page=page)
					]
				)
			)
			page.update()

		elif page.route == "/login/reset_password":
			page.views.append(
				View(
					route="/login/reset_password",
					controls=[
						ResetPassword(page=page)
					]
				)
			)
			page.update()


	page.on_route_change = change_route
	page.go(route="/verification/email/code")
	
if __name__ == "__main__":
	app(target=run_app)