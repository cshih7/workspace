
# so far, I've downloaded selenium package. I've also downloaded "Chrome driver"? have not downloaded the web driver part...


import time
from utils.driver import get_driver

driver = get_driver()

driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()