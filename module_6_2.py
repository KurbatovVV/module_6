
import time
from threading import Thread
from datetime import datetime 
time.sleep(3)
print("Параллельный запуск")

def get_thread(thread_name):
	print(f'Поток №', {thread_name})

sec_2=datetime.now()

threads=[Thread(target=get_thread, args=(i+1,)) for i in range(5)]

for t in threads:
	t.start()
for t in threads:
	t.join()

print('time ', (datetime.now() - sec_2).microseconds)
#--------------------------------------------------------------------------------------#
time.sleep(3)
print("Последовательный запуск")

def get_thread(thread_name):
	time.sleep(1)
	print(f'Поток №', {thread_name})
sec_1=datetime.now()
for i in range(5):
	get_thread(i+1)

print('time ', (datetime.now() - sec_1).microseconds)

if sec_2<sec_1:
	print ("Параллельный запуск быстрее")
else:
	print ("Последовательный запуск быстрее")




