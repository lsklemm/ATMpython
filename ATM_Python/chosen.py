class Chosen:
    """выбор карточки
        нужен для поиска карточки в процессе изменения пин-код или кард-счёта
    """
    chosen = 0

    def set_chosen(self, number: int):
        self.chosen = number

    def get_chosen(self) -> int:
        return self.chosen

    # выбор карты
    def choose_card(self,n) -> bool:

        try:
            if n == 1:
                self.set_chosen(1)
                return True
            elif n == 2:
                self.set_chosen(2)
                return True
            elif n == 3:
                self.set_chosen(3)
                return True
            else:
                print('\t----------Неверный код операции----------')
                return False
        except ValueError:
            print('\t----------Неверный формат ввода----------')
