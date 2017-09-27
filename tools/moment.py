from jinja2 import Markup
from time import gmtime, strftime
 
class moment(object):
 
    def __init__(self, timestamp=None):
        self.timestamp = timestamp if timestamp else gmtime()
 
    def pretty_time(self):
        return Markup(strftime('%m/%d/%Y', gmtime(self.timestamp)))