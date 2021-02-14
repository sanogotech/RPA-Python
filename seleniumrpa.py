from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time


# https://realpython.com/modern-web-automation-with-python-and-selenium/

opts = Options()
#opts.set_headless()
#assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://www.macieenligne.ci/')
# title
print("Le titre du site est :" ,browser.title)
wait = WebDriverWait(browser, 10)
browser.get('https://www.macieenligne.ci/particulier')
wait = WebDriverWait(browser, 10)
browser.get('https://www.macieenligne.ci/simuler_facture')

# search_form
#search_form = browser.find_element_by_id('search_form_input_homepage')
#search_form.send_keys('real python')
#search_form.submit()

time.sleep(30) 
#nouvel_index = browser.find_element_by_id("nouvel_index")
nouvel_index = browser.find_element_by_xpath("//input[@id='nouvel_index']")
time.sleep(30) 
nouvel_index.send_keys('1282333')

# results
#results = browser.find_elements_by_class_name('result')
#print(results[0].text)
#print(results)

browser.close()
quit()