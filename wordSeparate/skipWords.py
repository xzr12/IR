#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import os

def skipWords(filename,output,skipWordList):
    inputW = codecs.open(filename,'r','utf-8').readlines()
    inputWList = []
    for w in inputW:
        if (w[0]>='a' and w[0]<='z') or (w[0]>='A' and w[0]<='Z'):
            continue
        elif w[0]>='0' and w[0]<='9':
            continue
        else:
            inputWList.append(w)
    outputWList = list(set(inputWList)-set(skipWordList))
    f2 = codecs.open(output, "w", "utf-8")
    '''
    for w in outputWList:
        f2.write(w)
    '''
    for w in inputWList:
        if w in outputWList:
            f2.write(w)

def skipWords_En(filename,output,skipWordList):
    inputW = open(filename,'r').readlines()
    inputWList = []
    for w in inputW:
        w1 = w.lower()
        if w[0]>='0' and w[0]<='9':
            continue
        elif w1[0]>'z' or w1[0]<'a':
            continue
        else:
            inputWList.append(w1)
    outputWList = list(set(inputWList)-set(skipWordList))
    f2 = open(output, "w")
    '''
    for w in outputWList:
        f2.write(w)
    '''
    for w in inputWList:
        if w in outputWList:
            f2.write(w)


def getStopWords():
    skipW = codecs.open("skipwords/skipContent.txt",'r',"utf-8").readlines()
    skipWList = []
    for w in skipW:
        skipWList.append(w)
    return skipWList
def getStopWords_En():
    skipW = codecs.open("skipwords/skipWords_En.txt",'r').readlines()
    skipWList = []
    for w in skipW:
        skipWList.append(w)
    return skipWList
'''
skipWordList = getStopWords()
path1 = '/Users/maggie/Documents/Words/'
path2 = '/Users/maggie/Documents/FinalWords/'
fileNo = '0001'
filename = path1+fileNo+'.txt'
output = path2+fileNo+'.txt'
skipWords(filename,output,skipWordList)
'''
def processAll():
    path1 = 'words_sohu/'
    path2 = 'final_sohu/'
    dirs = os.listdir(path1)
    print dirs
    skipWordList = getStopWords()
    for file in dirs:
        if file == ".DS_Store":
            continue
        fileNo = str(file)[0:4]
        print fileNo
        fileName = path1+fileNo+'.txt'
        output = path2+fileNo+'.txt'
        skipWords(fileName,output,skipWordList)

def processAll_En():
    path1 = 'words_wiki/'
    path2 = 'final_wiki/'
    dirs = os.listdir(path1)
    print dirs
    skipWordList = getStopWords_En()
    for file in dirs:
        if file == ".DS_Store":
            continue
        fileNo = str(file)[0:4]
        print fileNo
        fileName = path1+fileNo+'.txt'
        output = path2+fileNo+'.txt'
        skipWords_En(fileName,output,skipWordList)

processAll()
processAll_En()