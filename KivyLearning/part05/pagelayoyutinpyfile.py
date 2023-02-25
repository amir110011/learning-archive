import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout


class MyPageLayout(PageLayout):
    def __init__(self,*args ,**kwargs):
        super(MyPageLayout, self).__init__()

        btn1= Button(text="btn1")
        btn2= Button(text="btn2")
        btn3= Button(text="btn3")
        btn4= Button(text="btn4")
        btn5= Button(text="btn5")

        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)
        self.add_widget(btn5)


class TestApp(App):
    def build(self):
        return MyPageLayout()

if __name__ == '__main__':
    TestApp().run()

