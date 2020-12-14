from random import randrange
import logging


class Multiply:

    def __init__(self, user_choice=None):
        self.table = user_choice
        self.multiplicateur = self.random_int()
        self.computer_choice = self.random_int()
        self.result = 0

    @staticmethod
    def random_int():
        multiplier = randrange(1, 12)
        return multiplier

    def calculate_result(self, user_menu_choice=None):
        _user_menu_choice = user_menu_choice

        if _user_menu_choice == 1:
            self.result = self.table * self.multiplicateur
            print(f'{self.multiplicateur} * {self.table} = ')
        else:
            self.result = self.computer_choice * self.multiplicateur
            print(f'{self.multiplicateur} * {self.computer_choice} = ')
        return self.result

    def evaluate_result(self, user_answer):
        if user_answer == self.result:
            print(f"***** Hurray ! good answer ! *****")
            print('***********************************')
        else:
            print(f"{user_answer} is a Bad answer !")
            logging.debug(f'Question : {self.multiplicateur} * {self.computer_choice}---Reponse : {user_answer}')


