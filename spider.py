import urllib2
import re

class Spider:
    def __init__(self, urls):
        self.index = 1
        self.linkList = linkList()
        if isinstance(urls, list):
            for url in urls:
                self.linkList.addUnvisitedUrl(url)
        if isinstance(urls, str):
            self.linkList.addUnvisitedUrl(urls)
            
    def spidering(self, urls, maxcount):
        while self.index <= maxcount:
            if not self.linkList.isUnvisitedEmpty():
                visitUrl = self.linkList.getUnvisitedTop()
                if visitUrl == None or visitUrl == "":
                    continue
                links = self.getHtml(visitUrl)
                self.linkList.addVisitedUrl(visitUrl)
                
                if links != None:
                    for link in links:
                        if link[1][0:4] == 'http':
                            self.linkList.addUnvisitedUrl(link[1])
                            #print link[1]              
    
    def getHtml(self, url):
        output = open('./html1/' + self.transNum() + '.html', 'w')
        pattern = re.compile(r'<a(.*?)href="(.*?)"(.*?)>(.*?)</a>')
        
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent, 'Referer': 'http://www.baidu.com' }
        request = urllib2.Request(url, headers=headers)
        
        try:
            response = urllib2.urlopen(request)
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason
            return None
        else:
            #print self.index
            
            # get html file
            content = response.read()
            print self.index
            output.write(content)
            output.close()
            
            self.index = self.index + 1
            
            # re parse, refresh visited/unvisited list
            links = re.findall(pattern, content)
            return links   
    
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
    #main("http://www.baidu.com", 10)
    #main(["http://www.baidu.com", "http://www.sohu.com"], 1000)
    main("http://www.sina.com", 10)