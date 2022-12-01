# Task2

def url():
    n = int(input('Введіть кількість адрес: '))
    url_list = []
    for i in range(n):
        url = input('Введіть адресу: ')
        url_list.append(url)
    return url_list


def protocol(url_list):
    for i in range(len(url_list)):
        if url_list[i].startswith('http://'):
            url_list[i] = url_list[i].replace('http://', '')
        elif url_list[i].startswith('https://'):
            url_list[i] = url_list[i].replace('https://', '')
    return url_list


if __name__ == '__main__':
    print(protocol(url()))