from threading import Timer, Thread, Event
from datetime import datetime


class perpetualTimer():

    def __init__(self, t, hFunction):
        self.t = t
        self.hFunction = hFunction
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.daemon = True
        self.thread.start()

    def cancel(self):
        self.thread.cancel()

# def printer():
#     print('ipsem lorem')
#
#
# t = perpetualTimer(5, printer)
# t.start()
