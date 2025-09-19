from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton
from kivymd.uix.anchorlayout import MDAnchorLayout


class AuthScreen(MDScreen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "AuthScreen"
        layout = MDAnchorLayout(
            anchor_x='center', anchor_y='center')
        
        button = MDIconButton(text='Test Button Yay')
        layout.add_widget(button)
