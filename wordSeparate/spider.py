import urllib2
import httplib
import re

class Spider:
    def __init__(self, urls):
        self.index = 1
        self.linkList = linkList()
        self.htmlFile = open('../IR/html_sohu.txt', 'w')
        #self.htmlFile = open('../IR/html_wiki.txt', 'w')

        if isinstance(urls, list):
            for url in urls:
                self.linkList.addUnvisitedUrl(url)
        if isinstance(urls, str):
            self.linkList.addUnvisitedUrl(urls)
            
    def spidering(self, urls, maxcount):
        while self.index <= maxcount:
            #self.setProxy()
            if not self.linkList.isUnvisitedEmpty():
                visitUrl = self.linkList.getUnvisitedTop()
                if visitUrl == None or visitUrl == "":
                    continue
                links, error = self.getHtml(visitUrl)
                self.linkList.addVisitedUrl(visitUrl)
                
                if links != None and error == 0:
                    for link in links:
                        l = len(link[1])
                        # if link[1][0:6] == '/wiki/':
                        #     self.linkList.addUnvisitedUrl('https://en.wikipedia.org'+link[1])
                        if link[1][0:4] == 'http':
                            if link[1][(l-4):l] == '.htm' or link[1][(l-5):l] == '.html' or link[1][(l-6):l] == '.shtml':
                                self.linkList.addUnvisitedUrl(link[1])
                                #print link[1]
        self.htmlFile.close()

    def getHtml(self, url):
        output = open('./html_sohu/' + self.transNum() + '.html', 'w')
        #output = open('./html_wiki/' + self.transNum() + '.html', 'w')
        pattern = re.compile(r'<a(.*?)href="(.*?)"(.*?)>(.*?)</a>')
        
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent, 'Referer': 'http://news.sohu.com/' }
        request = urllib2.Request(url, headers=headers)

        error = 0

        try:
            response = urllib2.urlopen(request)
        except urllib2.URLError, e:
            error = 1
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason
            return None, error
        else:
            #print self.index

            # get html file
            try:
                content = response.read()
            except httplib.IncompleteRead, e:
                error = 1
                content = e.partial

            print self.index
            output.write(content)
            output.close()

            self.htmlFile.write(str(self.index)+'\t'+url+'\n')
            #print str(self.index)+'\t'+url

            self.index = self.index + 1
            
            # re parse, refresh visited/unvisited list
            links = re.findall(pattern, content)
            return links, error
    
    def transNum(self):
        num = self.index
        result = str(num/1000)+str((num%1000)/100)+str((num%100)/10)+str(num%10)
        return result
    
    def setProxy(self):
        enable_proxy = True
        proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
        null_proxy_handler = urllib2.ProxyHandler({})
        if enable_proxy:
            opener = urllib2.build_opener(proxy_handler)
        else:
            opener = urllib2.build_opener(null_proxy_handler)
        urllib2.install_opener(opener)
        return
 
class linkList:
    def __init__(self):
        self.visited = []
        self.unvisited = []
    def addVisitedUrl(self, url):
        self.visited.append(url)
    def getUnvisitedTop(self):
        if len(self.unvisited) > 0:
            url = self.unvisited[0]
            del self.unvisited[0]
            return url
        else:
            return None
    def addUnvisitedUrl(self, url):
        if url != "" and url not in self.visited and url not in self.unvisited:
            self.unvisited.append(url)
    def isUnvisitedEmpty(self):
        return len(self.unvisited) == 0
  
    
def main(urls, maxcount):
    spider = Spider(urls)
    spider.spidering(urls, maxcount)


if __name__ == "__main__":
    #main("https://en.wikipedia.org/wiki/Main_Page", 3000)
    main("http://news.sohu.com/", 3000)