from interface import WelcomeScreen, MoneyOperations
from kivy.uix.screenmanager import ScreenManager


from mainscreen import MainScreen
from card import Card
from chosen import Chosen
from menuoperations import MenuOperations
from singleton import Singleton
from cardSessions import GiveMoney, GetMoney, ChangePin, Telephone, Currency_transactions
from bankomat import Bankomat



class Controller:
    def __init__(self):
        self.main_screen = WelcomeScreen(controller=self)
        self.money_operations = MoneyOperations()
        self.current_screen = self.main_screen


        self.single_t = Singleton()
        self.storage = Bankomat()
        self.storage.set_storage_byn(10000)
        self.storage.set_storage_usd(1000)

        self.pin = 0
        self.card = 0

    def set_pin(self, pin):
        self.pin = pin

    def check_pin(self):
        if int(self.pin) == int(self.card.get_pin()):
            return True


    def choose_card(self, number):
        chosen = Chosen()
        if chosen.choose_card(number):
            self.card = Card(chosen.get_chosen())
            # card = Card(chosen.get_chosen())
            # card.get_balance_byn()


    def money_out(self, money):
        give_money = GiveMoney()
        print(self.card.get_balance_byn())
        give_money.money_out(self.card, int(money), self.storage, self.single_t, 'BYN', 1)
        print(self.card.get_balance_byn())

    def money_in(self, money):
        print(self.card.get_balance_byn())
        get_money = GetMoney()
        get_money.money_in(self.card, int(money), self.storage, self.single_t, 'BYN', 1)
        print(self.card.get_balance_byn())

    def telephone_payment(self, telephone_number, money):
        print(self.card.get_balance_byn())
        telephone = Telephone()
        telephone.telephone_pay(self.card, int(money), telephone_number, self.storage, self.single_t)
        print(self.card.get_balance_byn())

    def fromBUNtoUSD(self, money):
        print(self.card.get_balance_byn())
        transaction = Currency_transactions()
        transaction.fromBUNtoUSD(self.card, money, 1)
        print(self.card.get_balance_byn())

    def fromUSDtoBUN(self, money):
        print(self.card.get_balance_byn())
        transaction = Currency_transactions()
        transaction.fromUSDtoBUN(self.card, money, 1)
        print(self.card.get_balance_byn())









    def set_screen(self, name):
        if name == 'card operations':
            self.current_screen = self.money_operations
            self.get_screen()


    def get_screen(self):
        return self.current_screen