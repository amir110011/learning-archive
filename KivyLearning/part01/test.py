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
        lbl = Label(text="[color=1b23c4]lable[/color] \naaaa \n[b]bold text[/b] [i]italic[/i]", font_size="50sp", color=[1,1,0,1], markup=True)# color system is RGBA , color for one word or one part is six hegxadesimal number
        txt = TextInput(multiline=False)
        self.txt=txt
        box = BoxLayout(orientation='vertical')
        btn =Button(text="[b]send data[/b]", markup=True,background_color=(0,1,0,1),color=(1,1,1,1),size_hint=(0.5,0.2 ), pos_hint={'x':0.5 , 'y':0.5 })# size 0-1

        btn.bind(on_press=self.press_key)

        box.add_widget(lbl)
        box.add_widget(txt)
        box.add_widget(btn)
        return box

    def press_key(self, event):
        self.txt.text="senfd fstsa"
if __name__ == "__main__":
    Test().run()
