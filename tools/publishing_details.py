import os

def get_page_details(page):

  filename = 'content/%s.md' % page
  try:
    return {
      'last_edited': os.path.getmtime(filename)
    }

  except FileNotFoundError:
    return {}