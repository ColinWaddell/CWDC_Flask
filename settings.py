''' A place to store the site details '''

from key import SECRET_KEY

class Settings(): # pylint: disable=too-few-public-methods
    ''' Stash anything in here '''
    title = 'ColinWaddell.com'
    spacer = "::"
    key = SECRET_KEY
    email_from = 'mrcolin+server@gmail.com'
    email_to = 'mrcolin+server@gmail.com'
    email_subject = 'WEBSITE CONTACT FORM'
