import yaml
import infos
import wordGuesser


answers : list[str] = []
options : list[str] = []

gameSize : int

alphabet : dict[str, int] = {}


def openWords() -> bool:

    """
    Opens and reads the answers and options files to load them to lists.
    Returns True if successful, False if lists are invalid (word lists should have equal length across all lines).
    """

    global answers, options, gameSize, alphabet

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
        for char in answer.upper():
            if char not in alphabet:
                alphabet[char] = infos.infoless()
        if len(answer) != gameSize:
            answers = []
            options = []
            alphabet = {}
            return False
    
    for option in options:
        for char in option.upper():
            if char not in alphabet:
                alphabet[char] = infos.infoless()
        if len(option) != gameSize:
            answers = []
            options = []
            alphabet = {}
            return False

    return True

print(openWords())
wordGuesser.guess(gameSize, answers, options, alphabet)