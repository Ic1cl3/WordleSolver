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

def getGuessImperfection(guess : str, answers : list[str], information : dict[str, infos.info]) -> int:
    """
    Returns an imperfection score for the guess based on the information known about the letters.
    """
    score : float = 0.0
    poolSize : float = len(answers)
    possibleResults : int = 3 ** len(guess)
    possibleInfos : list[dict[str, infos.info]] = [information.copy() for i in range(possibleResults)]
    possibleMasks : list[str] = getBaseThreeList(len(guess))
    for maskI in range(len(possibleMasks)):
        mask = possibleMasks[maskI]
        for charI in range(len(mask)):
            char = guess[charI]
            if mask[charI] == "0":
                possibleInfos[maskI][char] = infos.infofull(-1)
            elif mask[charI] == "1":
                possibleInfos[maskI][char] = infos.infopartial()
                possibleInfos[maskI][char].markIndex(charI)
            elif mask[charI] == "2":
                possibleInfos[maskI][char] = infos.infofull(charI)
    for possibleInfo in possibleInfos:
        possibleAnswers : list[str] = filterAnswers(answers, possibleInfo)
        score += abs((1/possibleResults) - (len(possibleAnswers) / poolSize))
    return score

def getBaseThreeList(length : int) -> list[str]:
    """
    Returns a list of all possible base 3 masks for a given length.
    """
    masks : list[str] = []
    for i in range(3 ** length):
        mask : str = ""
        for j in range(length):
            mask += str((i // (3 ** j)) % 3)
        masks.append(mask)
    return masks