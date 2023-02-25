from logging import disable
from os import supports_bytes_environ
from typing import OrderedDict
import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        dropdown = DropDown()
        for item in range(4):
            btn = Button(text=f"item {item}", size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        supperbtn = Button(text="dropdown", size_hint=(.3, .1),
                           pos_hint={'x': .35, 'y': .45})
        supperbtn.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance,
                      txt: setattr(supperbtn, 'text', txt))

        return supperbtn


if __name__ == "__main__":
    MyApp().run()
