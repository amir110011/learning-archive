from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class MyFloatLayout(FloatLayout):
    pass

class TestApp(App):
    def build(self):
        return MyFloatLayout()

kv = TestApp()
kv.run()
