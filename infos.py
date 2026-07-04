NO_INFO = 0
SOME_INFO = 1
ALL_INFO = 2

class info():
    """
    Class to store information about a letter.
    infoLevel - amount of information known about a letter. Set via module enum.
    """

    infoLevel : int

    def __init__(self, _infoLevel : int) -> None:
        self.infoLevel = _infoLevel

class infoless(info):
    """
    Class to store information about a letter with no information.
    """

    def __init__(self) -> None:
        super().__init__(NO_INFO)

class infopartial(info):
    """
    Class to store information about a letter with some information.
    falseIndicies - list of indicies where the letter is known to not be.
    """

    falseIndicies : list[int]

    def __init__(self) -> None:
        super().__init__(SOME_INFO)
        self.falseIndicies = []

    def markIndex(self, index : int) -> None:
        self.falseIndicies.append(index)

class infofull(info):
    """
    Class to store information about a letter with all information.
    index - index where the letter is known to be. -1 if it is not present in the word.
    """

    index : int

    def __init__(self, index : int) -> None:
        super().__init__(ALL_INFO)
        self.index = index