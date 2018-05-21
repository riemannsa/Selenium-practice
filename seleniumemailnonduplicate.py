from selenium import webdriver
import re
driver=webdriver.Chrome()
driver.get('http://python.org')
doc=driver.page_source

#emails=re.findall(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)",doc) #does not work

emails=re.findall(r'[\w\.-]+@[\w\.-]+',doc)
myfile=open('EmailList.txt','w')
myfile.write('Below is the email list from this Website:\n')
for email in emails:
    myfile.write(str(email)+'\n')
myfile.close()
with open ('EmailList.txt')as result:
    uniqlines=set(result.readlines())
    with open('NonDuplicateEmailList.txt','w')as rmdup:
        rmdup.writelines(set(uniqlines))
result.close()
rmdup.close()
driver.quit()
