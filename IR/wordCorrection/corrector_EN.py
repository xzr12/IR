__author__ = 'maggie'

from wordCorrection.models import *
def cal_levenshtein_dist(first, second):
    """Find the Levenshtein distance between two strings."""
    if len(first) > len(second):
        first, second = second, first
    if len(second) == 0:
        return len(first)
    first_len = len(first) + 1
    second_len = len(second) + 1
    distance = [[0] * second_len for x in range(first_len)]
    for i in range(first_len):
       distance[i][0] = i
    for j in range(second_len):
       distance[0][j]=j
    for i in xrange(1, first_len):
        for j in range(1, second_len):
            delete = distance[i-1][j] + 1
            insert = distance[i][j-1] + 1
            substitute = distance[i-1][j-1]
            if first[i-1] != second[j-1]:
                substitute += 1
            distance[i][j] = min(insert, delete, substitute)
    return distance[first_len-1][second_len-1]



def correctOneWord_EN(input,dictionary,commonDic):
    input = input.lower()
    min_dist = 100
    output = ""
    outputList = []
    outputList2 = []
    si = input[0]
    sindex = 0
    eindex = -1
    '''
    for w in dictionary:
        #print w
        if w[0] == si:
            sindex = dictionary.index(w)
            break
    '''
    sindex = dictionary.index(si)
    print si,sindex
    dictionary1 = dictionary[sindex:-1]
    if si!='z':
        ei = chr(ord(si) + 1)
        eindex = dictionary1.index(ei)
        '''
        for w in dictionary1:
            #print w
            if w[0] == ei:
                eindex =dictionary1.index(w)
                break
        '''
    cur_dictionary = dictionary1[0:eindex]

    for w in cur_dictionary:
        distance = cal_levenshtein_dist(input,w)
        if distance<min_dist:
            min_dist = distance
            output = w
            outputList = []
            outputList.append(w)
        elif distance == min_dist:
            outputList.append(w)
    print "list1",outputList

    print "commonDictionary check"
    for w in outputList:
        if w in commonDic:
            print w
            outputList2.append(w)

    print "list2",outputList2

    resultWord = ""
    minIdf = 100
    if len(outputList2)>1:
        for w in outputList2:
            result = EnglishWordModel.objects.filter(word=w)
            print "search result len",len(result),w
            if len(result)>0:
                for r in result:
                    print r['word'],r['idf']
                    if r['idf']<minIdf:
                        resultWord = w
                        minIdf = r['idf']
        if resultWord == "":
            resultWord = outputList2[0]
            print "commonList first"
        #return resultWord
    elif len(outputList2) == 1:
        resultWord =  outputList2[0]
    else:
        for w in outputList:
            result = EnglishWordModel.objects.filter(word=w)
            print "search result len",len(result),w
            if len(result)>0:
                for r in result:
                    print r['word'],r['idf']
                    if r['idf']<minIdf:
                        resultWord = w
                        minIdf = r['idf']
        if resultWord == "":
            resultWord = outputList[0]
            print "List first"
    print "resultWord",resultWord
    return resultWord

def getDictionary():
    f = open('dic/dictionary.txt').read()
    dictionary = f.splitlines()
    #f2 = open('dic.txt','w')
    '''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for al in alphabet:
        if al in dictionary:
            print al, dictionary.index(al)
    '''
    return dictionary
def getCommonDic():
    f = open('dic/commonDic.txt','r').read()
    commonDic = f.splitlines()
    commonDicDict = {}
    for w in commonDic:
        commonDicDict[w] = 1
    return commonDicDict

def loadDic():
    dictionary = getDictionary()
    commonDic = getCommonDic()
    return dictionary, commonDic

def corrector_EN(inputList, dictionary, commonDic):
    outputList = []
    newWord = ""
    for oldWord in inputList:
        newWord = correctOneWord_EN(oldWord,dictionary,commonDic)
        outputList.append(newWord)
    print "outputList"
    for w in outputList:
        print w
    return outputList
