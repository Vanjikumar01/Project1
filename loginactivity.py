from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3
from kivymd.toast import toast
from kivy.clock import Clock
from signtotamil import SignToTamilScreen


class LoginActivity(MDScreen):
    def __init__(self, con, cur, **kwargs):
        super().__init__(**kwargs)
        self.con = con
        self.cur = cur

        self.orientation = "vertical"

        # Scroll view for the form
        scroll_view = ScrollView()
        self.form_layout = GridLayout(cols=1, size_hint_y=None)
        self.form_layout.bind(minimum_height=self.form_layout.setter('height'))
        scroll_view.add_widget(self.form_layout)
        self.add_widget(scroll_view)

        # Username Field
        self.username = MDTextField(hint_text="Username", size_hint_y=None, height=48)
        self.form_layout.add_widget(self.username)

        # Password Field
        self.password = MDTextField(hint_text="Password", size_hint_y=None, height=48, password=True)
        self.form_layout.add_widget(self.password)

        # Login Button
        self.login_button = MDIconButton(icon="login", pos_hint={"center_x": 0.45})
        self.login_button.bind(on_release=self.login)
        self.add_widget(self.login_button)

        # Register Button
        self.register_button = MDIconButton(icon="account-plus", pos_hint={"center_x": 0.55})
        self.register_button.bind(on_release=self.register)
        self.add_widget(self.register_button)

    def login(self, instance):
        username = self.username.text
        password = self.password.text

        self.cur.execute("SELECT * FROM login WHERE logname=? AND logpwd=?", (username, password))
        user = self.cur.fetchone()
        if user:
            self.show_welcome_message()
            # Schedule calling SignToTamil screen after 3 seconds
            Clock.schedule_once(self.call_sign_to_tamil, 3)
        else:
            show_toast("Invalid Login")

    def show_welcome_message(self):
        # Create and add welcome label in center
        welcome_label = MDLabel(text="Welcome, User!", halign="center", valign="middle")
        self.add_widget(welcome_label)

    def call_sign_to_tamil(self, dt):
        # Remove welcome label after 3 seconds
        for widget in self.children[:]:
            if isinstance(widget, MDLabel):
                self.remove_widget(widget)
        # Change to SignToTamil screen
        self.manager.current = "sign_to_tamil"

    def register(self, instance):
        self.manager.current = "register"


def show_toast(text):
    toast = MDLabel(text=text, halign="center")
    toast.open()


class RegisterActivity(MDScreen):
    def __init__(self, con, cur, **kwargs):
        super().__init__(**kwargs)
        self.con = con
        self.cur = cur

        self.orientation = "vertical"

        # Scroll view for the form
        scroll_view = ScrollView()
        self.form_layout = GridLayout(cols=1, size_hint_y=None)
        self.form_layout.bind(minimum_height=self.form_layout.setter('height'))
        scroll_view.add_widget(self.form_layout)
        self.add_widget(scroll_view)

        # Username Field
        self.username = MDTextField(hint_text="Username", size_hint_y=None, height=48)
        self.form_layout.add_widget(self.username)

        # Password Field
        self.password = MDTextField(hint_text="Password", size_hint_y=None, height=48, password=True)
        self.form_layout.add_widget(self.password)

        # Confirm Password Field
        self.confirm_password = MDTextField(hint_text="Confirm Password", size_hint_y=None, height=48, password=True)
        self.form_layout.add_widget(self.confirm_password)

        # Register Button
        self.register_button = MDIconButton(icon="account-plus", pos_hint={"center_x": 0.5})
        self.register_button.bind(on_release=self.register)
        self.add_widget(self.register_button)

    def register(self, instance):
        username = self.username.text
        password = self.password.text
        confirm_password = self.confirm_password.text

        if password != confirm_password:
            show_toast("Passwords do not match")
            return

        self.cur.execute("INSERT INTO login (logname, logpwd) VALUES (?, ?)", (username, password))
        self.con.commit()
        show_toast("Registration Successful")



class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.primary_hue = "500"

        # Initialize database connection and cursor
        con = sqlite3.connect('deafdumb.db')
        cur = con.cursor()

        screen_manager = ScreenManager()
        screen_manager.add_widget(LoginActivity(con, cur, name="login"))
        screen_manager.add_widget(RegisterActivity(con, cur, name="register"))
        screen_manager.add_widget(SignToTamilScreen(name="sign_to_tamil"))


        return screen_manager


if __name__ == "__main__":
    MyApp().run()