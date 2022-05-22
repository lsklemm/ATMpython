import os
from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from controller import Controller

from interface import WelcomeScreen, MenuScreen, MoneyOperations

# kv = Builder.load_file(os.path.join(os.path.dirname(__file__), "interface.kv"))

class Manager(ScreenManager):
    def change_screen(self, name):
        self.current = name

class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = Controller()
        self.sm = Manager()
        self.sm.add_widget(WelcomeScreen(name='welcome_screen', controller = self.controller))
        self.sm.add_widget(MenuScreen(name='menu_screen'))
        self.sm.add_widget(MoneyOperations(name='operations_screen'))



    def build(self):
        #return self.controller.get_screen()
        return self.sm


MyApp().run()
