# Taken directly from
# http://stackoverflow.com/questions/2281850/timeout-function-if-it-takes-too-long-to-finish
# answer by Thomas Ahle: http://stackoverflow.com/a/22348885/1141805

"""
Usage:

with timeout(seconds=10):
  time.sleep(12)
"""

import signal

class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)
