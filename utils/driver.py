import os
from selenium import webdriver


def get_driver(browser='chrome'):
  print 'Initializing driver...'

  if browser == 'chrome':
    driver = webdriver.Chrome(os.environ.get('CHROMEDRIVER'))
  elif browser == 'firefox':
    driver = webdriver.Firefox()
  else:
    driver = webdriver.PhantomJS()

  driver.set_page_load_timeout(60)

  return driver