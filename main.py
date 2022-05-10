from mainscreen import MainScreen
from card import Card
from chosen import Chosen
from menuoperations import MenuOperations
from singleton import Singleton
import typer
single_t = Singleton()
ATM = typer.Typer()
@ATM.command()
def run():
    typer.echo(MainScreen.show_welcom_screen())
@ATM.command()
def choose_card(number:int):
    chosen = Chosen()
    if chosen.choose_card(number):
        card = Card(chosen.get_chosen())
        if MainScreen.check_pin(chosen.get_chosen(), card, single_t):
            single_t.log('Вход в систему', True, '')
            MenuOperations.print_menu(card, single_t)
        else:
            single_t.log('Вход в систему', False, ' Неверный пин-код')
            print('Попробуйте ещё раз позже!')

if __name__=="__main__":
    ATM()
# выбор карточки


# если введен несуществующий номер (порядковый) карточки

