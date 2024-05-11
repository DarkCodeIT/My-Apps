from flet import *

from views.Register import Register
from views.Login import Login
from views.Reset_Password import ResetPassword

def run_app(page: Page):
	page.title = "App"
	page.padding = 0
	page.vertical_alignment = "center"
	page.horizontal_alignment = "center"
	page.window_resizable = False

	def change_route(route) -> None:
		page.views.clear()

		if page.route == "/login":
			page.views.append(
				View(
					route="/login",
					controls=[
						Login(page=page)
					]
				)
			)
			page.update()
		
		if page.route == "/register":
			page.views.append(
				View(
					route="/register",
					controls=[
						Register(page=page)
					]
				)
			)
			page.update()

		if page.route == "/login/reset_password":
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
	page.go(route="/login")
	
if __name__ == "__main__":
	app(target=run_app)