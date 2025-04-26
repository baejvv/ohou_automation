from appium import webdriver
from appium.options.common import AppiumOptions


def setup_prod():
    caps = dict(
        platformName = 'android',
        udid = 'R3CT60P5Y3A',
        automationName = 'uiautomator2',
        appPackage = 'com.android.vending',
        appActivity = 'com.android.vending.AssetBrowserActivity',
        maxTypingFrequency = 10,
        noReset = True,
        forceAppLaunch = True,
        **{'settings[enableMultiWindows]': True},
    )

    wd = webdriver.Remote('http://0.0.0.0:4723', options=AppiumOptions().load_capabilities(caps))
    return wd