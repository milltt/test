import flet as ft


def main(page: ft.Page):
    page.title = "Destructive Impact Scanner"

    page.window_width = 400
    page.window_height = 170
    page.window_resizable = False

    page.window_center()
    page.update()

    def check_invite_code(e):
        if invite_code.value:
            invite_code.border_color = "green"
            invite_code.label_style = ft.TextStyle(color="green")

            error_text.value = f"Пригласительный код: {invite_code.value}"
            error_text.color = "green"
            page.update()
        else:
            invite_code.border_color = "red"
            invite_code.label_style = ft.TextStyle(color="red")

            error_text.value = "Обязательное поле"
            error_text.color = "red"
            page.update()

    invite_code = ft.TextField(
        label="Пригласительный код",
        autofocus=True
    )
    enter_button = ft.IconButton(icon=ft.icons.LOGIN, icon_size=35, tooltip="Войти", on_click=check_invite_code)

    invite_row = ft.Row(
        width=400,
        controls=[
            invite_code,
            enter_button
        ]
    )
    error_text = ft.Text()

    page.add(invite_row, error_text)


ft.app(target=main)
