from xml.etree.ElementTree import iselement
import flet as ft


class CustomControls(ft.UserControl):
    def __init__(self, text: str, start_number: int=0) -> None:
        super().__init__()
        self.text = text
        self.counter = start_number
        self.description: ft.Text = ft.Text(value=self.text, text_align=ft.TextAlign.CENTER)
        self.count: ft.Text = ft.Text(value=str(self.counter), text_align=ft.TextAlign.CENTER)
        self.button: ft.ElevatedButton = ft.ElevatedButton(text="Report", on_click=self.increment)

    def increment(self, e: ft.ControlEvent) -> None:
        self.counter += 1
        self.count.value = str(self.counter)
        self.button.disabled = True
        self.update()

    def build(self) -> ft.Row:
        return ft.Row(
            controls=[
                self.description,
                self.button,
                self.count
            ]
        )

def main(page: ft.Page) -> None:
    page.title = "Custom Controls"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 600

    page.add(
        CustomControls(text="Are you gay"),
        CustomControls(text="Like brawl?", start_number=5),
        CustomControls(text="FF is bad", start_number=23)
    )


if __name__ == "__main__":
    ft.app(target=main)