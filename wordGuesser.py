import infos

def guess(gameSize : int, answers : list[str], options : list[str], information : dict[str, infos.info]) -> None:
    """
    Main function to guess words.
    """

def filterAnswers(answers : list[str], information : dict[str, infos.info]) -> list[str]:
    possibleAnswers : list[str] = answers.copy()

    for answer in answers:
        for charI in range(len(answer)):
            char = answer[charI]
            if information[char] is infos.infopartial:
                if charI in information[char].falseIndicies:
                    possibleAnswers.remove(answer)
            if information[char] is infos.infofull:
                if information[char].index != charI:
                    possibleAnswers.remove(answer)
    
    return possibleAnswers