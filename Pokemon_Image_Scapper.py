from urllib.request import urlopen
import numpy as np
import cv2
import urllib.request
import time
import threading
import math

def get_pokemon(start, end):
    for i in range(start, end):
        try:
            url = 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/'+'{:03d}'.format(i)+'.png'
            request = urllib.request.Request(url)
            response = urlopen(request)
            binary_str = response.read()
            byte_array = bytearray(binary_str)
            numpy_array = np.asarray(byte_array, dtype="uint8")
            image = cv2.imdecode(numpy_array, cv2.IMREAD_UNCHANGED)
            cv2.imwrite("pokedex/" + '{:04d}'.format(i) +'.png', image)
            print("Saved: " + '{:04d}'.format(i) +'.png')

        except Exception as e:
            print(str(e))

start_time = time.time()
thread_list = []
thread_count = 4
image_count = 809

for i in range(thread_count):
    start = math.floor(i * image_count / thread_count) + 1
    end = math.floor(i + 1 * image_count / thread_count) + 1
    thread_list.append(threading.Thread(target=get_pokemon, args=(start,end)))

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

end_time = time.time()
print("Done!")
print("Time Taken : ", round(end_time - start_time,2),'Sec')