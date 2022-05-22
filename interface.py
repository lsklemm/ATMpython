import os
from kivy.lang import Builder

from kivy.uix.textinput import TextInput

from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty



class WelcomeScreen(MDScreen):
    controller = ObjectProperty()
    def __init__(self, controller, balance, **kw):
        super().__init__(**kw)
        self.controller = controller
        self.balance = balance
        self.pin_count = 0





    def set_phone_number(self, phone):
        self.controller.set_phone_number(phone)

    def change_widget_text(self, widget, text):
        self.ids.widget.text = text

    def card_operations(self):
        self.controller.set_screen('card operations')

    def choose_card(self, number):
        self.balance.card = self.controller.choose_card(number)









    def telephone_payment(self):
        self.controller.telephone_payment('+375 25 234 10 23',5)

    def fromBUNtoUSD(self):
        self.controller.fromBUNtoUSD()


class PinScreen(MDScreen):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.pin_count = 0


    def set_pin(self, pin):
        self.controller.set_pin(pin)

    def change_pin(self):
        self.controller.change_pin()

    def check_pin(self):
        if self.controller.check_pin():
            self.ids.pin_label.text = '[color=#FF88FF]pin is correct[/color]'
        else:
            self.ids.pin_label.text = '[color=#FF88FF]try one more time[/color]'
            self.pin_count += 1
        if self.pin_count == 3:
            self.ids.pin_label.text = '[color=#FF88FF]bad[/color]'
            self.pin_count = 0


class MenuScreen(MDScreen):
    pass

class MoneyOutChoiceScreen(MDScreen):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller

    def set_money(self, money):
        if self.controller.set_money(money) == False:
            self.ids.money_out_label.text = '[color=#FF9900]the money input is not what i wanted[/color]'
        else:
            self.ids.money_out_label.text = '[color=#FF9900]okeyy[/color]'
            self.controller.money_out()

    def money_out(self):
        self.controller.money_out()


class MoneyOutScreen(MDScreen):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller


    def set_money(self, money):
        if self.controller.set_money(money) == False:
            self.ids.money_out_label.text = '[color=#FF9900]the money input is not what i wanted[/color]'
        else:
            self.ids.money_out_label.text = '[color=#FF9900]okeyy[/color]'

    def money_out(self):
        self.controller.money_out()



class MoneyInScreen(MDScreen):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller

    def set_money(self, money):
        if self.controller.set_money(money) == False:
            self.ids.money_in_label.text = '[color=#FF9900]the money input is not what i wanted[/color]'
        else:
            self.ids.money_in_label.text = '[color=#FF9900]okeyy[/color]'

    def money_in(self):
        self.controller.money_in()


class MoneyOperations(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)





class ContinueScreen(MDScreen):
    pass

class CheckScreen(MDScreen):
    pass


class BalanceScreen(MDScreen):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.card = 0


        # self.ids.balance_byn_label.text = '[color=#FF9966]' + self.controller.get_card_balance_byn() + '[/color]'
        # self.ids.balance_usd_label.text = '[color=#FF9966]' + self.controller.get_card_balance_usd() + '[/color]'

    def byn(self):
        self.byn = '[color=#FF9966]' + self.controller.get_card_balance_byn() + '[/color]'
        return '[color=#FF9966]' + self.controller.get_card_balance_byn() + '[/color]'






class PhoneInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.phone = ''

    def insert_text(self, string, from_undo = False):
        new_text = self.text + string
        if new_text != '':
            if len(new_text) < 17:
                TextInput.insert_text(self, string, from_undo = from_undo)
            elif len(new_text) == 17:
                self.phone = new_text




Builder.load_file(os.path.join(os.path.dirname(__file__), "interface.kv"))