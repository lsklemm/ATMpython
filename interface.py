import os
from datetime import datetime

from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

from kivymd.uix.screen import MDScreen




class WelcomeScreen(MDScreen):
    controller = ObjectProperty()
    def __init__(self, controller, balance, **kw):
        super().__init__(**kw)
        self.controller = controller
        self.balance = balance
        self.pin_count = 0
        self.death_screen_value = self.controller.death_screen_value





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

        self.not_correct = False


    def set_pin(self, pin):
        self.controller.set_pin(pin)

    def change_pin(self):
        self.controller.change_pin()

    def check_pin(self):
        if self.controller.check_pin():
            self.ids.pin_label.text = '[color=#74B0D8]pin is correct[/color]'
            self.clean_input()
            return 1
        else:
            self.ids.pin_label.text = '[color=#FF0000]Неверный пин-код!\nПовторите попытку[/color]'
            self.pin_count += 1

        if self.pin_count == 3:
            self.ids.pin_label.text = '[color=#FF88FF]bad[/color]'
            self.pin_count = 0
            self.not_correct = True
            return 2




    def clean_input(self):
        self.ids.pin_input.text = ''


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
    """
    Check screen
    """
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller

    def show_check(self):
        check = ''
        check += '[color=#FF9966]---------------------------------------------------[/color]\n'
        check += '[color=#FF9966]                     ЧЕК[/color]\n'
        check += '[color=#FF9966]---------------------------------------------------[/color]\n'
        date = datetime.now()
        check += '[color=#FF9966]Date: ' + date.strftime('%d-%m-%Y') + '[/color]\n'
        check += '[color=#FF9966]Time: ' + date.strftime('%H:%M:%S') +'[/color]\n'
        check += '[color=#FF9966]---------------------------------------------------[/color]\n'

        check += '[color=#FF9966]Operation: ' + self.controller.last_operation + '[/color]\n'
        check += '[color=#FF9966]---------------------------------------------------[/color]\n'

        self.ids.check_label.text = check



class BalanceScreen(MDScreen):
    """
    Card balance screen
    """
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller


    def set_balance(self, byn, usd):
        print(byn, usd)
        self.ids.balance_byn_label.text = '[color=#FF9966]' + byn + '[/color]'
        self.ids.balance_usd_label.text = '[color=#FF9966]' + usd + '[/color]'






class PhoneInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.phone = ''

    def insert_text(self, string, from_undo = False):
        new_text = self.text + string
        if new_text != '':
            if len(new_text) <= 17:
                if len(new_text) == 4:
                    string += ' '
                    TextInput.insert_text(self, string, from_undo = from_undo)
                elif len(new_text) == 7:
                    string += ' '
                    TextInput.insert_text(self, string, from_undo=from_undo)
                elif len(new_text) == 11:
                    string += ' '
                    TextInput.insert_text(self, string, from_undo=from_undo)
                elif len(new_text) == 14:
                    string += ' '
                    TextInput.insert_text(self, string, from_undo=from_undo)
                else:
                    TextInput.insert_text(self, string, from_undo=from_undo)


class TelephonePaymentScreen(MDScreen):
    number = ObjectProperty()
    money = ObjectProperty()
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
    def phone_payment(self):
        number = self.number.text
        money = self.money.text

        self.controller.telephone_payment(number,money)

class PinInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pin = ''

    def insert_text(self, string, from_undo = False):
        new_text = self.text + string
        if new_text != '':
            if len(new_text) <= 4:
                TextInput.insert_text(self, string, from_undo = from_undo)
            # elif len(new_text) == 4:
            #     self.pin = new_text


class CheckChoiceScreen(MDScreen):
    def __init__(self, check_screen, **kw):
        super().__init__(**kw)
        self.check_screen = check_screen

    def check(self):
        self.check_screen.show_check()


class DeathScreen(MDScreen):
    pass

class WarningScreen(MDScreen):
    pass

class ExitScreen(MDScreen):
    pass

class BYNtoUSD(MDScreen):
    money = ObjectProperty()
    def __init__(self,controller, **kw):
        super().__init__(**kw)
        self.controller = controller

    def from_byn_to_usd(self):
        money=self.money.text
        self.controller.fromBUNtoUSD(money)

class USDtoBYN(MDScreen):
    money = ObjectProperty()
    def __init__(self,controller, **kw):
        super().__init__(**kw)
        self.controller = controller
    def from_usd_to_byn(self):
        money = self.money.text
        self.controller.fromUSDtoBUN(money)



Builder.load_file(os.path.join(os.path.dirname(__file__), "interface.kv"))