from GoogleNews import GoogleNews
from time import sleep
import os

while True:
    print('-'*12,'Notícias','-'*12)
    palavra = input('Digite uma palavra chave: ')
    print()
    noticia = GoogleNews(lang='pt-BR')
    noticia.search(palavra)

    for i in range(3):
        sleep(1)
        print()
        print(noticia.results()[i]['media'].upper())
        print(f'{noticia.results()[i]["title"]} - {noticia.results()[i]["date"]}')
        print(noticia.results()[i]['link'])
        print(noticia.results()[i]['desc'])

    print()
    input('Tecle Enter para repetir')
    os.system('cls')