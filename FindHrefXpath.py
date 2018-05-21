from selenium import webdriver

driver=webdriver.Chrome()
driver.get('http://google.com')
ids=driver.find_elements_by_xpath('//*[@href]')
for ii in ids:
    print(ii.get_attribute('href'))
driver.close()
