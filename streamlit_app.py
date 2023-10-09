# import streamlit as st
# import time

# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from webdriver_manager.firefox import GeckoDriverManager

# URL = "https://www.unibet.fr/sport/football/europa-league/europa-league-matchs"
# XPATH = "//*[@class='ui-mainview-block eventpath-wrapper']"
# TIMEOUT = 20

# st.title("Test Selenium")
# st.markdown("You should see some random Football match text below in about 21 seconds")

# firefoxOptions = Options()
# firefoxOptions.add_argument("--headless")
# service = Service(GeckoDriverManager().install())
# driver = webdriver.Firefox(
#     options=firefoxOptions,
#     service=service,
# )
# driver.get(URL)

# st.code(driver.page_source)

# try:
#     WebDriverWait(driver, TIMEOUT).until(
#         EC.visibility_of_element_located((By.XPATH, XPATH,))
#     )

# except TimeoutException:
#     st.warning("Timed out waiting for page to load")
#     driver.quit()

# # time.sleep(10)
# # elements = driver.find_elements_by_xpath(XPATH)
# # st.write([el.text for el in elements])
# # driver.quit()

import streamlit as st

"""
## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's Community Cloud.

Fork this repo, and edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:
"""

with st.echo():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    @st.experimental_singleton
    def get_driver():
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')

    driver = get_driver()
    driver.get("http://example.com")

    st.code(driver.page_source)