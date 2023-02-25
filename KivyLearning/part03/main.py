from math import e
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MainGridLayout(GridLayout):
    def calc(self,event):
        if event:
            try:
                self.display.text = str(eval(event))
            except:
                self.display.text("error")
        else:
            self.display.text("error")

class TestApp(App):
    def build(self):
        return MainGridLayout()

kv = TestApp()
kv.run()
