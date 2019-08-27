from __future__ import absolute_import, unicode_literals
from flask import request
import requests 
import pdb
import time
from utils.download_thread import download_thread
from tasks import cel
from settings.conn import conn
@cel.task
def download_file_threaded(**kwargs):
    c = conn()
    con = c.con
    idd = str(cel.current_task.request.id)
    number_of_threads = 100
    url_of_file = kwargs['url']
    r = requests.head(url_of_file) 
    file_name = "/home/tushar/Documents/sides/skywritebe/src/data/"+url_of_file.split('/')[-1]
    file_size = int(r.headers['content-length'])

    # con.execute("INSERT INTO status (id,total_size) \
    #    VALUES (1, 3232)")

    part = int(int(file_size) / number_of_threads)
    
    fp = open(file_name, "w") 
    # fp.write('\0' * file_size) 
    fp.close() 
    if (number_of_threads * part) < file_size:
        number_of_threads += 1
    
    for i in range(number_of_threads): 
        start = part * i 
        if i == number_of_threads - 1:
            end = start + (file_size - (part * i))
        else:
            end = start + part 
        t = download_thread(i, file_name, url_of_file, start, end)
        t.start()

    print ('%s downloaded' % file_name) 
    return file_size