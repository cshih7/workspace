
# so far, I've downloaded selenium package. I've also downloaded "Chrome driver"? have not downloaded the web driver part...


import time
from utils.driver import get_driver

driver = get_driver()

driver.get('http://www.google.com/xhtml')
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()

'''
# to send login information to a website
username = browser.find_element_by_id("username_id") #username form field
password = browser.find_element_by_id("password_id") #password form field

username.send_keys("my_username")
password.send_keys("my_password")

submitButton = browser.find_element_by_id("submit_button_id") 
button.click() 

#Retrieving the inner HTML
browser.get("http://example.com/page.php") #navigate to page behind login
innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string