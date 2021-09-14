from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class InstagramScrap:
    """Class for Instagram Scrapping Using selenium"""

    def __init__(self):
        """Initialize the InstagramScrap"""
        url = "https://www.instagram.com/"
        # Set the browser as firefox
        self.driver = webdriver.Firefox()
        # Implicit await the browser to load maximum of 10 seconds
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        # Set the browser to full screen
        self.driver.maximize_window()


    def login(self, username, password):
        """This login method accept username and password to login inside the instragram"""
        # Input the username and password then click the login button
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_xpath("//div[text()='Log In']").click()
        try:
            # Check if the username and password are correct
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, "slfErrorAlert")))
            print("Invalid account")
        except:
            pass
        try:
            # If the instagram is asking to save your login info it will choose Not Now
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']")))
            self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
            # If the instagram is asking to turn on notifications it will choose Not Now
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']")))
            self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
        except TimeoutException:
            pass

    def screenshot(self):
        try:
            # It will locate the second post
            article = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//article[2]")))
            # Move to screen location to the second post
            article.location_once_scrolled_into_view
            # Take a screen shot
            self.driver.save_screenshot("screenshot.png")
        except TimeoutException:
            print("No Article can found")
        finally:
            # It will close the browser
            self.driver.quit()



if __name__ == "__main__":
    scrap = InstagramScrap()
    username = "blufipscafe"
    password = "Blufipscafe741"
    scrap.login(username, password)
    scrap.screenshot()
