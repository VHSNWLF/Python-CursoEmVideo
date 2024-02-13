import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com')
except:
    print('deu erro')
else:
    print('deu certo')