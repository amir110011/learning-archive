from logging import disable
import kivy
from kivy.app import App
from kivy.core import text
from kivy.core.text import markup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class Test(App):
    def build(self):

        btn = Button(size_hint=(0.5, 0.2), pos_hint={
                     'x': 0.35, 'y': 0.35}, background_normal="subs.png", background_down="subsBLUE.png", disabled=True)  # size 0-1 , disabled option for disable button

        return btn


if __name__ == "__main__":
    Test().run()
