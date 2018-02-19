import re
fo = open("out_nl_20160901_20160909.log","r")
fp = open("output.txt","w+")

trigger=0

tempList=list()
for line in fo:
	if re.search('ers_senderip',line):
		trigger=0
		print trigger
	if trigger==1:
		line=line.split("(")[0]
		line=line[:-1]
		fp.write(line + '\n')
	if re.search('sender_ip',line):
		trigger=1
		print trigger
fo.close()
fp.close()
