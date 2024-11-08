'''
This is NOT using M3L / GSS and is meant to be a temporary solution until
that system is in place. I need something at this time that I can use to 
test and make sure that the code written so far flows correctly in a GUI
based environment.
'''

from kivy.app import App
from kivy.uix.widget import Widget

class MainWidget(Widget):
    pass

class UndChainApp(App):
    def build(self) -> MainWidget:
        self.title = "UndChain"
        return MainWidget()

if __name__ == "__main__":
    UndChainApp().run()
