'''
author    xuziru
function  split the input words and drop the stopwords
'''
import jieba
import codecs


def splitWords(input):
    sep = jieba.cut(input, cut_all=False)
    inputLine = ' '.join(sep)
    inputList = inputLine.encode('utf-8').split(' ')
    return inputList

def splitWordsAfter(input):
    sep = jieba.cut_for_search(input)
    inputLine = ' '.join(sep)
    inputList = inputLine.encode('utf-8').split(' ')
    return inputList

def skipStopWords(inputList, type):
    if type == 0:
        stopwords = codecs.open('skipwords/skipWords.txt', 'r', 'utf-8').readlines()
    else:
        stopwords = codecs.open('skipwords/skipWords_En.txt', 'r', 'utf-8').readlines()

    stopList = []
    for word in stopwords:
        stopList.append((word.split('\n')[0]).encode('utf-8'))

    if type == 0:
        inputFilter1 = []
        for word in inputList:
            if word == '':
                continue
            elif (word[0] >= 'a' and word[0] <= 'z') or (word[0] >= 'A' and word[0] <= 'Z'):
                continue
            elif word[0] >= '0' and word[0] <= '9':
                continue
            else:
                inputFilter1.append(word)
    else:
        inputFilter1 = []
        for word in inputList:
            word = word.lower()
            if word == '':
                continue
            elif word[0] >= '0' and word[0] <= '9':
                continue
            elif word[0] > 'z' or word[0] < 'a':
                continue
            else:
                inputFilter1.append(word)
    inputFilter2 = list(set(inputFilter1) - set(stopList))
    outputList = []
    for word in inputFilter1:
        if word in inputFilter2:
            outputList.append(word)
    return outputList