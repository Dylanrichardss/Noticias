from GoogleNews import GoogleNews
from time import sleep

print('-'*12,'Notícias','-'*12)
palavra = input('Digite uma palavra chave: ')
print()
noticia = GoogleNews(lang='pt-BR')
noticia.search(palavra)

for i in range(3):
    sleep(1)
    if noticia.results()[i]["media"] == 'Poder360':
        print(noticia.results()[i+3]['media'].upper())
        print(f'{noticia.results()[i+3]["title"]} - {noticia.results()[i+3]["date"]}')
        print(noticia.results()[i+3]['link'])
        print(noticia.results()[i+3]['desc'])
    else:
        print(noticia.results()[i]['media'].upper())
        print(f'{noticia.results()[i]["title"]} - {noticia.results()[i]["date"]}')
        print(noticia.results()[i]['link'])
        print(noticia.results()[i]['desc'])

input('Pressione qualquer tecla para sair')