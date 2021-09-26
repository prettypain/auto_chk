import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys


class student:
    def __init__(self,school,name,pw,birthday):
        self.birthday = birthday
        self.school = school
        self.name = name
        self.pw = str(pw)
        
    def start(self):
        driver = webdriver.Chrome()
        driver.get("https://hcs.eduro.go.kr/")
        driver.find_element_by_id("btnConfirm2").click()
        input_list = driver.find_elements_by_css_selector(".input_text_common")
        input_list[0].click()

        #학교 선택 부분
        driver.find_element_by_id("sidolabel").click()
        city_school_list = driver.find_elements_by_tag_name("option")
        city_school_list[9].click()

        driver.find_element_by_id("crseScCode").click()
        city_school_list[22].click()

        driver.find_element_by_id("orgname").send_keys(self.school)
        driver.find_element_by_id("orgname").send_keys(Keys.RETURN)
        time.sleep(1)

        driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p/a').click()
        driver.find_elements_by_css_selector(".layerFullBtn")[0].click()

        #성명 부분
        input_list[1].click()
        input_list[1].send_keys(self.name)

        #생년월일 부분
        input_list[2].click()
        input_list[2].send_keys(self.birthday)

        driver.find_element_by_id("btnConfirm").click()
        time.sleep(1)
#         try:
#             result = Alert(driver)
#             print(result.text)
#             result.accept()
#         except:
#             print("alert이 없습니다.")
#         time.sleep(0.5)
#         driver.find_element_by_id("extraInfo0").click()
#         time.sleep(0.5)
#         driver.find_element_by_id("btnConfirm").click()
#         time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/input').click()
        time.sleep(0.5)
        for i in self.pw:
            driver.find_element_by_xpath(f'//a[@aria-label="{i}"]').click()
        


        driver.find_element_by_id("btnConfirm").click()
        time.sleep(1)
        driver.find_element_by_class_name("name").click()
        time.sleep(1)
        for i in range(3):
            driver.find_element_by_id("survey_q"+str(i+1)+"a1").click()
        driver.find_element_by_id("btnConfirm").click()
        time.sleep(2)
        # driver.close()


#plz write your status, and it will work.
# me = student(Your_school_name,your_name,your_pw,your_birthday)
# me.start()
