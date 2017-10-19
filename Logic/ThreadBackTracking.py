import threading
import time
import logging
from cgi import log

logging.basicConfig(level = logging.DEBUG, format= '[%(levelname)s](%(threadName)-s) %(message)s')



class ThreadBackTracking(threading.Thread):
    def __init__(self, group=None, target=None, name=None, 
        args=(), kwargs=None, verbose=None):
        threading.Thread.__init__(self, target= ThreadBackTracking.run, name=name)
        
    def run(self):
        threading.Thread.run(self)
        pass
    
    def backtracking(self):
        pass
        
        
        