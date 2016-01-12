#!/usr/bin/python
# -*- coding: utf-8 -*-

from pypinyin import lazy_pinyin
from wordCorrection.models import *

def corrector_CH(inputList):
    outputList = []
    for oldWord in inputList:
        newWord = correctOneWord(oldWord)
        outputList.append(newWord)
    # print "outputList"
    # for w in outputList:
    #     print w
    return outputList


def correctOneWord(oldWord):
    word = oldWord.decode('utf-8')
    pyList = lazy_pinyin(word)
    pyStr = ""
    maxSame = 0
    resultWord = ""
    same = 0
    count = 0
    for py in pyList:
        pyStr+=py.encode('utf-8')
    print pyStr
    result = ChineseWordModel.objects.filter(pinyin=pyStr).order_by('idf')
    if len(result) == 0:
        print "pinyin do not exist"
        return oldWord
    for r in result:
        print r['word']
        print r['idf']
        same = findSameChar(word,r['word'])
        if(same>maxSame):
            maxSame = same
            resultWord = r['word']
    print "maxSame",maxSame
    if maxSame == 0:
        resultWord = result[0]['word']
        print "no similar word"
    return resultWord

def findSameChar(oldWord,newWord):
    same = 0
    for c in newWord:
        print c
        if c in oldWord:
            same+=1
    #print "same",same
    return same

'''
oldWord = u'西按市'
WordList = [u'显示',u'西安市',u'现实']
findSameChar(oldWord,WordList[1])
'''

# results = splitWords('小明硕士毕业于中国科学院计算所，后在日本京都大学深造')
# # results = splitWords('today is  a good day, and happy')
# # for result in results:
# #     if result != '':
# #         print result
# result = skipStopWords(results, 0)
# for r in result:
#     print r