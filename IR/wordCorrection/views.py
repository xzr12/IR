# coding=utf-8
from wordCorrection.search import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from wordCorrection.models import *
from wordCorrection.corrector_CH import *
from wordCorrection.corrector_EN import *
from wordCorrection.splitBeforeSearch import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from time import clock
# Create your views here.

def home(request):
    # saveData('testC', 0)
    # saveData('test', 1)
    saveData('final_sohu', 0)
    saveData('final_wiki', 1)
    return HttpResponse('initial successfully!')


def test(request):
    # input1 = "四川人喜欢吃麻拉火果"
    # list1 = splitWords(input1)
    # list2 = skipStopWords(list1, 0)
    # output1 = corrector_CH(list2)
    # list3 = splitWordsAfter(''.join(output1))
    # output = skipStopWords(list3, 0)
    # for i in output:
    #     print i
    #
    # docu, results = calcSimilarity(output, 0)
    # docu, results = calcSimilarity(['人类', '用户', '机器', '接口'], 0)
    # docu, results = calcSimilarity(['human', 'user', 'machine', 'interface'], 1)


    dictionary, commonDic = loadDic()
    input1 = "I cannot spelll a right arawee today good"
    list1 = splitWords(input1)
    list2 = skipStopWords(list1, 1)
    output = corrector_EN(list2, dictionary, commonDic)

    docu, results = calcSimilarity(output, 1)
    for i in range(10):
        print results[i][0] + ' : ' + str(results[i][1])
    print len(docu)
    print len(results)

    return HttpResponse('test query!')

# content {'docu': 'content'}
@csrf_exempt
def search(request):
    if request.method == 'GET':
        return render_to_response('indexQuery.html', {})

    input = request.POST.get('search_input', '')
    list1 = splitWords(input)
    if len(list1) == 0:
        return render_to_response('index.html', {'input': input, 'error': '没有找到相关的结果！'})

    timeBgein = clock()
    if list1[0].isalnum():
        type = 1
        dictionary, commonDic = loadDic()
        list2 = skipStopWords(list1, 1)
        output = corrector_EN(list2, dictionary, commonDic)
        b = ' '.join(output)
    else:
        type = 0
        list2 = skipStopWords(list1, 0)
        output1 = corrector_CH(list2)
        b = ''.join(output1)
        list3 = splitWordsAfter(b)
        output = skipStopWords(list3, 0)

    a = input.encode('utf-8')
    if a in b.encode('utf-8'):
        change = 0
    else:
        change = 1

    docu, results = calcSimilarity(output, type)
    timeout = clock() - timeBgein

    out = []
    for r in results:
        # print r[0] + ':' + str(r[1])
        documentName = r[0]
        if type == 0:
            file = open('content_sohu/'+documentName+'.txt').readlines()
            sep = 20
            #print documentName
        else:
            file = open('content_wiki/'+documentName+'.txt').readlines()
            sep = 20
        allContent = ' '.join(file)
        allContentNew = ' '.join(allContent.split('\n')).decode('utf-8')

        resStr = []
        #print documentName
        #print allContentNew
        for word in output:
            if word.decode('utf-8') in allContentNew:
                wordList = allContentNew.split(word.decode('utf-8'))
                #print len(wordList)
                for i in range(len(wordList)):
                    #print wordList[i]
                    if type == 0:
                        if i == 0:
                            resStr.append('...' + (wordList[i][(len(wordList[i])-sep-1):(len(wordList[i])-3)]).encode('utf-8'))
                        else:
                            resStr.append('<em>')
                            resStr.append(word)
                            resStr.append('</em>')
                            if i == len(wordList) - 1:
                                resStr.append((wordList[i][0:sep]).encode('utf-8') + '...')
                            else:
                                resStr.append((wordList[i][0:sep]).encode('utf-8') + '...' + (wordList[i][(len(wordList[i])-sep-1):(len(wordList[i])-1)]).encode('utf-8'))
                    else:
                        if i == 0:
                            resStr.append('...' + wordList[i][(len(wordList[i])-sep-1):(len(wordList[i])-1)])
                        else:
                            resStr.append('<em>')
                            resStr.append(word)
                            resStr.append('</em>')
                            if i == len(wordList) - 1:
                                resStr.append(wordList[i][0:sep] + '...')
                            else:
                                resStr.append(wordList[i][0:sep] + '...' + wordList[i][(len(wordList[i])-sep-1):(len(wordList[i])-1)])
                break
        if len(resStr) > 22:
            resStr = resStr[0:21]
        out.append({'docu': documentName, 'href': docu[documentName]['href'], 'title': docu[documentName]['title'], 'content': resStr})
    return render_to_response('index.html', {'input': input, 'output': b, 'outList': output, 'change': change, 'times': len(results), 'time': timeout, 'results': out})

@csrf_exempt
def searchNoCorrect(request, input):
    print input
    list1 = splitWords(input)
    if len(list1) == 0:
        return render_to_response('index.html', {'input': input, 'error': '没有找到相关的结果！'})

    timeBegin = clock()
    if list1[0].isalnum():
        type = 1
        output = skipStopWords(list1, 1)
        b = ' '.join(output)
    else:
        type = 0
        b = ''.join(list1)
        list3 = splitWordsAfter(b)
        output = skipStopWords(list3, 0)

    change = 0

    docu, results = calcSimilarity(output, type)
    timeout = clock() - timeBegin

    out = []
    for r in results:
        # print r[0] + ':' + str(r[1])
        documentName = r[0]
        if type == 0:
            file = open('content_sohu/'+documentName+'.txt').readlines()
            sep = 20
            #print documentName
        else:
            file = open('content_wiki/'+documentName+'.txt').readlines()
            sep = 20
        allContent = ' '.join(file)
        allContentNew = ' '.join(allContent.split('\n')).decode('utf-8')

        resStr = []
        #print documentName
        #print allContentNew
        for word in output:
            if word.decode('utf-8') in allContentNew:
                wordList = allContentNew.split(word.decode('utf-8'))
                #print len(wordList)
                for i in range(len(wordList)):
                    #print wordList[i]
                    if type == 0:
                        if i == 0:
                            resStr.append('...' + (wordList[i][(len(wordList[i])-sep-1):(len(wordList[i])-3)]).encode('utf-8'))
                        else:
                            resStr.append('<em>')
                            resStr.append(word)
                            resStr.append('</em>')
                            if i == len(wordList) - 1:
                                resStr.append((wordList[i][0:sep]).encode('utf-8') + '...')
                            else:
                                resStr.append((wordList[i][0:sep]).encode('utf-8') + '...' + (wordList[i][(len(wordList[i])-sep-1):(len(wordList[i])-1)]).encode('utf-8'))
                    else:
                        if i == 0:
                            resStr.append('...' + wordList[i][(len(wordList[i])-sep-1):(len(wordList[i])-1)])
                        else:
                            resStr.append('<em>')
                            resStr.append(word)
                            resStr.append('</em>')
                            if i == len(wordList) - 1:
                                resStr.append(wordList[i][0:sep] + '...')
                            else:
                                resStr.append(wordList[i][0:sep] + '...' + wordList[i][(len(wordList[i])-sep-1):(len(wordList[i])-1)])
                break
        if len(resStr) > 22:
            resStr = resStr[0:21]
        out.append({'docu': documentName, 'href': docu[documentName]['href'], 'title': docu[documentName]['title'], 'content': resStr})
    return render_to_response('index.html', {'input': input, 'output': b, 'outList': output, 'change': change, 'times': len(results), 'time': timeout, 'results': out})
