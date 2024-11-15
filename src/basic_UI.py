'''
This is NOT using M3L / GSS and is meant to be a temporary solution until
that system is in place. I need something at this time that I can use to 
test and make sure that the code written so far flows correctly in a GUI
based environment.
'''
import kivy
import os
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock
from kivy.graphics import Color, RoundedRectangle

kivy.require('2.3.0')  # Ensure the Kivy version is at least 2.3.0


class CustomLabel(Label):
    """
    A custom Label that left-aligns its text.
    """
    def __init__(self, **kwargs):
        super(CustomLabel, self).__init__(**kwargs)
        self.halign = 'left'
        self.valign = 'middle'
        self.text_size = (self.width, None)
        self.bind(size=self.update_text_size)

    def update_text_size(self, *args):
        self.text_size = (self.width, None)


class CustomTextInput(TextInput):
    """
    A custom TextInput that ensures single-line input, handles Tab key navigation,
    and has a semi-transparent frosted glass-like white background with black text.
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

        self.height = 48  # Set height to 48 pixels as per requirement
        self.padding = (10, 10, 10, 10)  # Adjust padding for better vertical centering

        # Reverted Styling: Semi-transparent white background with black text
        self.background_normal = ''  # Remove default background
        self.background_active = ''  # Remove default active background
        self.background_color = (1, 1, 1, 0.3)  # Semi-transparent white for background
        self.foreground_color = (0, 0, 0, 1)  # Black text color for contrast

        # Add Rounded Corners and Enhanced Background
        with self.canvas.before:
            self.bg_color = Color(1, 1, 1, 0.3)  # Match background_color
            self.bg_rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[10, ])  # Rounded corners with radius 10
        self.bind(pos=self.update_bg, size=self.update_bg)

        # Debugging: Confirm that foreground_color is set correctly
        print(f"CustomTextInput initialized with foreground_color: {self.foreground_color}")

    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

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

        # Define Electric Blue color
        self.electric_blue = (0, 0.6, 1, 1)  # Electric Blue RGB

        # Set default background color to Electric Blue
        self.background_normal = ''  # Remove default background
        self.background_active = ''  # Remove default active background
        self.background_color = self.electric_blue  # Set to Electric Blue

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
    The main login screen containing Username and Password fields and multiple buttons.
    """
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 20

        # Username Label
        self.add_widget(CustomLabel(
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
        self.add_widget(CustomLabel(
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

        # Horizontal BoxLayout for Login and Account Recovery Buttons
        buttons_layout = BoxLayout(
            orientation='horizontal',
            spacing=20,
            size_hint=(1, None),
            height=60  # Adjusted height to accommodate buttons
        )

        # Login Button
        self.login_button = CustomButton(
            text='Login'
            # No need to set background_color here; it defaults to Electric Blue
        )
        self.login_button.bind(on_press=self.validate_credentials)
        buttons_layout.add_widget(self.login_button)

        # Account Recovery Button
        self.account_recovery_button = CustomButton(
            text='Recover Account'
            # No need to set background_color here; it defaults to Electric Blue
        )
        self.account_recovery_button.bind(on_press=self.recover_account)
        buttons_layout.add_widget(self.account_recovery_button)

        self.add_widget(buttons_layout)

        # New Account Button
        self.new_account_button = CustomButton(
            text='Create New Account'
            # No need to set background_color here; it defaults to Electric Blue
        )
        self.new_account_button.bind(on_press=self.create_new_account)
        self.add_widget(self.new_account_button)

        print("LoginScreen initialized and widgets added.")

    def validate_credentials(self, instance):
        """
        Validates the entered credentials.
        """
        uname = self.username.text.strip()
        pwd = self.password.text.strip()

        if uname == "admin" and pwd == "password":
            self.login_button.text = "Login Successful!"
            self.login_button.background_color = (0, 0.8, 0, 1)  # Change button color to green
            print("Login successful.")
        else:
            self.login_button.text = "Invalid Credentials"
            self.login_button.background_color = (0.8, 0, 0, 1)  # Change button color to red
            print("Invalid credentials entered.")

        # Reset the button text and color after 2 seconds
        Clock.schedule_once(self.reset_login_button, 2)

    def reset_login_button(self, dt):
        """
        Resets the login button to its original state.
        """
        self.login_button.text = "Login"
        self.login_button.background_color = (0, 0.6, 1, 1)  # Reset to original Electric Blue color
        print("Login button reset.")

    def recover_account(self, instance):
        """
        Placeholder method for account recovery functionality.
        """
        print("Account Recovery Button Pressed")
        # Implement account recovery logic here

    def create_new_account(self, instance):
        """
        Placeholder method for creating a new account.
        """
        print("Create New Account Button Pressed")
        # Implement new account creation logic here


class LoginApp(App):
    def build(self):
        # Ensure the application starts in windowed mode with a predefined size
        Window.fullscreen = False  # Start in windowed mode
        Window.size = (800, 600)  # Set initial window size (width, height)
        Window.set_title("Login Application")  # Optional: Set window title

        # Root layout
        root = FloatLayout()
        print("Root FloatLayout created.")

        # Construct the path to background.png located in ../assets/background.png
        script_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(script_dir, '..', 'assets')
        background_path = os.path.join(assets_dir, 'background.png')  # Ensure correct file name and extension
        background_path = os.path.normpath(background_path)  # Normalize the path

        print(f"Script directory: {script_dir}")
        print(f"Assets directory: {assets_dir}")
        print(f"Background path: {background_path}")

        # Check if the background image exists
        if not os.path.exists(background_path):
            print(f"Background image not found at {background_path}")
            # Optionally, handle the missing image by setting a default color or raising an error
            # For example, you can add a colored background instead
            root.add_widget(Label(
                text='Background Image Missing',
                color=(1, 0, 0, 1),  # Red color
                size_hint=(None, None),
                size=(300, 50),
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                font_size=24
            ))
        else:
            # Background Image with preserved aspect ratio
            background = Image(
                source=background_path,
                allow_stretch=True,
                keep_ratio=True,  # Preserve aspect ratio
                size_hint=(1, 1),
                pos_hint={'center_x': 0.5, 'center_y': 0.5}
            )
            root.add_widget(background)
            print("Background image added to root.")

        # Centered LoginScreen using AnchorLayout
        anchor_layout = AnchorLayout(
            anchor_x='center',
            anchor_y='center'
        )
        print("AnchorLayout created for centering LoginScreen.")

        login_screen = LoginScreen()
        anchor_layout.add_widget(login_screen)
        print("LoginScreen added to AnchorLayout.")

        root.add_widget(anchor_layout)
        print("AnchorLayout added to root FloatLayout.")

        return root

    def on_start(self):
        # Automatically focus on the Username field when the app starts
        Clock.schedule_once(self.focus_username, 0.5)
        print("Application started. Scheduling focus on username field.")

    def focus_username(self, dt):
        try:
            # Access the AnchorLayout, which is the first child of FloatLayout
            anchor_layout = self.root.children[0]  # FloatLayout's first child is AnchorLayout
            print(f"AnchorLayout children count: {len(anchor_layout.children)}")
            if anchor_layout.children:
                # Access the LoginScreen, which is the first child of AnchorLayout
                login_screen = anchor_layout.children[0]  # AnchorLayout's first child is LoginScreen
                print("Accessing LoginScreen to set focus on username field.")
                login_screen.username.focus = True
            else:
                print("AnchorLayout has no children to set focus on.")
        except Exception as e:
            print(f"Error in focus_username: {e}")


if __name__ == '__main__':
    LoginApp().run()
