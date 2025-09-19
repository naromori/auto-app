from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class HomeScreen(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "HomeScreen"
        layout = AnchorLayout(
            anchor_x='center', anchor_y='center')
        
        button = Button(text="Wsp, ppl")
        layout.add_widget(button)
        self.add_widget(layout)
