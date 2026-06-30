words = open("WordList.txt", "r")
new = open("Answers.txt", "w")
onew = open("Options.txt", "w")

wordList = []

for line in words:
    word = (line.split("\t")[2][0:5])
    wordList.append(word)

for i in range(2316):
    new.write(wordList[i] + "\n")

for word in wordList:
    onew.write(word + "\n")

words.close()
new.close()
onew.close()