from logging import disable
from typing import OrderedDict
import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox

class MyApp(App):
    def build(self):
        supper_box = BoxLayout(orientation='vertical')

        box1 = BoxLayout(orientation='horizontal')
        ch1 = CheckBox(active=True, disabled=True)
        lbl1 = Label(text="choice 1")
        box1.add_widget(ch1)
        box1.add_widget(lbl1)

        box2 = BoxLayout(orientation='horizontal')
        ch2 = CheckBox()
        lbl2 = Label(text="choice 2")
        box2.add_widget(ch2)
        box2.add_widget(lbl2)

        supper_box.add_widget(box1)
        supper_box.add_widget(box2)

        return supper_box

if __name__ == "__main__":
    MyApp().run()
