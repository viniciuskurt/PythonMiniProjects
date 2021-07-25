'''
Desenvolvimento de um Web Crawler básico para capturar informações, cadastrar e compreender as mais relevantes
Development of a basic Web Crawler to capture information, register and understand the most relevant ones
'''
from bs4 import BeautifulSoup
import requests
import operator
from collections import Counter

#Função inicia url e salvatodo conteúdo do site numa lista
#Function starts url and save all site content in list
def start(url):

    wordlist = []
    source_code = requests.get(url).text

    #faz a requisição dos dados e transforma em HTML
    #requests the data and transforms it into HTML
    soup = BeautifulSoup(source_code, 'html.parser')

    #procura tudo que existe com div e classe e transforma em string
    #finds everything there is with div and class and turns it into string
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

        #separa o conteúdo buscado em linhas
        #separates the fetched content into lines
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

#função para remover simbolos indesejados da wordlist
#function to remove unwanted symbols from wordlist
def clean_wordlist(wordlist):
    clean_list = []

    for word in wordlist:
        simbols = '!@#$%¨&*()_+`{}^?:><|\,.;/]~´[=-'

        for i in range(0, len(simbols)):
            word = word.replace(simbols[i], '')

        if len (word) > 0:
            clean_list.append(word)
        create_dictionary(clean_list)

#cria um dicionario e faz um contagem de palavras criando uma lista de maior ocorrencias de palavras que há no site
#creates a dictionary and does a word count creating a list of the highest occurrences of words on the site
def create_dictionary(clean_list):
    word_count = {}

    #contador de palavras
    #word counter
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(),
                             key = operator.itemgetter(1)):
        print("% s : % s" % (key, value))

    c = Counter(word_count)


    top = c.most_common(10)
    print(top)

#link da pagina a ser analisada
#link to the page to be analyzed
if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")


