import yaml


answers : list[str] = []
options : list[str] = []

gameSize : int


def openWords() -> bool:

    """
    Opens and reads the answers and options files to load them to lists.
    Returns True if successful, False if lists are invalid (word lists should have equal length across all lines).
    """

    global answers, options, gameSize

    config = {}
    answersPath = ""
    optionsPath = ""

    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
        f.close()
    answersPath = config.get("answersPath", "")
    optionsPath = config.get("optionsPath", "")

    with open(answersPath, "r") as f:
        answers = f.read().splitlines()
        f.close()

    with open(optionsPath, "r") as f:
        options = f.read().splitlines()
        f.close()
    
    gameSize = len(answers[0])

    for answer in answers:
        if len(answer) != gameSize:
            answers = []
            options = []
            return False
    
    for option in options:
        if len(option) != gameSize:
            answers = []
            options = []
            return False

    return True