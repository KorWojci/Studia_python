import urllib.request as req
import re

url = input()
strona = req.urlopen(url)
a = strona.read()
urllist = re.findall(r'"((http)s?://.*?)"', str(a))

for i in urllist:
    print(i[0])
