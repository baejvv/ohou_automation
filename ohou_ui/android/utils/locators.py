from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as ec


def xq_text(wd, text):
    element = wd.until(ec.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[@text="{text}"]')))
    return element

def xq_con_text(wd, text):
    element = wd.until(ec.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[contains(@text,"{text}")]')))
    return element

def xq_access(wd, accessbility_id):
    element = wd.until(ec.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, f'{accessbility_id}')))
    return element