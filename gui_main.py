import os
from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from controller import Controller

# kv = Builder.load_file(os.path.join(os.path.dirname(__file__), "interface.kv"))

class Manager(ScreenManager):
    pass

class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = Controller()

    def build(self):
        return self.controller.get_screen()


MyApp().run()
