from selenium.webdriver.common.by import By


class Naukri(object):

    def __init__(self):
        self.login_url = 'https://login.naukri.com'
        self.tb_username = (By.ID, 'usernameField')
        self.tb_password = (By.ID, 'passwordField')
        self.btn_submit = (By.XPATH, '//button[text()="Login"]')

        self.lnk_skip_and_continue = (By.XPATH, '//input[@value="Skip and Continue"]')
        self.btn_my_naukri = (By.XPATH, '//div[@class="mTxt" and contains(text(),"My Naukri")]')
        self.btn_logout = (By.XPATH, '//*[@title="Logout"]')
        self.btn_edit_profile = (By.XPATH, '//*[@title="Edit Profile"]')
        self.input_upload_cv = (By.XPATH, '//input[@id="attachCV"]')
        self.lbl_upload_date = (By.CSS_SELECTOR, 'span.updateOn')



