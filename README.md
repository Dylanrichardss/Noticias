# Noticias
<b>App Python que busca 3 noticías do assunto que o usuário desejar.</b>

## Demonstração

Ao iniciar o arquivo .py, o usuário poderá digitar um assunto, palavra ou frase.

![image](https://github.com/user-attachments/assets/6e5153cd-14d2-4201-9b06-14b22e289557)



O Script buscará 3 noticías mais recentes sobre o assunto que o usuário digitou.
Ele trará: Mídia que publicou a notícia, o título da matéria, a quanto tempo foi publicada, link da web e a descrição da reportagem. 
O usuário poderá apertar Enter para repetir novas buscas.
![image](https://github.com/user-attachments/assets/feed0d06-e804-497d-bb52-3616473d453b)




## Código
``` bash
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
```
