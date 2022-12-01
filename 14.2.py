
import json
import re

import requests
from bs4 import BeautifulSoup


def get_emails(url):
  
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    emails = soup.find_all('a', href=re.compile(r'mailto:'))
    return [email.get_text() for email in emails]

def get_domains(emails):
   
    domains = {}
    for email in emails:
        domain = email.split('@')[1]
        if domain in domains:
            domains[domain] += 1
        else:
            domains[domain] = 1
    return domains

def main():

    url = 'https://safety.olx.ua/'
    emails = get_emails(url)
    domains = get_domains(emails)
    with open('task2.json', 'w') as file:
        json.dump(domains, file)

if __name__ == '__main__':
    main()