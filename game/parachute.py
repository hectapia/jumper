
class Parachute:
    """The role of this class is to show the parachute picture
    based on how well the user responds correctly"""

    def __init__(self):
        """constructor: a list of lines"""
        # The symbols are used for the game graph 
        # is that a syntax for it ?

        # Identifying sensible variables and converting them in private guarantee
        # an execution without risks of unpredictable changes into their values.
        # added by Hector Olivares  Tapia.
        self.__line1 = "  / \  "
        self.__line2 = "  /!\  "
        self.__line3 = "   o   "
        self.__line4 = "  \ /  "
        self.__line5 = " \   / "
        self.__line6 = "  ___  "
        self.__line7 = ' /   \ '
        self.__line8 = "  ___  "
        self.__line = [self.__line8, self.__line7, self.__line6, self.__line5, self.__line4, self.__line3, self.__line2, self.__line1] 

    def _show(self,check):
        """to print the list of lines depending on the parameter called check,
        this check is an imaginary score or result of how well the user respond correctly, 
        if the answer is correct, the parachute will print a new line at the top unless that imaginary score is still equal to 8,
        if the answer is not correct, the parachute will not print the top line"""

        #when the check is equal to 3, it will be game over and the self._line3 will turns into "  x  "
        if check == 3:
            self.__line[5] = "  x  "
        for i in range(8):
            if i <= (7 - check):
                continue
            print(self.__line[i])
            