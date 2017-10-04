''' Handle the details of content pages '''

import os

def get_page_details(page):
    ''' return a dictionary with the details of a page '''
    filename = 'content/%s.md' % page
    try:
        return {
            'edited': os.path.getctime(filename)
        }
    except FileNotFoundError:
        return {}
