import streamlit as st
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

URL = "https://marvelsnapzone.com/news/patch-notes/"
XPATH = "//*[@class='ui-mainview-block eventpath-wrapper']"
TIMEOUT = 20

st.title("Test Selenium 3")
st.markdown("You should see some cards")

firefoxOptions = Options()
firefoxOptions.add_argument("--headless")
firefoxOptions.add_argument('--disable-dev-shm-usage')
firefoxOptions.add_argument('--disable-extensions')
firefoxOptions.add_argument('--disable-gpu')
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(
    options=firefoxOptions,
    service=service,
)
driver.get(URL)

st.code(driver.page_source)

# try:
#     WebDriverWait(driver, TIMEOUT).until(
#         EC.visibility_of_element_located((By.XPATH, XPATH,))
#     )

# except TimeoutException:
#     st.warning("Timed out waiting for page to load")
#     driver.quit()

# time.sleep(10)
# elements = driver.find_elements_by_xpath(XPATH)
# st.write([el.text for el in elements])
# driver.quit()