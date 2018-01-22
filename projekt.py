import json
import ssl
import urllib.request

from pprint import pprint

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('Podaj 3 znakowy symbol kryptowaluty np. BTC - bitcoin')
kwal = input()
print('Podaj 3 znakowy symbol waluty, w której ma być podana cena(PLN,EUR.USD,BTC)')
wal = input()

page = 'https://bitbay.net/API/Public/'+kwal.upper()+wal.upper()+'/ticker.json'
site = urllib.request.urlopen(page, context=ctx)

data = json.loads(site.read())

print(data['vwap'])