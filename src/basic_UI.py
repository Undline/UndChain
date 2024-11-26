'''
basic_UI.py

This script creates a Kivy-based login application with the following features:
- Gradient background with an optional background image.
- Login interface with Username and Password fields.
- Buttons for Login, Account Recovery, and Creating a New Account.
- Full-screen toggle functionality using the F12 key only.
- Presentation mode to display key presses using the FeedbackLabel system.
- Visual feedback for user actions.
- Robust error handling and dynamic UI adjustments.

Directory Structure:
project/
│
├── assets/
│   └── background.png  # Ensure this image exists
│
└── src/
    └── basic_UI.py
'''

import kivy
import os
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty, ListProperty, NumericProperty
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.animation import Animation
from kivy.uix.widget import Widget

kivy.require('2.3.0')  # Ensure the Kivy version is at least 2.3.0


class GradientBackground(Widget):
    """
    A widget that renders a vertical linear gradient background using specified color stops.
    """
    # Define color stops as a list of tuples (r, g, b, a)
    color_stops = ListProperty([
        (26/255, 4/255, 28/255, 1),      # Dark Purple
        (40/255, 0/255, 80/255, 1)       # Even Darker Purple
    ])

    def __init__(self, **kwargs):
        super(GradientBackground, self).__init__(**kwargs)
        self.bind(pos=self.update_gradient, size=self.update_gradient, color_stops=self.update_gradient)
        self.update_gradient()

    def update_gradient(self, *args):
        """
        Draws the vertical gradient by layering multiple horizontal rectangles with interpolated colors.
        """
        # Clear previous instructions
        self.canvas.before.clear()

        with self.canvas.before:
            num_rects = 100  # Reduced number for better performance
            for i in range(num_rects):
                # Calculate interpolation factor
                factor = i / (num_rects - 1)
                
                # Interpolate between color stops (linear in this case)
                if factor <= 0.5:
                    # Interpolate between first and second color
                    local_factor = factor / 0.5
                    c1 = self.color_stops[0]
                    c2 = self.color_stops[1]
                else:
                    # Continue with the second color (no further color stops)
                    local_factor = 1
                    c1 = self.color_stops[1]
                    c2 = self.color_stops[1]
                
                interpolated_color = (
                    c1[0] + (c2[0] - c1[0]) * local_factor,
                    c1[1] + (c2[1] - c1[1]) * local_factor,
                    c1[2] + (c2[2] - c1[2]) * local_factor,
                    1  # Full opacity
                )
                
                Color(*interpolated_color)
                rect_y = self.y + i * (self.height / num_rects)
                Rectangle(pos=(self.x, rect_y), size=(self.width, self.height / num_rects))


class FeedbackLabel(Label):
    """
    A custom Label that displays feedback messages with a semi-transparent background,
    positioned at the bottom-right corner.
    """
    def __init__(self, message, bg_color=(0, 0, 0, 0.5), **kwargs):
        super(FeedbackLabel, self).__init__(**kwargs)
        self.text = message
        self.halign = 'right'
        self.valign = 'middle'
        self.text_size = self.size  # Ensures text is right-aligned within the label

        with self.canvas.before:
            # Semi-transparent background with customizable color
            Color(*bg_color)
            self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[10, 10, 10, 10])

        # Bind position and size updates to ensure the background stays aligned
        self.bind(pos=self.update_bg, size=self.update_bg, texture_size=self.update_size)

    def update_bg(self, *args):
        """
        Updates the position and size of the background rectangle to match the label.
        """
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

    def update_size(self, *args):
        """
        Updates the size of the label based on the texture size to dynamically adjust width.
        """
        # Add some padding to the width
        padding = 20
        self.width = self.texture_size[0] + padding
        self.height = self.texture_size[1] + 10  # Add some vertical padding


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

    def __init__(self, password=False, **kwargs):
        super(CustomTextInput, self).__init__(**kwargs)
        self.password = password  # Enable password masking if True
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

        # Styling: Semi-transparent white background with black text
        self.background_normal = ''  # Remove default background
        self.background_active = ''  # Remove default active background
        self.background_color = (1, 1, 1, 0.3)  # Semi-transparent white for background
        self.foreground_color = (0, 0, 0, 1)  # Black text color for contrast

        # Add Rounded Corners and Enhanced Background
        with self.canvas.before:
            Color(1, 1, 1, 0.3)  # Match background_color
            self.bg_rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[10, 10, 10, 10]  # Rounded corners with radius 10
            )
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
        self.electric_blue = (0, 0.6, 1, 1)  # Electric Blue RGBA

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


class LoginScreen(RelativeLayout):
    """
    The main login screen containing Username and Password fields and multiple buttons.
    """
    scale = NumericProperty(1.0)  # Property to handle scaling

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (400, 300)  # Adjust size as needed

        # Initialize child widgets
        # Username Label
        username_label = CustomLabel(
            text='Username:',
            font_size=24,
            size_hint=(None, None),
            size=(200, 40),
            color=(1, 1, 1, 1)  # White text color
        )
        username_label.pos = (50, 200)  # Position relative to LoginScreen
        self.add_widget(username_label)

        # Username TextInput
        self.username = CustomTextInput()
        self.username.hint_text = "Enter your username"
        self.username.pos = (50, 150)  # Position relative to LoginScreen
        self.add_widget(self.username)

        # Password Label
        password_label = CustomLabel(
            text='Password:',
            font_size=24,
            size_hint=(None, None),
            size=(200, 40),
            color=(1, 1, 1, 1)  # White text color
        )
        password_label.pos = (50, 100)  # Position relative to LoginScreen
        self.add_widget(password_label)

        # Password TextInput
        self.password = CustomTextInput(password=True)
        self.password.hint_text = "Enter your password"
        self.password.pos = (50, 50)  # Position relative to LoginScreen
        self.add_widget(self.password)

        # Horizontal BoxLayout for Login and Account Recovery Buttons
        buttons_layout = BoxLayout(
            orientation='horizontal',
            spacing=20,
            size_hint=(None, None),
            size=(300, 60),
            pos=(50, -10)  # Position relative to LoginScreen
        )

        # Login Button
        self.login_button = CustomButton(
            text='Login'
        )
        buttons_layout.add_widget(self.login_button)

        # Account Recovery Button
        self.account_recovery_button = CustomButton(
            text='Recover Account'
        )
        buttons_layout.add_widget(self.account_recovery_button)

        # Add buttons_layout to the LoginScreen
        self.add_widget(buttons_layout)
        print("Buttons layout added to LoginScreen.")

        # New Account Button
        self.new_account_button = CustomButton(
            text='Create New Account'
        )
        self.new_account_button.size_hint = (None, None)
        self.new_account_button.size = (300, 60)
        self.new_account_button.pos = (50, -80)  # Position relative to LoginScreen
        self.add_widget(self.new_account_button)

        # Assign next_widget for Tab navigation
        self.username.next_widget = self.password

        # Bind buttons to their respective methods
        self.login_button.bind(on_press=self.validate_credentials)
        self.account_recovery_button.bind(on_press=self.recover_account)
        self.new_account_button.bind(on_press=self.create_new_account)

        print("LoginScreen initialized and widgets added.")

    def animate_login_screen(self):
        """
        Animates the LoginScreen with a scale-up effect for added visual appeal.
        """
        # Reset scale and opacity
        self.scale = 0.8
        self.opacity = 1

        # Create scale and fade-in animation
        anim = Animation(scale=1.0, duration=1, t='out_back')

        # Start the animation
        anim.start(self)
        print("Animation started: LoginScreen scaling up for presentation.")

    def validate_credentials(self, instance):
        """
        Validates the entered credentials.
        """
        uname = self.username.text.strip()
        pwd = self.password.text.strip()

        if uname == "admin" and pwd == "password":
            print("Login successful.")
            # Animate fade-out
            fade_out = Animation(opacity=0, duration=0.5)
            fade_out.bind(on_complete=lambda anim, widget: self.after_successful_login())
            fade_out.start(self)
        else:
            print("Invalid credentials entered.")
            # Shake the password field
            self.shake_password_field()

    def shake_password_field(self):
        """
        Shakes the password TextInput to indicate invalid credentials.
        """
        password_field = self.password
        original_x, original_y = password_field.pos
        shake_distance = 10  # Pixels to move left and right
        shake_duration = 0.05  # Duration of each shake movement

        # Create a sequence of animations to shake the widget
        anim = Animation(x=original_x - shake_distance, duration=shake_duration) + \
               Animation(x=original_x + shake_distance, duration=shake_duration) + \
               Animation(x=original_x - shake_distance, duration=shake_duration) + \
               Animation(x=original_x + shake_distance, duration=shake_duration) + \
               Animation(x=original_x, duration=shake_duration)
        anim.start(password_field)
        print("Shake animation started on password field.")

    def after_successful_login(self):
        """
        Called after fade-out is complete on successful login.
        """
        # Schedule fade-in after 10 seconds
        Clock.schedule_once(self.fade_in_widgets, 10)
        print("Scheduled fade-in after 10 seconds.")

    def fade_in_widgets(self, dt):
        """
        Fades in all widgets by resetting opacity and re-animating the LoginScreen.
        """
        # Reset opacity to 1
        self.opacity = 1
        print("Opacity reset to 1.")

        # Animate the LoginScreen scaling up again
        self.animate_login_screen()
        print("Animating LoginScreen back into view.")

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
    def __init__(self, **kwargs):
        super(LoginApp, self).__init__(**kwargs)
        self.presentation_mode = False  # Flag to track presentation mode

        # Manually define keycode to name mapping for specific keys
        self.manual_keycode_to_name = {
            292: 'F11',
            293: 'F12',
            13: 'Enter',
            14: 'Backspace',
            29: 'Ctrl',        # Left Ctrl
            3613: 'Ctrl',      # Right Ctrl (verify on your system)
            42: 'Shift',       # Left Shift
            54: 'Shift',       # Right Shift
            56: 'Alt',         # Left Alt
            57: 'AltGr',       # Right Alt
            58: 'CapsLock',
            # Add more keycodes and their corresponding names as needed
        }

    def build(self):
        # Ensure the application starts in windowed mode with a predefined size
        Window.fullscreen = False  # Start in windowed mode
        Window.size = (800, 600)    # Set initial window size (width, height)
        Window.set_title("Login Application")  # Optional: Set window title

        # Root layout
        root = FloatLayout()
        print("Root FloatLayout created.")

        # Add Gradient Background
        gradient = GradientBackground()
        root.add_widget(gradient)
        print("GradientBackground added to root.")

        # Add Background Image Over Gradient with Transparency
        # Adjust the path to your background image as needed
        script_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(script_dir, '..', 'assets')
        background_image_path = os.path.join(assets_dir, 'background.png')  # Ensure correct file name and extension
        background_image_path = os.path.normpath(background_image_path)  # Normalize the path

        if not os.path.exists(background_image_path):
            print(f"Background image not found at {background_image_path}")
            # Optionally, handle missing image by displaying a message or using a default color
            with root.canvas.before:
                Color(0.1, 0.1, 0.1, 1)  # Slightly off-black color
                root_bg = RoundedRectangle(pos=root.pos, size=root.size, radius=[0, 0, 0, 0])
            root.bind(pos=self.update_canvas, size=self.update_canvas)
            root.add_widget(Label(
                text='Background Image Missing',
                color=(1, 0, 0, 1),  # Red color
                size_hint=(None, None),
                size=(300, 50),
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                font_size=24
            ))
        else:
            # Add the background image with partial transparency
            background_image = Image(
                source=background_image_path,
                allow_stretch=True,
                keep_ratio=True,
                size_hint=(1, 1),
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                color=(1, 1, 1, 0.5)  # 0.5 opacity for transparency
            )
            root.add_widget(background_image)
            print("Background image added over GradientBackground.")

        # Centered LoginScreen using AnchorLayout
        anchor_layout = AnchorLayout(
            anchor_x='center',
            anchor_y='center',
            size_hint=(1, 1)
        )
        print("AnchorLayout created for positioning LoginScreen.")

        self.login_screen = LoginScreen()
        anchor_layout.add_widget(self.login_screen)
        print("LoginScreen added to AnchorLayout.")

        root.add_widget(anchor_layout)
        print("AnchorLayout added to root FloatLayout.")

        # Removed the debug label section as per user request

        # Bind only the F12 key to toggle full-screen mode and F11 to toggle presentation mode
        Window.bind(on_key_down=self.on_key_down)
        print("Bound F12 and F11 keys for full-screen and presentation mode toggles.")

        # Bind to window size changes to re-center the LoginScreen if needed
        Window.bind(on_resize=self.on_window_resize)
        print("Bound on_resize event to handle window size changes.")

        # Schedule the animation to start after the UI is built
        Clock.schedule_once(lambda dt: self.login_screen.animate_login_screen(), 0.5)

        return root

    def on_window_resize(self, window, width, height):
        """
        Handles window resize events to ensure that the LoginScreen remains centered.
        Replays the start animation for added visual effect.
        """
        print(f"Window resized to width: {width}, height: {height}. Repositioning LoginScreen.")
        # Replay the animation to add fun
        self.login_screen.animate_login_screen()

    def on_key_down(self, window, key, scancode, codepoint, modifiers):
        """
        Handles key press events.
        - F12: Toggles full-screen mode.
        - F11: Toggles presentation mode.
        - Other keys: If in presentation mode, display key presses.
        """
        try:
            # Define keycodes manually based on system (example keycodes)
            F12_KEYCODE = 293  # Adjust based on your system's keycode for F12
            F11_KEYCODE = 292  # Adjust based on your system's keycode for F11

            # Handle F12 key for full-screen toggle
            if key == F12_KEYCODE:
                if Window.fullscreen != 'auto':
                    Window.fullscreen = 'auto'
                    print("Switched to full-screen mode (auto) using F12 key.")
                    self.show_feedback("Full-Screen Mode (F12)")
                else:
                    Window.fullscreen = False
                    print("Switched to windowed mode using F12 key.")
                    self.show_feedback("Windowed Mode (F12)")

            # Handle F11 key for presentation mode toggle
            elif key == F11_KEYCODE:
                self.presentation_mode = not self.presentation_mode
                mode = "ON" if self.presentation_mode else "OFF"
                print(f"Presentation Mode toggled {mode} using F11 key.")
                self.show_feedback(f"Presentation Mode {mode} (F11)")

            # Handle other keys in presentation mode
            elif self.presentation_mode:
                # Exclude certain keys from being displayed
                excluded_keys = ['F11', 'F12', 'Tab', 'Enter', 'Shift', 'Ctrl', 'Alt', 'CapsLock']

                if codepoint:
                    # Display the character as typed, preserving case
                    display_text = f"{codepoint}"
                    self.show_feedback(display_text)
                else:
                    # Attempt to get the key name from manual mapping
                    key_name = self.manual_keycode_to_name.get(key, 'Unknown')
                    if key_name not in excluded_keys:
                        display_text = f"{key_name}"
                        self.show_feedback(display_text)

        except AttributeError as e:
            print(f"Error in on_key_down: {e}")
        except Exception as e:
            print(f"Unexpected error in on_key_down: {e}")

        return False  # Allow other handlers to process the event

    def show_feedback(self, message, bg_color=(0, 0, 0, 0.5)):
        """
        Displays a temporary label with the given message at the bottom-right corner of the window,
        with a semi-transparent background and slight margins.
        """
        feedback_label = FeedbackLabel(
            message=message,
            bg_color=bg_color,
            size_hint=(None, None),
            size=(300, 50),
            pos_hint={'right': 0.95, 'y': 0.05},  # Positioned near bottom-right
            color=(1, 1, 1, 1),  # White text color
            font_size=24,
        )
        self.root.add_widget(feedback_label)
        
        # Animate the label to fade out over 2 seconds
        anim = Animation(opacity=0, duration=2)
        anim.bind(on_complete=lambda anim, widget: self.root.remove_widget(feedback_label))
        anim.start(feedback_label)
        print(f"Displayed feedback: {message}")

    def on_start(self):
        """
        Called when the application starts. Sets focus to the username text box.
        """
        # Schedule focus after a short delay to ensure all widgets are loaded
        Clock.schedule_once(self.focus_username, 1.0)
        print("Application started. Scheduling focus on username field.")

    def focus_username(self, dt):
        """
        Sets focus to the username text box.
        """
        try:
            print(f"Login Screen Reference: {self.login_screen}")
            print(f"Username TextInput Reference: {self.login_screen.username}")
            self.login_screen.username.focus = True
            print("Username text box focused.")
        except AttributeError as e:
            print(f"Error focusing username: {e}")

    def update_canvas(self, instance, value):
        """
        Updates the background rectangle position and size when the window is resized or moved.
        """
        # This method is only bound if the background image is missing
        try:
            self.bg_rect.pos = instance.pos
            self.bg_rect.size = instance.size
        except AttributeError:
            # bg_rect does not exist
            pass


if __name__ == '__main__':
    LoginApp().run()
