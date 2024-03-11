from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
import sqlite3
from kivy.properties import ObjectProperty

class RegisterActivity(MDScreen):
    def __init__(self,con=None,cur=None, **kwargs):
        super().__init__(**kwargs)
        self.con = sqlite3.connect('deafdumb.db')
        self.cur = self.con.cursor()
        self.con = con
        self.cur = cur


        # Create login table if not exists
        self.cur.execute('''CREATE TABLE IF NOT EXISTS login (
                                username TEXT PRIMARY KEY NOT NULL,
                                password TEXT,
                                phone TEXT
                            )''')
        self.con.commit()

        self.orientation = "vertical"

        self.add_widget(
            MDLabel(
                text="Register",
                halign="center",
                font_style="H5"
            )
        )

        self.username = MDTextField(hint_text="Username")
        self.add_widget(self.username)

        self.password = MDTextField(hint_text="Password", password=True)
        self.add_widget(self.password)

        self.phone = MDTextField(hint_text="Phone")
        self.add_widget(self.phone)

        self.btn_register = MDRaisedButton(text="Register", on_release=self.register)
        self.add_widget(self.btn_register)

        self.btn_back = MDIconButton(icon="arrow-left", on_release=self.back)
        self.add_widget(self.btn_back)

    def register(self, instance):
        username = self.username.text
        password = self.password.text
        phone = self.phone.text

        try:
            self.cur.execute("INSERT INTO login (username, password, phone) VALUES (?, ?, ?)", (username, password, phone))
            self.con.commit()
            dialog = MDDialog(title="Success", text="Registration Successful")
            dialog.open()
        except sqlite3.IntegrityError:
            dialog = MDDialog(title="Error", text="Username already exists")
            dialog.open()

    def back(self, instance):
        self.manager.current = "login_screen"
