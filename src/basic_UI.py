'''
This is NOT using M3L / GSS and is meant to be a temporary solution until
that system is in place. I need something at this time that I can use to 
test and make sure that the code written so far flows correctly in a GUI
based environment.
'''

import kivy
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock

kivy.require('2.3.0')  # Ensure the Kivy version is at least 2.3.0


class CustomTextInput(TextInput):
    """
    A custom TextInput that ensures single-line input and handles Tab key navigation.
    """
    next_widget = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(CustomTextInput, self).__init__(**kwargs)
        self.multiline = False  # Ensure single-line input
        self.size_hint_x = None  # Disable automatic width sizing
        self.size_hint_y = None  # Disable automatic height sizing
        self.font_size = 24  # Set font size

        # Set a reasonable fixed width based on character count
        # Approximate average character width: 0.6 * font_size
        avg_char_width = 0.6 * self.font_size
        self.width = avg_char_width * 24  # 0.6 * 24 = 14.4; 14.4 * 24 ≈ 345 pixels
        self.width = 350  # Rounded to 350 pixels for simplicity

        self.height = 48  # Default height
        self.padding = (10, 8, 10, 8) 

        # Optional Styling
        self.background_normal = ''  # Remove default background
        self.background_active = ''  # Remove default active background
        self.background_color = (1, 1, 1, 0.1)  # Light background color with some transparency
        self.foreground_color = (1, 1, 1, 1)  # White text color

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        """
        Overrides the keyboard_on_key_down method to handle Tab and Enter key presses.
        """
        if keycode[1] == 'tab':
            if self.next_widget:
                self.next_widget.focus = True  # Shift focus to the next widget
            return True  # Indicate that the event has been handled
        elif keycode[1] == 'enter':
            # Trigger the login button's on_press event if defined
            if self.parent and hasattr(self.parent, 'login_button'):
                self.parent.login_button.dispatch('on_press')
            return True  # Indicate that the event has been handled
        return super(CustomTextInput, self).keyboard_on_key_down(window, keycode, text, modifiers)


class CustomButton(Button):
    """
    A custom Button that adjusts its size based on the text it displays, with added margins.
    """
    text = StringProperty('Login')  # Default text

    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        self.size_hint_x = None  # Disable automatic width sizing
        self.size_hint_y = None  # Disable automatic height sizing
        self.font_size = 24  # Set font size
        self.bold = True  # Make text bold

        # Initial sizing
        self.update_size()

        # Bind the text property to update_size whenever it changes
        self.bind(text=self.update_size)

    def update_size(self, *args):
        """
        Updates the size of the button based on the text content, adding margins.
        """
        # Create a temporary Label to calculate the size of the text
        temp_label = Label(text=self.text, font_size=self.font_size, bold=self.bold, size_hint=(None, None))
        temp_label.texture_update()  # Update the texture to get the latest size
        text_width, text_height = temp_label.texture_size

        # Define margins
        margin_x = 40  # Horizontal margin (20 pixels on each side)
        margin_y = 20  # Vertical margin (10 pixels on top and bottom)

        # Set button size based on text size and margins
        self.width = text_width + margin_x
        self.height = text_height + margin_y


class LoginScreen(BoxLayout):
    """
    The main login screen containing Username and Password fields and a Login button.
    """
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 20

        # Username Label
        self.add_widget(Label(
            text='Username:',
            font_size=24,
            size_hint=(1, None),
            height=40,
            color=(1, 1, 1, 1)  # White text color
        ))

        # Username TextInput
        self.username = CustomTextInput()
        self.username.hint_text = "Enter your username"
        self.add_widget(self.username)

        # Password Label
        self.add_widget(Label(
            text='Password:',
            font_size=24,
            size_hint=(1, None),
            height=40,
            color=(1, 1, 1, 1)  # White text color
        ))

        # Password TextInput
        self.password = CustomTextInput(password=True)
        self.password.hint_text = "Enter your password"
        self.add_widget(self.password)

        # Assign next_widget for Tab navigation
        self.username.next_widget = self.password

        # Login Button
        self.login_button = CustomButton(
            text='Login',
            background_color=(0, 0.5, 0.5, 1)  # Initial button color (teal)
        )
        self.login_button.bind(on_press=self.validate_credentials)
        self.add_widget(self.login_button)

    def validate_credentials(self, instance):
        """
        Validates the entered credentials.
        """
        uname = self.username.text.strip()
        pwd = self.password.text.strip()

        if uname == "admin" and pwd == "password":
            self.login_button.text = "Login Successful!"
            self.login_button.background_color = (0, 0.8, 0, 1)  # Change button color to green
        else:
            self.login_button.text = "Invalid Credentials"
            self.login_button.background_color = (0.8, 0, 0, 1)  # Change button color to red

        # Reset the button text and color after 2 seconds
        Clock.schedule_once(self.reset_login_button, 2)

    def reset_login_button(self, dt):
        """
        Resets the login button to its original state.
        """
        self.login_button.text = "Login"
        self.login_button.background_color = (0, 0.5, 0.5, 1)  # Reset to original teal color


class LoginApp(App):
    def build(self):
        # Set the window background color (optional)
        Window.clearcolor = (0.1, 0.1, 0.1, 1)  # Dark background

        # Create an AnchorLayout to center the LoginScreen
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')

        # Add the LoginScreen to the AnchorLayout
        anchor_layout.add_widget(LoginScreen())

        return anchor_layout

    def on_start(self):
        # Automatically focus on the Username field when the app starts
        Clock.schedule_once(self.focus_username, 0.5)

    def focus_username(self, dt):
        # Access the LoginScreen and set focus to the username TextInput
        login_screen = self.root.children[0]  # Assuming LoginScreen is the first child
        login_screen.username.focus = True


if __name__ == '__main__':
    LoginApp().run()
