import random


class Coin:
    def __init__(self):
        self.__sideup = 'Heads'

    def toss(self):
        side = random.randint(0, 1)
        if side == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        return self.__sideup

    def __str__(self):
        return 'Coin side is ' + self.__sideup
