from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

driver = webdriver.Edge()

driver.get("https://passport2.chaoxing.com/login?fid=18078&refer=http://i.mooc.chaoxing.com/space/index.shtml")
driver.find_element_by_id('unameId').clear()
driver.find_element_by_id('unameId').send_keys("201714600323")
driver.find_element_by_id('passwordId').clear()
driver.find_element_by_id('passwordId').send_keys("zxz19991031")
driver.find_element_by_id('numcode').clear()
driver.find_element_by_id('numcode').send_keys("")
WebDriverWait(driver, 3600, 0.5).until(
    EC.title_contains("泛雅")
    )
sleep(0.5)
# TODO: OCR验证码
# Log in
driver.switch_to_frame('frame_content')
WebDriverWait(driver, 5, 0.5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "Mdelc2dt"))
    )
class_list = driver.find_elements_by_css_selector('h3.clearfix')
all_old_handles = driver.window_handles
class_list[3].click()
# Class

all_handles = driver.window_handles
for handle in all_handles:
    if handle not in all_old_handles:
        driver.switch_to_window(handle)

# Enter the new page
WebDriverWait(driver, 10, 0.5).until(
    EC.title_contains("学习进度")
    )
# Waiting for the page to load

orange_list = driver.find_elements_by_xpath('//em[@class="orange"]/ancestor::h3/span[@class="articlename"]')

orange_list[0].click()
# Waiting for the page to load

WebDriverWait(driver, 3600, 0.5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "tabtags"))
    )
driver.find_element_by_xpath("//span[@title='视频']")

iframe = driver.find_element_by_xpath('//iframe[@id="iframe"]')
driver.switch_to_frame(iframe)
iframe = driver.find_element_by_xpath('//iframe[@class="ans-attach-online ans-insertvideo-online"]')
driver.switch_to_frame(iframe)

WebDriverWait(driver, 5, 0.5).until(
    EC.presence_of_all_elements_located((By.ID, "reader"))
    )
sleep(3)

#right_click = driver.find_element_by_xpath('//html[@class="x-border-box x-strict"]')
#ActionChains(driver).context_click(right_click).perform()
mouse = driver.find_element_by_xpath('//html[@class="x-border-box x-strict"]')
mouse.click()
while True:
    ActionChains(driver).move_to_element(mouse).perform()

print(len(orange_list))
