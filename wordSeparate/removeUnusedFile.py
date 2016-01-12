import os

inputDir = os.listdir('final_sohu')
outputDir = os.listdir('html_sohu')

for txt in outputDir:
	fileNo = txt[0:4]
	file = fileNo+'.txt'
	if file in inputDir:
		continue
	else:
		os.remove('html_sohu/'+txt)