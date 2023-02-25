from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class Layout(App):

    def build(self):
        layout = GridLayout(cols=3, row_force_default=True,
                            row_default_height=50)
        layout2 = GridLayout(cols=2)
        layout2.add_widget(Button(text="btn"))
        layout2.add_widget(Button(text="btn"))
        layout2.add_widget(Button(text="btn"))
        layout2.add_widget(Button(text="btn"))

        layout.add_widget(layout2)
        layout.add_widget(Button(text="btn2"))
        layout.add_widget(Button(text="btn4"))
        layout.add_widget(Button(text="btn1", size_hint_x=None, width=100))
        layout.add_widget(Button(text="btn5"))
        layout.add_widget(Button(text="btn1", size_hint_x=None, width=100))
        layout.add_widget(Button(text="btn6"))

        return layout


# run the App
if __name__ == '__main__':
    Layout().run()
