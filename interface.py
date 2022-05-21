import os
from kivy.lang import Builder


from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty



class WelcomeScreen(MDScreen):
    controller = ObjectProperty()
    def __init__(self, controller, **kw):
        super().__init__(**kw)
        self.controller = controller
        self.pin_count = 0

    def set_pin(self, pin):
        self.controller.set_pin(pin)

    def change_widget_text(self, widget, text):
        self.ids.widget.text = text

    def card_operations(self):
        self.controller.set_screen('card operations')

    def choose_card(self, number):
        self.controller.choose_card(number)

    def check_pin(self):
        if self.controller.check_pin():
            self.ids.label.text = '[color=#FF88FF]eq[/color]'
        else:
            self.ids.label.text = '[color=#FF88FF]try one more time[/color]'
            self.pin_count += 1
        if self.pin_count == 3:
            self.ids.label.text = '[color=#FF88FF]bad[/color]'
            self.pin_count = 0



    def money_out(self):
        self.controller.money_out(10)

    def money_in(self):
        self.controller.money_in(10)

    def telephone_payment(self):
        self.controller.telephone_payment('+375 25 234 10 23',5)

    def fromBUNtoUSD(self):
        self.controller.fromBUNtoUSD(5)

class MoneyOperations(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)




Builder.load_file(os.path.join(os.path.dirname(__file__), "interface.kv"))