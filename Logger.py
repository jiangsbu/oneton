#!/user/bin/env python
'''
redirect stdout to file and terminal from
http://stackoverflow.com/questions/14906764/how-to-redirect-stdout-to-file-and-console-with-scripting

to use
sys.stdout = Logger()
'''
import sys

class Logger(object):
    def __init__(self,fn='logfile.log'):
        self.terminal = sys.stdout
        self.log = open(fn, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass    
