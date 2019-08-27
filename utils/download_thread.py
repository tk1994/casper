import threading
import requests
from utils.writer_thread import writer_thread
from tasks import cel

class download_thread(threading.Thread):
    def __init__(self, threadID, fileName, url, startofFile, end):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.fileName = fileName
        self.url = url
        self.startofFile = startofFile
        self.end = end
    def run(self):
        number_of_writers = 3
        print("starting download thread" + str(self.threadID))
        headers = {'Range': 'bytes=%d-%d' % (self.startofFile, self.end)}
        r = requests.get(self.url, headers=headers, stream=True) 
        download_length = int(r.headers.get('content-length'))
        part_size = int(download_length / number_of_writers)
        if (part_size * number_of_writers) < download_length:
            number_of_writers += 1
        streamArr = r.content
        
        for i in range(number_of_writers):
            # t = writer_thread(i, self.fileName, r, (self.startofFile + (download_length*i)))
            if i == number_of_writers - 1:
                startIndex = part_size * i
                endIndex = startIndex + (download_length - (part_size * i))
            else:
                startIndex = part_size * i
                endIndex = startIndex + part_size
            # print(type(r.content))
            t = writer_thread(i, self.fileName, streamArr[startIndex:endIndex], (self.startofFile + (i * part_size)))
            t.start()
        

        print("exiting thread" + str(self.threadID))
