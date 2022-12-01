import json
import requests


def get_links(url):
    response = requests.get(url)
    return response.text.count('ref')

def main():
    list_of_urls = []
    for i in range(5):
        list_of_urls.append(input('Введіть URL-адресу: '))
    dict_of_urls = {}
    for url in list_of_urls:
        dict_of_urls[url] = get_links(url)
    with open('14.1.json', 'w') as file:
        json.dump(dict_of_urls, file)

if __name__ == '__main__':
    main()