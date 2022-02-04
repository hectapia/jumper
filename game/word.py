import random

class Word:
    def __init__(self):
        self._list = ["carrot", "abide", "life", "radio", "message", "python", "github", "computer", "facebook", "school",
        "house", "instructor", "land", "constitution", "head", "english", "mouse", "screen", "banana", "clock", "phone", "roof",
        "activity", "feeling", "calendar", "price", "excel", "spoon", "wall", "kingdom", "eternal", "keyboard", "violin", "discipline",
        "guitar", "documents", "jumper", "corporation", "word", "parachute", "game", "table", "funny", "learn", "education", "black","history",
        "coding", "prediction", "random", "agency", "atonement", "windows", "yard", "difficulty", "road", "pathway", "scissor", "decoration"]
        self._initial_word = random.choice(self._list)

    def _length(self):
        blank = []
        for i in range(len(self._initial_word)):
            blank.append(" _")
        return blank

    def _printlist(self, list):
        printblank=""
        for i in list:
            printblank += i
        print(printblank)
        return printblank
