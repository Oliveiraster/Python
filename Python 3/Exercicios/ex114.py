import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.erro.URLError:
    print('Deu erro!!')
else:
    print('Deu Certo!!')
    print(site.read())
