import requests
from bs4 import BeautifulSoup


def menu():
    print('Type "en" if you want to translate from French into English,'
          ' or "fr" if you want to translate from English into French:')
    lang = input()
    print('Type the word you want to translate:')
    word = input()
    print(f'You chose {lang} as a language to translate {word}.')
    if lang == 'fr':
        url = 'https://context.reverso.net/translation/english-french/' + word
    else:
        url = 'https://context.reverso.net/translation/french-english/' + word

    get_translation(url, lang)


def get_translation(url, lang):
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)

    if page.status_code == 200:
        print("200 OK")
        print("Translations")

        soup = BeautifulSoup(page.content, 'html.parser')
        single_words = soup.find_all('button', {'class': 'other-content'})
        words = str(single_words).lstrip('[<button class="other-content" data-negative="')
        words = words.rstrip('" data-other="0">Other translations</button>]')
        words = words.replace('-', '')
        words = words.replace('{', '')
        words = words.replace('}', '')
        words = words.split(' ')
        print(words)

        example_section = soup.find('section', {'id': 'examples-content'})
        from_phrases_words = example_section.find_all('span', class_='text')
        phrases = []
        for i in from_phrases_words:
            phrases.append(i.text.lstrip('\r').lstrip('\n').lstrip(' '))
        print(phrases)

    else:
        print("Trying again")
        for i in range(100000000000):
            c = 1000 * i / 1000 + 12
            get_translation(url)


menu()


