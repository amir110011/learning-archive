from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout



class PopupApp(App):

    def openpop(self , btn):
        lbl= Label(text="this is a pop up")
        btnclosepopup = Button(text="close pop up")
        box = BoxLayout(orientation="vertical")
        box.add_widget(lbl)
        box.add_widget(btnclosepopup)
        popup = Popup(title="test pop up!", content= box)
        popup.open()
        btnclosepopup.bind(on_press= popup.dismiss)


    def build(self):
        btnpopupopen = Button(text="open popup")
        btnpopupopen.bind(on_press= self.openpop)
        return btnpopupopen


# run the App
if __name__ == '__main__':
    PopupApp().run()
