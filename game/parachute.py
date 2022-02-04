class Parachute:
    def __init__(self):
        self._line1 = " / \ "
        self._line2 = " /!\ "
        self._line3 = "  o  "
        self._line4 = " \ / "
        self._line5 = "\   /"
        self._line6 = " ___ "
        self._line7 = "/   \ "
        self._line8 = " ___ "
        self._line = [self._line8, self._line7, self._line6, self._line5, self._line4, self._line3, self._line2, self._line1]

    def _show(self,check):
        if check == 3:
            self._line[5] = "  x  "
        for i in range(8):
            if i <= (7 - check):
                continue
            print(self._line[i])


