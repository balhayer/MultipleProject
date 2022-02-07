from selenium.common.exceptions import UnexpectedAlertPresentException

driver = webdriver.Chrome()
driver.get('https://www.google.com')

while True:
    try:
        driver.execute_script("var a = prompt('Enter a number');document.body.setAttribute('user-manual-input', a)")
        sleep(10)  # must 
        print(driver.find_element_by_tag_name('body').get_attribute('user-manual-input')) # get the text
        break

     except (UnexpectedAlertPresentException):
        pass



from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://gma-threads4thought.com/")

for element in driver.find_elements_by_tag_name('script'):
    script_text = element.get_attribute('innerHTML')
    if 'product.variants[' not in script_text:
        continue
    print('***********************************************************')
    index = 0
    while True:
        start = script_text[index:].find('product.variants[')
        if start == -1:
            break
        start += index
        end = script_text[start:].find(';') + start
        print(script_text[start:end])
        index = end

driver.close()