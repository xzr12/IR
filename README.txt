.
|-- report
|   |-- report.docx					实验报告（doc)
|   |-- report.pdf					实验报告（pdf）
|-- project
|   |-- IR
|   |   |-- content_sohu/wiki				网页提取正文的结果（需补充）
|   |   |-- dic						英文词典
|   |   |   |-- commonDic.txt
|   |   |   |-- dictionary.txt
|   |   |-- final_sohu/wiki				网页分词的结果
|   |   |-- skipwords					停用词词典，同wordSeparate文件夹中（需补充）
|   |   |   |-- skipContent.txt				中文
|   |   |   |-- skipWords_En.txt			英文
|   |   |-- IR						显示相关代码
|   |   |   |-- __init__.py
|   |   |   |-- settings.py
|   |   |   |-- urls.py					url定义
|   |   |   |-- wsgi.py
|   |   |-- testMongo					前期测试数据库和django连接代码
|   |   |   |-- __init__.py
|   |   |   |-- models.py
|   |   |   |-- tests.py
|   |   |   |-- views.py
|   |   |-- wordCorrection				纠错、搜索代码，显示页面
|   |   |   |-- static					页面相关jpg，css和js，此处不展开显示
|   |   |   |-- templates				搜索显示页面，此处不展开显示
|   |   |   |-- __init__.py
|   |   |   |-- corrector_CH.py				中文纠错
|   |   |   |-- corrector_EN.py				英文纠错
|   |   |   |-- search.py				搜索相关，包括数据存储
|   |   |   |-- splitBeforeSearch.py			分词、停用词过滤相关
|   |   |   |-- models.py				MongoDB模型定义
|   |   |   |-- tests.py
|   |   |   |-- views.py				显示页面相关
|   |   |-- manage.py					django项目入口
|   |   |-- html_sohu/wiki.txt				网页链接列表，由爬虫spider.py获得（需补充）
|   |   |-- title_sohu/wiki.txt				网页标题列表，由wordSeparate/extractor-title.py获得（需补充）
|   |-- wordSeparate
|   |   |-- extractor-final-en				英文正文提取
|   |   |   |-- BeautifulSoup.py
|   |   |   |-- BeautifulSoup.pyc
|   |   |   |-- ExtMainText_English_txt_utf-8.py	英文正文提取至utf-8编码（运行）
|   |   |-- skipwords					停用词表
|   |   |   |-- skipContent.txt				中文
|   |   |   |-- skipWords_En.txt			英文
|   |   |-- extractor-final-ch-utf-8.py			中文正文提取至utf-8编码（运行）
|   |   |-- extractor-title.py				提取标题（运行）
|   |   |-- removedUnusedFile.py			筛选分词结果后删掉对应的网络文件（运行）
|   |   |-- skipWords.py				停用词过滤（运行）
|   |   |-- splitWords.py				分词（运行）
|   |   |-- spider.py					网络爬虫（运行）
|-- README.txt						项目相关说明
|-- 检索大数据展示.pptx					答辩展示ppt


注：程序部署、编译、运行说明见doc/report.pdf第五部分。
　　标注运行的代码是我们实际运行的。wordSeparate中有些代码的运行需要先建立相关的文件夹