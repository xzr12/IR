#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import codecs
import os


def getHtmlContent(filename,output):
    #f = open(filename,'r')
    fileNo = filename[10:14]
    # print fileNo
    # if fileNo in [50, 51, 52, 136, 137, 138, 145, 147, 148, 149, 150, 151, 152, 180, 181, 182, 183,184,185,186,187, 189, 376, 377, 378, 379, 380,381,382,383,386,395,396,397,398,399,400,401,402,403,404,405,406,407,408,]:
    #     f = codecs.open(filename, 'r', 'utf-8')
    # else:
    f = codecs.open(filename,'r','gbk')
 
    #f2 = open(output, "w")
    f2 = codecs.open(output,'w','utf-8')
    i = 0
    mark = 0
    mark2 = 0
    divMark = 0
    while 1:
        try:
            line = f.readline()
            if (line.find('<title>')>=0 and line.find('</title>')>=0):
                ts = line.find('<title>')+7
                te = line.find('</title>')
                #f2 = open(output, "a")
                f2 = codecs.open(output,'a','utf-8')
                title = line[ts:te]
                #print title
                f2.write(title.encode('utf-8'))
                f2.write("\n")
            if (line.find('<script')>=0):
                mark = 0

            if i>=0:
                if mark == 0:
                    if(line.find('<p>')>=0):
                        #print line
                        index =  line.find('<p>')
                        sIndex = index+3
                        #print sIndex, "sIndex"
                        mark = 1
                    elif line.find('<a')>=0:
                        index =  line.find('<a')
                        sIndex = index+2
                        #print sIndex, "sIndex"
                        mark = 1
                else:
                    sIndex = 0
                if line.find('</p>')>=0:
                    #print "end",line.find('</p>')
                    eIndex = line.find('</p>')
                    mark2 = 1
                elif line.find('</P>')>=0:
                    eIndex = line.find('</P>')
                    mark2 = 1
                elif line.find('</a>')>=0:
                    eIndex = line.find('</a>')
                    mark2 = 1
                else:
                    eIndex = -1
                if mark == 1:
                    #f2 = open(output, "a")
                    f2 = codecs.open(output,'a','utf-8')
                    mainText = line[sIndex:eIndex+1]
                    #print mainText
                    si = mainText.find('>')
                    ei = mainText.find('<')
                    while si>=0:
                        mainText = mainText[si+1:-1]
                        si = mainText.find('>')
                        #print "si",si
                        #print "n1",mainText
                    while ei>=0:
                        mainText = mainText[0:ei]
                        ei = mainText.find('<')
                        #print "ei",ei
                        #print "n2",mainText
                    #print mainText
                    if len(mainText)>0 and (not mainText.find('href')>=0 and not mainText.find(".com")>=0):
                        f2.write(mainText.encode("utf-8"))
                        f2.write("\n")
                        #mark2 = 1
                    if mark2 == 1:
                        mark = 0
                        mark2 = 0

            if not line:
                break
            i+=1
        except:
            return fileNo
    return 'True'


def getHtmlContentNew(filename,output):
    #f = open(filename,'r')
    fileNo = filename[10:14]
    # print fileNo
    # if fileNo in [50, 51, 52, 136, 137, 138, 145, 147, 148, 149, 150, 151, 152, 180, 181, 182, 183,184,185,186,187, 189, 376, 377, 378, 379, 380,381,382,383,386,395,396,397,398,399,400,401,402,403,404,405,406,407,408,]:
    #     f = codecs.open(filename, 'r', 'utf-8')
    # else:
    f = codecs.open(filename,'r','utf-8')
 
    #f2 = open(output, "w")
    f2 = codecs.open(output,'w','utf-8')
    i = 0
    mark = 0
    mark2 = 0
    divMark = 0
    while 1:
        try:
            line = f.readline()
            if (line.find('<title>')>=0 and line.find('</title>')>=0):
                ts = line.find('<title>')+7
                te = line.find('</title>')
                #f2 = open(output, "a")
                f2 = codecs.open(output,'a','utf-8')
                title = line[ts:te]
                #print title
                f2.write(title.encode('utf-8'))
                f2.write("\n")
            if (line.find('<script')>=0):
                mark = 0

            if i>=0:
                if mark == 0:
                    if(line.find('<p>')>=0):
                        #print line
                        index =  line.find('<p>')
                        sIndex = index+3
                        #print sIndex, "sIndex"
                        mark = 1
                    elif line.find('<a')>=0:
                        index =  line.find('<a')
                        sIndex = index+2
                        #print sIndex, "sIndex"
                        mark = 1
                else:
                    sIndex = 0
                if line.find('</p>')>=0:
                    #print "end",line.find('</p>')
                    eIndex = line.find('</p>')
                    mark2 = 1
                elif line.find('</P>')>=0:
                    eIndex = line.find('</P>')
                    mark2 = 1
                elif line.find('</a>')>=0:
                    eIndex = line.find('</a>')
                    mark2 = 1
                else:
                    eIndex = -1
                if mark == 1:
                    #f2 = open(output, "a")
                    f2 = codecs.open(output,'a','utf-8')
                    mainText = line[sIndex:eIndex+1]
                    #print mainText
                    si = mainText.find('>')
                    ei = mainText.find('<')
                    while si>=0:
                        mainText = mainText[si+1:-1]
                        si = mainText.find('>')
                        #print "si",si
                        #print "n1",mainText
                    while ei>=0:
                        mainText = mainText[0:ei]
                        ei = mainText.find('<')
                        #print "ei",ei
                        #print "n2",mainText
                    #print mainText
                    if len(mainText)>0 and (not mainText.find('href')>=0 and not mainText.find(".com")>=0):
                        f2.write(mainText.encode("utf-8"))
                        f2.write("\n")
                        #mark2 = 1
                    if mark2 == 1:
                        mark = 0
                        mark2 = 0

            if not line:
                break
            i+=1
        except:
            return fileNo
    return 'True'

def processAll():

    num = 1
    i = 1
    path1 = 'html_sohu/'
    path2 = 'content_sohu/'
    dirs = os.listdir(path1)
    #print dirs

    test = []
    print len(dirs)
    for file in dirs:
        #print file
        if file == ".DS_Store":
            continue
        fileNo = str(file)[0:4]
        print fileNo
        fileName = path1+fileNo+'.html'
        output = path2+fileNo+'.txt'
        
        result = getHtmlContent(fileName,output)
        if result == 'True':
            continue
        else:
            test.append(result)

    for i in test:
        fileName = path1+i+'.html'
        output = path2+i+'.txt'
        
        getHtmlContentNew(fileName,output)


def process():
    files = os.listdir('html')
    path1 = 'html_sohu/'
    path2 = 'content_sohu/'
    for i in files:
        fileNo = i[0:4]
        print fileNo
        fileName = path1+fileNo+'.html'
        output = path2+fileNo+'.txt'
        getHtmlContentNew(fileName,output)

'''
path = '/Users/maggie/Desktop/'
fileNo = '0001'
fileName = path+fileNo+'.html'
print fileName
output = path+fileNo+'.txt'
getHtmlContent(fileName,output)
'''
processAll()
#process()