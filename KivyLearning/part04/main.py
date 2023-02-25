from math import e
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MainGridLayout(GridLayout):
    pass


class TestApp(App):
    def build(self):
        return MainGridLayout()

kv = TestApp()
kv.run()
