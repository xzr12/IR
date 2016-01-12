#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import os

def getHtmlContent(filename,output):
    f = open(filename,'r')
    # f2 = codecs.open(output, 'w', 'utf-8')
    i = 0
    mark = 0
    mark2 = 0
    divMark = 0
    while 1:
        line = f.readline()
        if (line.find('<title>')>=0 and line.find('</title>')>=0):
            ts = line.find('<title>')+7
            te = line.find('</title>')
            # f2 = open(output, "a")
            title = line[ts:te]
            # print title
            # f2.write(title)
            # f2.write("\n")
            return title
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
                # f2 = open(output, "a")
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
                # print mainText
                # if len(mainText)>0 and (not mainText.find('href')>=0 and not mainText.find(".com")>=0):
                #     f2.write(mainText)
                #     f2.write("\n")
                    #mark2 = 1
                if mark2 == 1:
                    mark = 0
                    mark2 = 0

        if not line:
            break
        i+=1
    return ''


def processAll():

    num = 1
    i = 1
    path1 = 'html_sohu/'
    path2 = 'content_sohu/'
    titleFile = '../IR/title_sohu.txt'
    titleOutput = open(titleFile, 'w')
    dirs = os.listdir(path1)
    #print dirs

    for file in dirs:
        #print file
        if file == ".DS_Store":
            continue
        fileNo = str(file)[0:4]
        #print fileNo
        fileName = path1+fileNo+'.html'
        output = path2+fileNo+'.txt'
        title = getHtmlContent(fileName,output)
        print fileNo + " : " + title
        titleOutput.write(fileNo + "\t" + title)
        titleOutput.write('\n')

    titleOutput.close()

def processAll_EN():
    num = 1
    i = 1
    path1 = 'html_wiki/'
    path2 = 'content_wiki/'
    titleFile = '../IR/title_wiki.txt'
    titleOutput = open(titleFile, 'w')
    dirs = os.listdir(path1)
    #print dirs

    for file in dirs:
        #print file
        if file == ".DS_Store":
            continue
        fileNo = str(file)[0:4]
        #print fileNo
        fileName = path1+fileNo+'.html'
        output = path2+fileNo+'.txt'
        title = getHtmlContent(fileName,output)
        print fileNo + " : " + title
        titleOutput.write(fileNo + "\t" + title)
        titleOutput.write('\n')

    titleOutput.close()


'''
path = '/Users/maggie/Desktop/'
fileNo = '0001'
fileName = path+fileNo+'.html'
print fileName
output = path+fileNo+'.txt'
getHtmlContent(fileName,output)
'''
processAll()
processAll_EN()