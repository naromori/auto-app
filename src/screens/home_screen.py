from kivymd.uix.screen import MDScreen
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.label import MDLabel

class HomeScreen(MDScreen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "HomeScreen"
        layout = MDAnchorLayout(
            anchor_x='center', anchor_y='center')
        
        label = MDLabel(
            text='Home Page',
            pos_hint={'center_x': 0.5, 'y': 0.3}
        )

        button = MDButton(
            MDButtonText(
                text='Login',
                pos_hint={'center_x': 0.5, 'center_y': 0.5 }
            )
        )

        layout.add_widget(label)
        layout.add_widget(button)
        self.add_widget(layout)
