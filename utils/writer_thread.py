import threading

class writer_thread(threading.Thread):
    def __init__(self, threadID, fileName, r, startofFile):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.fileName = fileName
        self.r = r
        self.startofFile = startofFile

    def run(self):
        print("starting writer thread" + str(self.threadID))
        with open(self.fileName, "r+b") as fp: 
    
            fp.seek(self.startofFile)
            fp.write(self.r)
    

        print("exiting writer thread" + str(self.threadID))
