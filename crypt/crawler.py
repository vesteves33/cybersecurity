from bs4 import BeautifulSoup
from collections import Counter
import requests
import operator


def start(url):
    
    word_list = []
    source_code = requests.get(url).text
    
    soup = BeautifulSoup(source_code, 'html.parser')
    
    for post_text in soup.findAll('div', {'class': 'entry-content'}):
        content = post_text.text
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_wordlist(word_list)


def clean_wordlist(wordlist):
    clean_wordlist = []
    for word in wordlist:
        symbols = '!@#$%^&*()_+{}:"<>?/.,;[]-='
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')
        if len(word) > 0:
            clean_wordlist.append(word)
    create_dictionary(clean_wordlist)

def create_dictionary(clean_wordlist):
    word_count = {}
    
    for word in clean_wordlist:
        if word in word_count:
            word_count[word] += 1

        else:
            word_count[word] = 1



    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print("% s: % s " %(key, value))

    c = Counter(word_count)


    top_ten = c.most_common(10)
    

    print(top_ten)


if __name__ == '__main__':
    start('https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar')