import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium_task.XL_data import Openpyxl


class Demo(unittest.TestCase):
    driver = None


    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def test_01_window_handling(self):  # Write code for handling multiple windows
        driver = self.driver
        driver.get("https://demo.automationtesting.in/Windows.html")
        driver.find_element(By.XPATH, "//button[text()='    click   ']").click()
        windows = driver.window_handles

        for window in windows:
            driver.switch_to.window(window)
            print(driver.title)

    def test_02_handle_alert_window(self):#Write code for positive and negative scenarios for Alerts
        driver = self.driver
        driver.get("https://demo.automationtesting.in/Alerts.html")
        driver.find_element(By.XPATH, "//button[@onclick='alertbox()']").click()
        driver.switch_to.alert.accept()
        driver.find_element(By.XPATH, "//button[@onclick='alertbox()']").click()
        driver.switch_to.alert.dismiss()
    def test_03_handle_frame(self):#Write code for handling Frames
        driver = self.driver
        driver.get("https://demo.automationtesting.in/Frames.html")
        driver.switch_to.frame("singleframe")
        driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys("iframe")

    def test_04_navigate_manu_sub_manu(self):#Automate Menu and Sub Menu and click on a link in Sub Menu and navigate to the page and click on an element
        driver = self.driver
        driver.get("https://demo.automationtesting.in/FileUpload.html")
        interactions = driver.find_element(By.XPATH, "//a[text()='Interactions ']")
        drag_drop = driver.find_element(By.XPATH, "//a[contains(text(),'Drag and Drop ')]")
        static = driver.find_element(By.XPATH, "//a[contains(text(),'Static ')]")
        my_actions = ActionChains(driver)
        my_actions.move_to_element(interactions).move_to_element(drag_drop).move_to_element(static).click()
        my_actions.perform()
        time.sleep(5)

    def test_05_drop_down(self):# Select multiple options from the dropdown
        driver = self.driver
        driver.get("https://demo.automationtesting.in/Register.html")
        drop_down = Select(driver.find_element(By.ID, "Skills"))
        drop_down.select_by_visible_text("Python")
        time.sleep(5)

    def test_06_file_upload(self):  # How to do file upload in Selenium?
        driver = self.driver
        driver.get("https://demo.automationtesting.in/FileUpload.html")
        driver.find_element(By.ID,"input-4").send_keys("C:/Users/mujah/Desktop/C061 Mohamed.JPG")
        time.sleep(5)

    def test_07_screen_shot(self):  # Write code for taking Screenshot?
        driver = self.driver
        driver.get("https://demo.automationtesting.in/FileUpload.html")
        driver.find_element(By.ID,"input-4").send_keys("C:/Users/mujah/Desktop/C061 Mohamed.JPG")
        driver.save_screenshot("D://WORKSPACE//Projects//selenium_task//selenium_task//screen_short//test1.jpg")
        time.sleep(5)

    def test_08_data_driven(self): #Read data from Excel and given that data as input for login and password and click on submit and validate the popup which says Login is successful

            data_driven = Openpyxl()
            path = "/selenium_task//my_data.xlsx"
            rows =data_driven.get_count_row(path,'Sheet1')
            driver = self.driver
            driver.get("https://demo.guru99.com/test/newtours/")
            for r in range(2,rows+1):
                username = data_driven.read_data(path,"Sheet1",r,1)
                password = data_driven.read_data(path, "Sheet1", r, 2)

                driver.find_element(By.XPATH,"//input[@name='userName']").send_keys(username)
                driver.find_element(By.XPATH,"//input[@name='password']").send_keys(password)
                driver.find_element(By.XPATH, "//input[@name='submit'] ").click()
                time.sleep(5)
            login_msg = driver.find_element(By.XPATH,"//h3[text()='Login Successfully']").text
            assert login_msg == "Login Successfully"

    def test_09_shift_to_window_handling(self):  # How to shift between tabs of the same browser using selenium?
        driver = self.driver
        driver.get("https://demo.automationtesting.in/Windows.html")
        parent_window = driver.current_window_handle
        driver.find_element(By.XPATH, "//button[text()='    click   ']").click()
        windows = driver.window_handles

        for window in windows:
            if window != parent_window:
                driver.switch_to.window(window)
                print(driver.title)

    def test_10_file_upload(self):  # How to do file upload in Selenium?
        driver = self.driver
        my_actions = ActionChains(driver)
        driver.get("https://demo.automationtesting.in/FileUpload.html")
        driver.find_element(By.ID,"input-4").send_keys("D:\my cv\cv mujahith_QA_analayst.pdf")
        time.sleep(5)

    def test_11_file_download (self):  # How to perform download files using selenium?
        driver = self.driver
        driver.get("https://demo.automationtesting.in/FileDownload.html")
        driver.find_element(By.XPATH, "//h2/../div/a").click()
        time.sleep(5)

    def test_13_fins_more_elements (self):  # How to find more than one web element in the list?
        driver = self.driver
        driver.get("https://demo.automationtesting.in/Register.html")
        list_of_elements = driver.find_elements(By.XPATH, '//*[@id="Skills"]')
        for l in list_of_elements:
            print(l.text)

















    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
