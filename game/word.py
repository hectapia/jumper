from game.terminal_service import TerminalService
# Changes added by Hector Olivares Tapia as result of cse210 assignment #
import random
# I always suggest using the full module like "from random import random"
#  even though you don't use the randint part,I saw that you specify the module
class Word:
    """Behavior: retrieve a random word, and show the length of the random word"""
    def __init__(self):
        #Constructor
        self._list = ["carrot", "abide", "life", "radio", "message", "python", "github", "computer", "facebook", "school",
        "house", "instructor", "land", "constitution", "head", "english", "mouse", "screen", "banana", "clock", "phone", "roof",
        "activity", "feeling", "calendar", "price", "excel", "spoon", "wall", "kingdom", "eternal", "keyboard", "violin", "discipline",
        "guitar", "documents", "jumper", "corporation", "word", "parachute", "game", "table", "funny", "learn", "education", "black","history",
        "coding", "prediction", "random", "agency", "atonement", "windows", "yard", "difficulty", "road", "pathway", "scissor", "decoration"]
        self._initial_word = random.choice(self._list)
        # Changes added by Hector Olivares Tapia as result of cse210 assignment #
        self._terminal_service = TerminalService()         

    def _length(self):
        #to treat the random word as a list
        blank = []
        for i in range(len(self._initial_word)):
            blank.append(" _")
        # Changes added by Hector Olivares Tapia as result of cse210 assignment #    
        hint = f' The word that we are searching for has {i+1} letters.'
        self._terminal_service.write_text(hint)           
        return blank


    def _printlist(self, list):
        #to print the length of the random word, the number of the dashes will the number of the random word letters
        printblank=""
        for i in list:
            printblank += i
        
        # Changes added by Hector Olivares Tapia as result of cse210 assignment #
        self._terminal_service.write_text(printblank)
        j = 0
        for k in range(len(printblank)) :
            if '_' == printblank[k] :
                j += 1
         
        if j != 0 :
            missing_letters = f' Just there are {j} missing letters. Go ahead! ' 
        else:
            missing_letters = f' You did it ^.^ '           
        self._terminal_service.write_text(missing_letters)        
        return printblank
