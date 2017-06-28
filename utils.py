import os
import codecs
import random
import re
from nltk.corpus import stopwords
from sklearn.metrics import confusion_matrix

punctuals = ", . - ( ) / { } | _".split()
def replacePunctual(doc):
    for i in punctuals:
        doc = doc.replace(i,"")
    return doc

def readSingleFile(filePath):
    f = codecs.open(filePath, "r", "utf-8")
    doc = ""
    for line in f:
        line = line.strip()
        doc += line
    return doc

def readdata(dirPath):
    fileList = [os.path.join(dirPath, fileName) for fileName in os.listdir(dirPath)]
    return [readSingleFile(filePath) for filePath in fileList]

def split(pos, neg, trainingPercentage = 0.7):
    trainingX = []
    trainingY = []
    testingX = []
    testingY = []
    for i in pos:
        if random.random() < trainingPercentage:
            trainingX.append(i)
            trainingY.append(1)
        else:
            testingX.append(i)
            testingY.append(1)

    for i in neg:
        if random.random() < trainingPercentage:
            trainingX.append(i)
            trainingY.append(0)
        else:
            testingX.append(i)
            testingY.append(0)
    
    return trainingX, trainingY, testingX, testingY

def wordsFreqs(texts):
    # remove words that appear only once
    from collections import defaultdict
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1
    return frequency

def genValidWords(docs):
    _wordsFreqs = wordsFreqs(docs)
    alpha = re.compile('[a-zA-Z\?!\']*')
    validWords = []
    _stopwords = set(stopwords.words('english'))
    for word in _wordsFreqs:
        if alpha.fullmatch(word) and _wordsFreqs[word] > 2:
            validWords.append(word)
    return set(validWords) - _stopwords

def printPerformance(y_real, y_predict):
    
    pass

if __name__ == '__main__':
    # print(os.listdir())
    # removeLowFreqWords(readdata("data/pos"))
    # for i in readdata("data/pos"):
    #     print(i)

    alpha = re.compile('[a-zA-Z\?!\']*')
    s = "t??!2"
    print(alpha.fullmatch(s))
