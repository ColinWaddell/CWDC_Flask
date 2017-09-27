import os

def get_page_details(page):

  filename = 'content/%s.md' % page
  try:
    return {
      'edited': os.path.getmtime(filename),
      'created': os.path.getctime(filename)
    }

  except FileNotFoundError:
    return {}