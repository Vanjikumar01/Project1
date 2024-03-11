from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.popup import Popup


class SendMessageScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.tv = MDLabel(text="", halign="center", size_hint_y=None)
        self.btn = MDRaisedButton(text="Send Message", on_release=self.send_message)
        self.edmobile = MDTextField(hint_text="Recipient's Number", readonly=True)
        self.select_contact_btn = MDRaisedButton(text="Select Contact", on_release=self.select_contact)

        self.add_widget(self.tv)
        self.add_widget(self.btn)
        self.add_widget(self.edmobile)
        self.add_widget(self.select_contact_btn)

    def send_message(self, instance):
        message = self.tv.text
        recipient_number = self.edmobile.text
        if recipient_number:
            # Logic to send the message
            print(f"Sending message: '{message}' to {recipient_number}")
            self.show_toast("Message sent")
        else:
            self.show_toast("Please select a contact first")

    def select_contact(self, instance):
        # Logic to select contact
        print("Selecting contact")

    def show_toast(self, message):
        toast = ToastPopup(message)
        toast.open()


class ToastPopup(Popup):
    def __init__(self, message, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text=message)
        self.add_widget(self.label)


class SendMessageApp(MDApp):
    def build(self):
        return SendMessageScreen()


if __name__ == "__main__":
    SendMessageApp().run()


