from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as ec


def xq_text_text(wd, text):
    element = wd.until(ec.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[@text="{text}"]')))
    return element