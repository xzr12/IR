.
|-- report
|   |-- report.docx					ʵ�鱨�棨doc)
|   |-- report.pdf					ʵ�鱨�棨pdf��
|-- project
|   |-- IR
|   |   |-- content_sohu/wiki				��ҳ��ȡ���ĵĽ�����貹�䣩
|   |   |-- dic						Ӣ�Ĵʵ�
|   |   |   |-- commonDic.txt
|   |   |   |-- dictionary.txt
|   |   |-- final_sohu/wiki				��ҳ�ִʵĽ��
|   |   |-- skipwords					ͣ�ôʴʵ䣬ͬwordSeparate�ļ����У��貹�䣩
|   |   |   |-- skipContent.txt				����
|   |   |   |-- skipWords_En.txt			Ӣ��
|   |   |-- IR						��ʾ��ش���
|   |   |   |-- __init__.py
|   |   |   |-- settings.py
|   |   |   |-- urls.py					url����
|   |   |   |-- wsgi.py
|   |   |-- testMongo					ǰ�ڲ������ݿ��django���Ӵ���
|   |   |   |-- __init__.py
|   |   |   |-- models.py
|   |   |   |-- tests.py
|   |   |   |-- views.py
|   |   |-- wordCorrection				�����������룬��ʾҳ��
|   |   |   |-- static					ҳ�����jpg��css��js���˴���չ����ʾ
|   |   |   |-- templates				������ʾҳ�棬�˴���չ����ʾ
|   |   |   |-- __init__.py
|   |   |   |-- corrector_CH.py				���ľ���
|   |   |   |-- corrector_EN.py				Ӣ�ľ���
|   |   |   |-- search.py				������أ��������ݴ洢
|   |   |   |-- splitBeforeSearch.py			�ִʡ�ͣ�ôʹ������
|   |   |   |-- models.py				MongoDBģ�Ͷ���
|   |   |   |-- tests.py
|   |   |   |-- views.py				��ʾҳ�����
|   |   |-- manage.py					django��Ŀ���
|   |   |-- html_sohu/wiki.txt				��ҳ�����б�������spider.py��ã��貹�䣩
|   |   |-- title_sohu/wiki.txt				��ҳ�����б���wordSeparate/extractor-title.py��ã��貹�䣩
|   |-- wordSeparate
|   |   |-- extractor-final-en				Ӣ��������ȡ
|   |   |   |-- BeautifulSoup.py
|   |   |   |-- BeautifulSoup.pyc
|   |   |   |-- ExtMainText_English_txt_utf-8.py	Ӣ��������ȡ��utf-8���루���У�
|   |   |-- skipwords					ͣ�ôʱ�
|   |   |   |-- skipContent.txt				����
|   |   |   |-- skipWords_En.txt			Ӣ��
|   |   |-- extractor-final-ch-utf-8.py			����������ȡ��utf-8���루���У�
|   |   |-- extractor-title.py				��ȡ���⣨���У�
|   |   |-- removedUnusedFile.py			ɸѡ�ִʽ����ɾ����Ӧ�������ļ������У�
|   |   |-- skipWords.py				ͣ�ôʹ��ˣ����У�
|   |   |-- splitWords.py				�ִʣ����У�
|   |   |-- spider.py					�������棨���У�
|-- README.txt						��Ŀ���˵��
|-- ����������չʾ.pptx					���չʾppt


ע�������𡢱��롢����˵����doc/report.pdf���岿�֡�
������ע���еĴ���������ʵ�����еġ�wordSeparate����Щ�����������Ҫ�Ƚ�����ص��ļ���