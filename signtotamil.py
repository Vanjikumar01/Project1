from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

KV = '''
Screen:
    BoxLayout:
        orientation: "vertical"
        spacing: "10dp"
        padding: "10dp"

        MDTextField:
            id: tvmsg
            hint_text: "Type your message..."
            multiline: True

        GridLayout:
            cols: 2
            spacing: "10dp"

            BoxLayout:
                spacing: "10dp"
                size_hint_y: None
                height: "60dp"

                Image:
                    source: "images/a.png"  
                    size_hint_x: None
                    width: "60dp"

                MDRaisedButton:
                    text: "வணக்கம்!"
                    on_release: app.on_button_click("வணக்கம்! (Hello!)")

            BoxLayout:
                spacing: "10dp"
                size_hint_y: None
                height: "60dp"

                Image:
                    source: "images/b.png"  
                    size_hint_x: None
                    width: "60dp"

                MDRaisedButton:
                    text: "ம்ம் .."
                    on_release: app.on_button_click("ம்ம் ..(Hmmmm..) ")
            
            BoxLayout:
                spacing: "10dp"
                size_hint_y: None
                height: "60dp"

                Image:
                    source: "images/c.png"  # Example image path
                    size_hint_x: None
                    width: "60dp"

                MDRaisedButton:
                    text: "நான் உன்னை விரும்புகிறேன்."
                    on_release: app.on_button_click("நான் உன்னை விரும்புகிறேன்.(I Love You.)")
            
            BoxLayout:
                spacing: "10dp"
                size_hint_y: None
                height: "60dp"

                Image:
                    source: "images/d.png"  
                    size_hint_x: None
                    width: "60dp"

                MDRaisedButton:
                    text: "நான் உன்னை உண்மையாகவே விரும்புகிறேன்!."
                    on_release: app.on_button_click("நான் உன்னை உண்மையாகவே விரும்புகிறேன்!.(I Really Love You!. )")
            
            BoxLayout:
                spacing: "10dp"
                size_hint_y: None
                height: "60dp"

                Image:
                    source: "images/e.png"  
                    size_hint_x: None
                    width: "60dp"

                MDRaisedButton:
                    text: "பிறகு பார்க்கலாம."
                    on_release: app.on_button_click("பிறகு பார்க்கலாம.(See You Later.)")
            

            # Add more BoxLayouts for each button with image

        MDRaisedButton:
            text: "Send message"
            on_release: app.send_message(tvmsg.text)
'''


class SignToTamilApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_button_click(self, text):
        self.root.ids.tvmsg.text += text

    def send_message(self, message):
        self.root.ids.tvmsg.text = ""
        # Logic to send the message


if __name__ == "__main__":
    SignToTamilApp().run()


class SignToTamilScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Your initialization code here

        # Example initialization code
        self.add_widget(Label(text="Sign to Tamil Screen"))