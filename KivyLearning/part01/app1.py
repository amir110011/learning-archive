from typing import Text
import kivy
from kivy.app import App
from kivy.core import text, window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


class Myapp(App):
    Window.size=(300,500)
    def build(self):
        self.lbl_name = Label(text="inter your name:")
        self.txt_name = TextInput(multiline=False)
        self.lbl_family = Label(text="inter your family:")
        self.txt_family = TextInput(multiline=False)
        self.lbl_country = Label(text="inter your country:")
        self.txt_country = TextInput(multiline=False)
        self.btn_submit = Button(text="submit")
        self.btn_submit.bind(on_press=self.submit)

        box = BoxLayout(orientation='vertical')
        box.add_widget(self.lbl_name)
        box.add_widget(self.txt_name)
        box.add_widget(self.lbl_family)
        box.add_widget(self.txt_family)
        box.add_widget(self.lbl_country)
        box.add_widget(self.txt_country)
        box.add_widget(self.btn_submit)

        return box

    def submit(self,event):
        if (self.txt_name.text != "" and self.txt_family.text != "" and self.txt_country.text != ""):
            print(f"{self.txt_name.text} {self.txt_family.text} {self.txt_country.text}")
            self.btn_submit.disabled= True
            self.btn_submit.text = "thank you!"
        else:
            print("error")



if __name__ == "__main__":
    Myapp().run()
