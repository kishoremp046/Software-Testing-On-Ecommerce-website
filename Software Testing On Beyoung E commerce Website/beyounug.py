import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

class BeYoungTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--start-minimized")
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.implicitly_wait(10)
        cls.driver.get('https://www.beyoung.in/')
        print("Opened BeYoung website")

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()
        print("Closed the browser")

    def test_01_title_verification(self):
        time.sleep(3)
        if "Beyoung" in self.driver.title:
            print("Title verification passed")
        else:
            print("Title verification failed")

    def test_02_maximize_browser(self):
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        print("Maximized the browser")

    def test_03_click_sections(self):
        sections = ["MEN", "WOMEN", "COMBOS", "CARGO JOGGERS", "MEN'S SHIRTS"]
        for section in sections:
            try:
                section_element = self.driver.find_element(By.LINK_TEXT, section)
                section_element.click()
                time.sleep(3)
                print(f"Clicked on '{section}' section")
                self.driver.back()
                time.sleep(3)
            except NoSuchElementException:
                print(f"Section '{section}' not found")

    def test_04_search_for_item(self):
        time.sleep(5)
        try:
            # Click on the search icon to display the search box
            search_icon = self.driver.find_element(By.CLASS_NAME, "search-bar")
            search_icon.click()
            time.sleep(2)

            # Locate the search box
            search_box = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[3]/div[2]/div/div[2]/div/input")
            search_box.send_keys('Shirt')
            search_box.send_keys(Keys.RETURN)
            time.sleep(3)
            print("Searched for 'Shirt'")
        except NoSuchElementException:
            print("Search box or icon not found")

    def test_05_back_to_home(self):
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        print("Navigated back to home page")

    def test_06_forward_to_search_results(self):
        time.sleep(3)
        self.driver.forward()
        time.sleep(3)
        print("Navigated forward to search results page")

    def test_07_verify_watch_in_title(self):
        time.sleep(3)
        if "Shirt" in self.driver.title:
            print("Verified 'Shirt' in title")
        else:
            print("Verification of 'Shirt' in title failed")

    def test_08_scroll_down(self):
        time.sleep(3)
        # Scroll down gradually
        scroll_pause_time = 0.5
        screen_height = self.driver.execute_script("return window.innerHeight")
        scroll_height = self.driver.execute_script("return document.body.scrollHeight")

        for i in range(0, scroll_height, screen_height):
            self.driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(scroll_pause_time)
        time.sleep(3)
        print("Scrolled down the page gradually")

    def test_09_click_on_specific_item(self):
        time.sleep(3)
        # Search for the specific item by name
        specific_item = self.driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/div/div[2]/div[3]/div[25]/a/div/h2")

        # Click on the specific item
        specific_item.click()
        time.sleep(3)
        print("Clicked on the first item from search results")

    def test_10_add_specific_item_to_cart(self):

        # Wait for the size options to be present
        size_options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/div[4]/section[1]/div/div[2]/div[6]/ul/li[2]/div/div[2]/div[2]/p"))
        )
        if size_options:
            # Click on the first available size option
            size_options[0].click()
            time.sleep(1)
            print("Selected size:", size_options[0].text)
        else:
            print("No size options found")

        # Click on the "Add to Cart" button
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[4]/section[1]/div/div[2]/div[8]/div[1]/a"))
        )
        add_to_cart_button.click()
        time.sleep(3)
        print("Added item to the cart")

    def test_11_check_cart_for_added_item(self):
        # Click on the cart icon to view the cart
        cart_icon = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "add-cart-icon"))
        )
        cart_icon.click()
        time.sleep(3)
        print("Clicked on the cart icon")

    def test_12_quit_browser(self):
        time.sleep(3)
        self.driver.quit()
        print("Quit browser")


if __name__ == "__main__":
    unittest.main()