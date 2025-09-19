from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class AuthScreen(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "AuthScreen"
        layout = AnchorLayout(
            anchor_x='center', anchor_y='center')
        
        label
        layout.add_widget(button)
        self.add_widget(layout)
