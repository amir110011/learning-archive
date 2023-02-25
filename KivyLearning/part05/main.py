import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout


class MyPageLayout(PageLayout):
    pass


class TestApp(App):
    def build(self):
        return MyPageLayout()

if __name__ == '__main__':
    TestApp().run()

