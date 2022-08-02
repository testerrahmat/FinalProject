import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# variable
url = "http://opensource-demo.orangehrmlive.com"
username_login = "Admin"
password_login = "admin123"
search_username = "Charlie.Carter"
search_employee = "Charlie"
from_date = "2022-08-01"
to_date = "2022-08-02"
employee_name_leave = "Orange Test"
name_directory = "Odis"


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    # test case pertama
    def test_search_admin(self):

        driver = self.driver
        driver.get(url)  # buka situs
        time.sleep(5)
        driver.find_element(By.ID, "txtUsername").send_keys(
            username_login)  # isi username
        time.sleep(5)
        driver.find_element(By.ID, "txtPassword").send_keys(
            password_login)  # isi password
        time.sleep(5)
        driver.find_element(By.ID, "btnLogin").click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(By.ID, "welcome").text

        self.assertIn('Welcome', response_data)

        # step lanjutan
        driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
        time.sleep(5)
        driver.find_element(By.ID, "searchSystemUser_userName").send_keys(
            search_username)  # isi username
        time.sleep(5)
        driver.find_element(By.ID, "searchBtn").click()
        time.sleep(5)

        # validasi hasil
        response_data = driver.find_element(
            By.CSS_SELECTOR, "#resultTable > tbody > tr > td:nth-child(2) > a").text

        self.assertIn('Charlie', response_data)

    # test case kedua
    def test_search_pim(self):

        driver = self.driver
        driver.get(url)  # buka situs
        time.sleep(5)
        driver.find_element(By.ID, "txtUsername").send_keys(
            username_login)  # isi username
        time.sleep(5)
        driver.find_element(By.ID, "txtPassword").send_keys(
            password_login)  # isi password
        time.sleep(5)
        driver.find_element(By.ID, "btnLogin").click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(By.ID, "welcome").text

        self.assertIn('Welcome', response_data)

        # step lanjutan
        driver.find_element(By.ID, "menu_pim_viewPimModule").click()
        time.sleep(5)
        driver.find_element(By.ID, "empsearch_employee_name_empName").send_keys(
            search_employee)  # isi employee name
        time.sleep(5)
        driver.find_element(By.ID, "searchBtn").click()
        time.sleep(5)

        # validasi hasil
        response_data = driver.find_element(
            By.CSS_SELECTOR, "#resultTable > tbody > tr > td:nth-child(3) > a").text

        self.assertIn('Charlie', response_data)

    # test case ketiga
    def test_search_leave(self):

        driver = self.driver
        driver.get(url)  # buka situs
        time.sleep(5)
        driver.find_element(By.ID, "txtUsername").send_keys(
            username_login)  # isi username
        time.sleep(5)
        driver.find_element(By.ID, "txtPassword").send_keys(
            password_login)  # isi password
        time.sleep(5)
        driver.find_element(By.ID, "btnLogin").click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(By.ID, "welcome").text

        self.assertIn('Welcome', response_data)

        # step lanjutan
        driver.find_element(By.ID, "menu_leave_viewLeaveModule").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "#calFromDate").send_keys(
            from_date)  # isi from date
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "#calToDate").send_keys(
            to_date)  # isi to date
        time.sleep(5)
        driver.find_element(By.ID, "leaveList_chkSearchFilter_1").click()
        time.sleep(5)
        driver.find_element(By.ID, "leaveList_chkSearchFilter_2").click()
        time.sleep(5)
        driver.find_element(By.ID, "leaveList_txtEmployee_empName").send_keys(
            employee_name_leave)  # isi employee name
        time.sleep(5)
        driver.find_element(By.ID, "searchBtn").click()
        time.sleep(5)

        # validasi hasil
        response_data = driver.find_element(
            By.CSS_SELECTOR, "#resultTable > tbody > tr > td:nth-child(2) > a").text

        self.assertIn('Orange', response_data)

    # test case kelima
    def test_search_directory(self):

        driver = self.driver
        driver.get(url)  # buka situs
        time.sleep(5)
        driver.find_element(By.ID, "txtUsername").send_keys(
            username_login)  # isi username
        time.sleep(5)
        driver.find_element(By.ID, "txtPassword").send_keys(
            password_login)  # isi password
        time.sleep(5)
        driver.find_element(By.ID, "btnLogin").click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(By.ID, "welcome").text

        self.assertIn('Welcome', response_data)

        # step lanjutan
        driver.find_element(By.ID, "menu_directory_viewDirectory").click()
        time.sleep(5)
        driver.find_element(By.ID, "searchDirectory_emp_name_empName").send_keys(
            name_directory)  # isi employee name
        time.sleep(5)
        driver.find_element(By.ID, "searchBtn").click()
        time.sleep(5)

        # validasi hasil
        response_data = driver.find_element(
            By.CSS_SELECTOR, "#resultTable > tbody > tr.odd > td:nth-child(2) > ul > li:nth-child(1) > b").text

        self.assertIn('Odis', response_data)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
