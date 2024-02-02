"""
write a function that accepts a list of url strings in args and
returns what server the website is using. The answer could look something like this:

# URL                     Server
# -------------------------------------
# https://www.delfi.lt/   DWS
# https://www.alfa.lt/    nginx/1.10.3 (Ubuntu)
# https://www.15min.lt/   nginx
# https://www.lrytas.lt/  shield
# http://www.google.com/  gws
"""
import requests

urls = [
    'https://www.delfi.lt/',
    'https://www.15min.lt/',
    'https://www.lrytas.lt/',
    'https://www.vz.lt/',
    'https://www.bernardinai.lt/',
    'https://www.tv3.lt/',
    'https://www.lrt.lt/',
    'https://www.seb.lt/',
    'https://www.swedbank.lt/',
    'https://www.cvbankas.lt/',
    'https://www.cvonline.lt/',
    'https://www.autobilis.lt/',
    'https://www.aruodas.lt/',
    'https://www.skelbiu.lt/'
]


def get_servers(url_list):
    print('URL                                       SERVER')
    print('---------------------------------------------------')
    for url in url_list:
        r = requests.get(f'{url}')
        try:
            server = r.headers['server']
            print(f'{url}                   {server}')
        except KeyError or ValueError:
            print(f'{url}                   Server not found')


get_servers(urls)

