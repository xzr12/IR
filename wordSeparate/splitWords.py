__author__ = 'maggie'
import jieba
import codecs
import os

def splitContent(filename,output):
    f = open(filename,'r')
    f2 = codecs.open(output, "w", "utf-8")
    i = 0
    mark = 0
    while 1:
        line = f.readline()
        f2 = codecs.open(output, "a", "utf-8")
        word_list = jieba.cut(line, cut_all=False)
        for w in word_list:
            if w != " " and w!="\n":
                #print w
                f2.write(w)
                f2.write("\n")
            #print w
        if not line:
            break
        i+=1



def processAll():
    num = 1
    path1 = 'content_sohu/'
    path2 = 'words_sohu/'
    dirs = os.listdir(path1)
    print dirs
    #f = open('/Users/maggie/Desktop/skipContent.txt')
    for file in dirs:
        #print file
        if file == ".DS_Store":
            continue
        fileNo = str(file)[0:4]
        print fileNo
        fileName = path1+fileNo+'.txt'
        output = path2+fileNo+'.txt'
        splitContent(fileName,output)

def processAll_En():
    path1 = 'content_wiki/'
    path2 = 'words_wiki/'
    dirs = os.listdir(path1)
    print dirs
    #f = open('/Users/maggie/Desktop/skipContent.txt')
    for file in dirs:
        #print file
        if file == ".DS_Store":
            continue
        fileNo = str(file)[0:4]
        print fileNo
        fileName = path1+fileNo+'.txt'
        output = path2+fileNo+'.txt'
        splitContent(fileName,output)

'''
path1 = '/Users/maggie/Desktop/Content/'
path2 = '/Users/maggie/Desktop/Words/'
fileNo = '0005'
filename = path1+fileNo+'.txt'
output = path2+fileNo+'.txt'
splitContent(filename,output)
'''
processAll()
processAll_En()