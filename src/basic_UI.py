'''
This is NOT using M3L / GSS and is meant to be a temporary solution until
that system is in place. I need something at this time that I can use to 
test and make sure that the code written so far flows correctly in a GUI
based environment.
'''
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
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty, ListProperty
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

        # Styling: Semi-transparent white background with black text
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
        username_label.pos = (50, 200)  # Initial position (will be animated)
        self.add_widget(username_label)

        # Username TextInput
        self.username = CustomTextInput()
        self.username.hint_text = "Enter your username"
        self.username.pos = (50, 150)  # Initial position (will be animated)
        self.add_widget(self.username)

        # Password Label
        password_label = CustomLabel(
            text='Password:',
            font_size=24,
            size_hint=(None, None),
            size=(200, 40),
            color=(1, 1, 1, 1)  # White text color
        )
        password_label.pos = (50, 100)  # Initial position (will be animated)
        self.add_widget(password_label)

        # Password TextInput
        self.password = CustomTextInput(password=True)
        self.password.hint_text = "Enter your password"
        self.password.pos = (50, 50)  # Initial position (will be animated)
        self.add_widget(self.password)

        # Horizontal BoxLayout for Login and Account Recovery Buttons
        buttons_layout = BoxLayout(
            orientation='horizontal',
            spacing=20,
            size_hint=(None, None),
            size=(300, 60),
            pos=(50, -10)  # Initial position (will be animated)
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
        buttons_layout.pos = (50, -10)  # Initial position (will be animated)
        self.add_widget(buttons_layout)

        # New Account Button
        self.new_account_button = CustomButton(
            text='Create New Account'
        )
        self.new_account_button.size_hint = (None, None)
        self.new_account_button.size = (300, 60)
        self.new_account_button.pos = (50, -80)  # Initial position (will be animated)
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
        Animates the entire LoginScreen to slide in from the left to the center of the window.
        """
        # Define the target position (centered)
        target_x = (Window.width / 2) - (self.width / 2)
        target_y = (Window.height / 2) - (self.height / 2)

        # Set the initial position off-screen to the left
        self.pos = (-self.width, target_y)

        # Create an animation object
        anim = Animation(x=target_x, duration=1, t='out_cubic')  # 'out_cubic' easing curve

        # Start the animation
        anim.start(self)
        print("Animation started: LoginScreen sliding in from the left.")

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
                root_bg = RoundedRectangle(pos=root.pos, size=root.size, radius=[0,])
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

        # Centered LoginScreen using RelativeLayout
        relative_layout = RelativeLayout(
            size_hint=(1, 1)
        )
        print("RelativeLayout created for positioning LoginScreen.")

        login_screen = LoginScreen()
        relative_layout.add_widget(login_screen)
        print("LoginScreen added to RelativeLayout.")

        root.add_widget(relative_layout)
        print("RelativeLayout added to root FloatLayout.")

        # Schedule the animation to start after the UI is built
        Clock.schedule_once(lambda dt: login_screen.animate_login_screen(), 0.5)

        return root

    def on_start(self):
        # Automatically focus on the Username field when the app starts
        Clock.schedule_once(self.focus_username, 1.0)  # Adjusted to align with animation timing
        print("Application started. Scheduling focus on username field.")

    def focus_username(self, dt):
        try:
            # Access the RelativeLayout, which is the first child of FloatLayout
            relative_layout = self.root.children[-1]  # FloatLayout's last child is RelativeLayout
            print(f"RelativeLayout children count: {len(relative_layout.children)}")
            if relative_layout.children:
                # Access the LoginScreen, which is the first child of RelativeLayout
                login_screen = relative_layout.children[-1]  # RelativeLayout's last child is LoginScreen
                print("Accessing LoginScreen to set focus on username field.")
                login_screen.username.focus = True
            else:
                print("RelativeLayout has no children to set focus on.")
        except Exception as e:
            print(f"Error in focus_username: {e}")

    def update_canvas(self, instance, value):
        """
        Updates the background rectangle position and size when the window is resized or moved.
        """
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size


if __name__ == '__main__':
    LoginApp().run()
