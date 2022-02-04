from game.parachute import Parachute
from game.word import Word


class Director:
    """It has the behavior to start the game"""

    def __init__(self):
        """constructor"""
        self._parachute = Parachute()
        self._word = Word ()       
        self._random_word = self._word._initial_word 
        self._blank_word = ""
        self._user_guess = ""
        self._is_ending = True
        self.check = 8 
        
    def _start_game(self):
        self._blank_word = self._word._length()
        self._word._printlist(self._blank_word)
        self._parachute._show(self.check)
        while self._is_ending:
            print("")
            self._process()

    def _process(self):
        self._user_guess = input("Guess a letter [a-z]: ")
        if self._user_guess in self._random_word and f" {self._user_guess}" not in self._blank_word:
            random_word_indexes = []
            index_start = -1
                        
            while index_start <= len(self._random_word):
                try:
                    index = self._random_word.index(self._user_guess, index_start+1)
                except ValueError:
                    break
                else:
                    random_word_indexes.append(index)
                    index_start = index

            random_word_indexes_length = len(random_word_indexes)

            for i in random_word_indexes:
                self._blank_word[i]=f" {self._user_guess}"
            
            self._word._printlist(self._blank_word)

            if self.check == 8:
                self._parachute._show(self.check)

            elif self.check < 8:
                print("")
                self._parachute._show(self.check+1)
                self.check+=1
        elif f" {self._user_guess}" in self._blank_word:
            print("")
            self._parachute._show(self.check)
            
        else:
            self._word._printlist(self._blank_word)
            print("")
            self._parachute._show(self.check-1)
            self.check-=1

        if self.check == 3 or " _" not in self._blank_word:
            self._is_ending = False
            print("game over")    