from appium import webdriver
from appium.options.common import AppiumOptions

# 플레이스토어
def setup_store():
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

# 오늘의집
def setup_ohou():
    caps = dict(
        platformName = 'android',
        udid = 'R3CT60P5Y3A',
        automationName = 'uiautomator2',
        appPackage = 'net.bucketplace',
        appActivity = 'se.ohou.screen.splash.SplashActivity',
        maxTypingFrequency = 10,
        noReset = True,
        forceAppLaunch = True,
        **{'settings[enableMultiWindows]': True},
    )

    wd = webdriver.Remote('http://0.0.0.0:4723', options=AppiumOptions().load_capabilities(caps))
    return wd
