from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MainLayout(GridLayout):
    pass

class TestApp(App):
    def build(self):
        return MainLayout()

kv = TestApp()
kv.run()
