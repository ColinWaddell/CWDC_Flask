''' Moment renders template functions there to deal with date and time '''

from time import gmtime, strftime
from jinja2 import Markup


class Moment(object):
    ''' Handle dates and times in flask templates '''
    def __init__(self, timestamp=None):
        self.timestamp = timestamp

    def pretty_datetime(self):
        ''' take a file timestamp and return a prettified version '''
        return Markup(strftime('%H:%m - %d/%m/%Y', gmtime(self.timestamp)))
