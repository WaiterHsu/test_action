print('hello world, haha')

import time
import requests
import json
import math

#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from RPA.Browser.Selenium import Selenium


# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://shopee.tw/flash_sale')
# driver.set_window_size(1280,1400)
# #driver.refresh()

# driver.find_element_by_xpath(f'//*[@id="main"]/div/div[2]/div/div/div/div[3]/div/div/div[1]/ul/li[1]').click()
# time.sleep(2)

# driver.close()

lib = Selenium()

lib.open_available_browser('https://www.playsport.cc/predictgame.php?allianceid=1&gameday=yesterday')
out = lib.get_text('//*[@id="predict_form"]/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/a')
lib.close_browser()
print(out)

try:
  with open('未命名.txt','r') as rf:
    print(rf.readlines())
  print('未命名')
except:
  with open('未命名1.txt','r') as wf:
    print(wf.readlines())
  print('未命名1')
  
  

from datetime import datetime
a = datetime.now()
print(a)
try:
  with open('未命名.txt','w') as wf:
    wf.write('haha')
except:
  print('error')

  


