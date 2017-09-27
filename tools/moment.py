from jinja2 import Markup
from time import gmtime, strftime
 
class moment(object):
 
    def __init__(self, timestamp=None):
        self.timestamp = timestamp
 
    def pretty_time(self):
        return Markup(strftime('%d/%m/%Y', gmtime(self.timestamp)))