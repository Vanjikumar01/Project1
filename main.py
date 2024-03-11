# main.py

# Import the correct class name from the correct file
from signtotamil import SignToTamilScreen

# Other necessary imports
import sqlite3
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton

from loginactivity import LoginActivity
from registeractivity import RegisterActivity
from sendmessage import SendMessageScreen


class MainActivity(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.con = sqlite3.connect('deafdumb.db')
        self.cur = self.con.cursor()
        self.orientation = "vertical"
        self.add_widget(
            Image(
                source="images/deafaction.gif"
            )
        )

        # Create login table if not exists
        self.cur.execute("CREATE TABLE IF NOT EXISTS login(logname TEXT, logpwd TEXT, phone TEXT)")
        self.con.commit()

        # ImageButton for login
        self.btn_login = MDIconButton(icon="login")
        self.btn_login.bind(on_release=self.login)
        self.add_widget(self.btn_login)

    def login(self, instance):
        self.manager.current = "login_screen"


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.primary_hue = "500"
        con = sqlite3.connect('deafdumb.db')
        cur = con.cursor()
        # Create ScreenManager
        screen_manager = ScreenManager()

        # Add screens to ScreenManager
        screen_manager.add_widget(MainActivity(name="main"))
        screen_manager.add_widget(LoginActivity(name="login", con=con, cur=cur))
        screen_manager.add_widget(LoginActivity(name="login_screen", con=con, cur=cur))
        screen_manager.add_widget(RegisterActivity(name="register", con=con, cur=cur))
        screen_manager.add_widget(SignToTamilScreen(name="sign_to_tamil"))
        screen_manager.add_widget(SendMessageScreen(name="send_message"))

        return screen_manager


if __name__ == "__main__":
    MyApp().run()
