# coding=utf-8
from __future__ import division
import os
import math
from collections import Counter
from pypinyin import lazy_pinyin
from wordCorrection.models import *

# define
# type: 0 represent Chinese, 1 represent English
# model {('word', 'document'): {'tfIdf': tfidf, 'times': times, 'tf': tf}}
# documentModel {'document': {'length': length, 'href': href, 'title': title}}
# wordModel {'word': {'length': length, 'idf': idf, 'pinyin': pinyin}}
# wordModel {'word': {'length': length, 'idf': idf}}

def initial(folderName, type):
    documents = os.listdir('./'+folderName+'/')
    index = 1
    # the same sequence with model in models.py
    model = {}
    documentModel = {}
    wordModel = {}

    ld = len(documents)
    if type == 0:
        hrefList = open('./html_sohu.txt', 'r').readlines()
        titleList = open('./title_sohu.txt', 'r').readlines()
        for document in documents:
            if index % 50 == 0:
                print str(index) + ' / ' + str(ld)
            documentName = document[0:4]
            documentModel[documentName] = {'length': 0, 'href': hrefList[int(documentName)-1].split('\n')[0].split('\t')[1], 'title':titleList[int(documentName)-1].split('\n')[0].split('\t')[1]}
            words = open('./'+folderName+'/'+document, 'r').readlines()
            for word in words:
                singleWord = word.split('\n')[0]
                if len(singleWord) < 3:
                    continue
                singleWordUnicode = singleWord.decode('utf-8')
                pinyins = lazy_pinyin(singleWordUnicode)
                pinyinStr = ''
                for pinyin in pinyins:
                    pinyinStr = pinyinStr + pinyin.encode('utf-8')
                if len(pinyinStr) < 2:
                    continue
                if (singleWord in wordModel) == False:
                    wordModel[singleWord] = {'length': len(pinyins), 'idf': 0, 'pinyin': pinyinStr}
                if ((singleWord, documentName) in model) == False:
                    model[(singleWord, documentName)] = {'tfIdf': 0, 'times': 1, 'tf': 0}
                else:
                    times = model[(singleWord, documentName)]['times'] + 1
                    model[(singleWord, documentName)]['times'] = times
            index = index + 1
    else:
        hrefList = open('./html_wiki.txt', 'r').readlines()
        titleList = open('./title_wiki.txt', 'r').readlines()
        for document in documents:
            if index % 50 == 0:
                print str(index) + ' / ' + str(ld)
            documentName = document[0:4]
            documentModel[documentName] = {'length': 0, 'href': hrefList[int(documentName)-1].split('\n')[0].split('\t')[1], 'title':titleList[int(documentName)-1].split('\n')[0].split('\t')[1]}
            words = open('./'+folderName+'/'+document, 'r').readlines()
            for word in words:
                singleWord = word.split('\n')[0]
                l = len(singleWord)
                if l < 3 or l > 15:
                    continue
                if (singleWord in wordModel) == False:
                    wordModel[singleWord] = {'length': l, 'idf': 0}
                if ((singleWord, documentName) in model) == False:
                    model[(singleWord, documentName)] = {'tfIdf': 0, 'times': 1, 'tf': 0}
                else:
                    times = model[(singleWord, documentName)]['times'] + 1
                    model[(singleWord, documentName)]['times'] = times
            index = index + 1
    return model, documentModel, wordModel

# tfList {'document': max_times}
# idfList {'word': ni}
def calcTfIdf(model, documentModel, wordModel):
    tfList = {}
    idfList = {}

    modelList = model.keys()
    for group in modelList:
        word = group[0]
        document = group[1]
        tfList[document] = max([tfList.get(document, 0), model[group]['times']])
        idfList[word] = idfList.get(word, 0) + 1

    # calc idf
    wordModelList = wordModel.keys()
    n = len(documentModel)
    for word in wordModelList:
        ni = idfList[word]
        temp = n / ni
        wordModel[word]['idf'] = 1 + math.log10(temp)

    # calc tf & tfIdf
    for group in modelList:
        word = group[0]
        document = group[1]
        model[group]['tf'] = model[group]['times'] / tfList[document]
        model[group]['tfIdf'] = model[group]['tf'] * wordModel[word]['idf']

    return model, wordModel

def calcDocumentLength(model, documentModel):
    # calc length^2 (sum)
    modelList = model.keys()
    for group in modelList:
        document = group[1]
        tfIdf = model[group]['tfIdf']
        documentSingle = documentModel[document]
        documentSingle['length'] = documentSingle.get('length', 0) + math.pow(tfIdf, 2)

    documentList = documentModel.keys()
    for docu in documentList:
        length = documentModel[docu]['length']
        documentModel[docu]['length'] = math.sqrt(length)

    return documentModel

def saveDB(type, model, documentModel, wordModel):
    if type == 0:
        modelList = model.keys()
        index = 1
        l = len(modelList)
        for modelSingle in modelList:
            entry = ChineseModel(word=modelSingle[0], document=modelSingle[1], tfIdf=model[modelSingle]['tfIdf'], times=model[modelSingle]['times'], tf=model[modelSingle]['tf'])
            entry.save()
            if index % 5000 == 0:
                print str(index) + ' / ' + str(l)
            index = index + 1
        print 'Chinese model finish!'
        documentModelList = documentModel.keys()
        index = 1
        l = len(documentModelList)
        for documentModelSingle in documentModelList:
            entry = ChineseDocumentModel(document=documentModelSingle, length=documentModel[documentModelSingle]['length'], href=documentModel[documentModelSingle]['href'], title=documentModel[documentModelSingle]['title'])
            entry.save()
            if index % 5000 == 0:
                print str(index) + ' / ' + str(l)
            index = index + 1
        print 'Chinese document model finish!'
        wordModelList = wordModel.keys()
        index = 1
        l = len(wordModelList)
        for wordModelSingle in wordModelList:
            entry = ChineseWordModel(word=wordModelSingle, length=wordModel[wordModelSingle]['length'], pinyin=wordModel[wordModelSingle]['pinyin'], idf=wordModel[wordModelSingle]['idf'])
            entry.save()
            if index % 5000 == 0:
                print str(index) + ' / ' + str(l)
            index = index + 1
        print 'Chinese word model finish!'
    else:
        modelList = model.keys()
        index = 1
        l = len(modelList)
        for modelSingle in modelList:
            entry = EnglishModel(word=modelSingle[0], document=modelSingle[1], tfIdf=model[modelSingle]['tfIdf'], times=model[modelSingle]['times'], tf=model[modelSingle]['tf'])
            entry.save()
            if index % 5000 == 0:
                print str(index) + ' / ' + str(l)
            index = index + 1
        print 'English model finish!'
        documentModelList = documentModel.keys()
        index = 1
        l = len(documentModelList)
        for documentModelSingle in documentModelList:
            entry = EnglishDocumentModel(document=documentModelSingle, length=documentModel[documentModelSingle]['length'], href=documentModel[documentModelSingle]['href'], title=documentModel[documentModelSingle]['title'])
            entry.save()
            if index % 5000 == 0:
                print str(index) + ' / ' + str(l)
            index = index + 1
        print 'English document model finish!'
        wordModelList = wordModel.keys()
        index = 1
        l = len(wordModelList)
        for wordModelSingle in wordModelList:
            entry = EnglishWordModel(word=wordModelSingle, length=wordModel[wordModelSingle]['length'], idf=wordModel[wordModelSingle]['idf'])
            entry.save()
            if index % 5000 == 0:
                print str(index) + ' / ' + str(l)
            index = index + 1
        print 'English word model finish!'

def saveData(folderName, type):
    model, documentModel, wordModel = initial(folderName, type)
    model, wordModel = calcTfIdf(model, documentModel, wordModel)
    documentModel = calcDocumentLength(model, documentModel)
    saveDB(type, model, documentModel, wordModel)

def queryInfo(type, input):
    # words = (input).decode('utf-8').split(' ')
    wordsSet = dict(Counter(input))
    wordsList = list(Counter(input))
    maxWordNum = 0
    for word in wordsList:
        if wordsSet[word] > maxWordNum:
            maxWordNum = wordsSet[word]
    tfIdfList = []
    length = 0
    # all words in wordlist, otherwise need to correct
    for word in wordsList:
        if type == 0:
            oneWord = ChineseWordModel.objects.filter(word=word)
        else:
            oneWord = EnglishWordModel.objects.filter(word=word)
        tf = wordsSet[word] / maxWordNum
        if len(oneWord) == 0:
            continue
        idf = oneWord[0]['idf']
        tfIdf = tf * idf
        length = length + math.pow(tfIdf, 2)
        tfIdfList.append([word, tfIdf])
    return dict(tfIdfList), math.sqrt(length)

# calcList {'document': {'length': length, 'words': {'word1': tfidf, 'word2': tfidf, ...}}}
# words all in input
# documentList {'document': {'href': href, 'title': title}}
# similarityList {'document': similarity}
def calcSimilarity(input, type):
    tfIdfList, length = queryInfo(type, input)
    calcList = {}
    documentList = {}
    similarityList = {}
    if type == 0:
        # load
        for oneWord in tfIdfList.keys():
            documents = ChineseModel.objects.filter(word=oneWord)
            for document in documents:
                documentName = document['document']
                if documentName in calcList:
                    calcList[documentName]['words'].update({document['word']: document['tfIdf']})
                else:
                    docu = ChineseDocumentModel.objects.get(document=documentName)
                    calcList[documentName] = {'length': docu['length'], 'words': {document['word']: document['tfIdf']}}
                    documentList[documentName] = {'href': docu['href'], 'title': docu['title'], }
        # calc
        for document in calcList.keys():
            oneDocument = calcList[document]
            words = oneDocument['words']
            partation = 0
            for word in tfIdfList.keys():
                if word.decode('utf-8') in words:
                    partation = partation + tfIdfList[word] * words[word.decode('utf-8')]
            similarity = partation / oneDocument['length'] / length
            similarityList[document] = similarity
    else:
        # load
        for oneWord in tfIdfList.keys():
            documents = EnglishModel.objects.filter(word=oneWord)
            for document in documents:
                documentName = document['document']
                if documentName in calcList:
                    calcList[documentName]['words'].update({document['word']: document['tfIdf']})
                else:
                    docu = EnglishDocumentModel.objects.get(document=documentName)
                    calcList[documentName] = {'length': docu['length'], 'words': {document['word']: document['tfIdf']}}
                    documentList[documentName] = {'href': docu['href'], 'title': docu['title'], }
        # calc
        for document in calcList.keys():
            oneDocument = calcList[document]
            words = oneDocument['words']
            partation = 0
            for word in tfIdfList.keys():
                if word in words:
                    partation = partation + tfIdfList[word] * words[word]
            similarity = partation / oneDocument['length'] / length
            similarityList[document] = similarity
    return documentList, sorted(similarityList.items(), key=lambda e:e[1], reverse=True)