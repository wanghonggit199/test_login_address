from appium import webdriver

caps = {}
# 必填-且正确
caps['platformName'] = 'Android'
# 必填-且正确
caps['platformVersion'] = '5.1'
# 必填
caps['deviceName'] = '192.168.56.101:5555'
# toast
caps['automationName'] = 'Uiautomator2'
# APP包名 /
caps['appPackage'] = 'com.tencent.news'
# 中文
caps['unicodeKeyboard'] = True
caps['resetKeyboard'] = True
# 启动名 # /
caps['appActivity'] = '.ui.NewsDetailActivity'
# 获取driver
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
# 当前环境
print("当前环境：", driver.context)
print("当前所有环境：",driver.contexts)
# 隐式等待
driver.implicitly_wait(30)
# 新闻
driver.find_element_by_xpath("//*[contains(@text,'习近平在河南')]").click()
# 点击后所有环境
print("点击后所有环境：",driver.contexts)
# 切换环境 selenium环境
driver.switch_to.context("WEBVIEW_com.tencent.news")
result = driver.find_element_by_css_selector("p").text
print(result)
