import os

def get_page_details(page):

  filename = 'content/%s.md' % page
  try:
    return {
      'edited': os.path.getctime(filename)
    }
  except FileNotFoundError:
    return {}