import requests
import time
from threading import Thread


def get_html(link):
    text = requests.get(link)
    print(link, len(text.text))


links = ['https://yandex.ru', 'https://github.com', 'https://www.google.ru',
             'https://rambler.ru', 'https://www.mail.ru']
threads = [Thread(target=get_html, args=[links[i]]) for i in range(5)]

t_1 = time.time()
for i in range(5):
    print(get_html(links[i]))
print(f'Время последовательного выполнения: {time.time() - t_1}')

t_2 = time.time()
for start in threads:
    start.start()
for j in threads:
    j.join()
print(f'Время параллельного выполнения: {time.time() - t_2}')


if t_2>t_1:
	print ("Параллельный запуск быстрее")
else:
	print ("Последовательный запуск быстрее")