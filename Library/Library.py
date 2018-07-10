import os
import time
import re
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects import Naukri


class Library(object):

    def __init__(self):
        self.binary_location = r"/usr/local/bin/chromedriver"
        self.naukri_po = None

    def __enter__(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = Chrome(self.binary_location, chrome_options=options)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print exc_type, exc_val, exc_tb
        self.driver.close()

    def upload_resume_to_naukri(self, username, password):
        self.naukri_po = Naukri()
        upload_date = None

        self.driver.implicitly_wait(30)
        self.driver.get(self.naukri_po.login_url)

        self.driver.find_element(*self.naukri_po.tb_username).send_keys(username)
        self.driver.find_element(*self.naukri_po.tb_password).send_keys(password)
        self.driver.find_element(*self.naukri_po.btn_submit).click()

        try:
            self.driver.find_element(*self.naukri_po.lnk_skip_and_continue).click()
        except Exception as e:
            print " No Skip and Continue Present"

        element_to_hover_over = self.driver.find_element(*self.naukri_po.btn_my_naukri)
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()
        self.driver.find_element(*self.naukri_po.btn_logout)
        print "Naukri Login Successful, Logout Button Exists"

        # Now moving to edit profile
        self.driver.find_element(*self.naukri_po.btn_edit_profile).click()
        print os.getcwd()
        value = 0.4
        while value <= 1:
            self.driver.execute_script("window.scrollTo(0, {}*document.body.scrollHeight);".format(value))
            try:
                element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(self.naukri_po.input_upload_cv)
                )
                print os.getcwd()
                self.driver.find_element(*self.naukri_po.input_upload_cv).send_keys(
                    os.path.join(os.getcwd(), "Profile.docx"))
                print 'Done Successfully'
                time.sleep(10)
                updated_on = self.driver.find_element(*self.naukri_po.lbl_upload_date).text
                if updated_on:
                    upload_date = re.search('Uploaded on (.*)', updated_on).group(1)
                    print "Resume uploaded on :{}".format(upload_date)
                break
            except Exception as e:
                print e.message
                value += 0.1
        return upload_date
