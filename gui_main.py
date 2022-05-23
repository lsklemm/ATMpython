import os
from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import NoTransition

from controller import Controller

from interface import WelcomeScreen, PinScreen, MenuScreen, MoneyOperations, MoneyOutScreen, MoneyOutChoiceScreen, ContinueScreen, CheckScreen, MoneyInScreen, BalanceScreen

# kv = Builder.load_file(os.path.join(os.path.dirname(__file__), "interface.kv"))

class Manager(ScreenManager):
    def change_screen(self, name):
        self.current = name

class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = Controller()
        self.sm = Manager(transition=NoTransition())
        bs = BalanceScreen(name='balance_screen', controller=self.controller)
        self.controller.balance_screen = bs
        self.sm.add_widget(WelcomeScreen(name='welcome_screen', controller = self.controller, balance=bs))
        self.sm.add_widget(bs)
        self.sm.add_widget(PinScreen(name='pin_screen', controller=self.controller))
        self.sm.add_widget(MenuScreen(name='menu_screen'))
        self.sm.add_widget(MoneyOutChoiceScreen(name = 'money_out_choice_screen', controller=self.controller))
        self.sm.add_widget(MoneyOutScreen(name='money_out_screen', controller=self.controller))
        self.sm.add_widget(MoneyOperations(name='operations_screen'))
        self.sm.add_widget(ContinueScreen(name='continue_screen'))
        self.sm.add_widget(CheckScreen(name='check_screen'))
        self.sm.add_widget(MoneyInScreen(name='money_in_screen', controller=self.controller))
        self.sm.add_widget(BalanceScreen(name='balance_screen', controller=self.controller))
        self.sm.current = 'welcome_screen'



    def build(self):
        #return self.controller.get_screen()
        return self.sm


MyApp().run()
