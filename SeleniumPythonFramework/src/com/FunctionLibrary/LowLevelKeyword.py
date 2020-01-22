from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from com.Enumeration.StepResult import StepResult
from com.FunctionLibrary.webdriverFractory import webdriverFactory
from com.TestPlanInfo.TestStepResult import TestStepResult
from com.TestSettings.Settings import Settings
from com.Utility.Tool import Tool


class LowLevelKeyword():
    """this is the place to create low level keyword like click, set function"""
    testStepResult: TestStepResult = None

    def __init__(self):
        self.testStepResult = TestStepResult()
        self.settings = Settings.getSettings()

    def _deco(self, func, *args):
        tool = Tool()
        self.testStepResult.startTime = Tool.CurrentTime()
        try:
            func(*args)
        except Exception as e:
            self.settings.isRunable: bool = False
            self.testStepResult.endTime = Tool.CurrentTime()
            self.testStepResult.stepResult = StepResult.Error
            self.testStepResult.stepLog = str(self.testStepResult.endTime) + ' ' + func.__name__ + \
                ' execution was ' + StepResult.Error.name + \
                '. Actual exception : ' + str(e)
        else:
            webdriverFactory.waitforready(self.settings.wedriver)
            self.testStepResult.stepResult = StepResult.Passed
            self.testStepResult.endTime = Tool.CurrentTime()
            self.testStepResult.stepLog = str(self.testStepResult.endTime) + ' ' + \
                func.__name__ + ' execution was ' + self.testStepResult.stepResult.name
        finally:
            fileName = tool.RanString
            Tool.saveScreenShot(
                self.settings.wedriver, self.settings.CurrentScriptResultFolder + '\\' + fileName + '.png')
            self.testStepResult.Actual = fileName + '.png'
            return self.testStepResult

    def launchBrowser(self, url):
        self.settings.wedriver.get(url)
        self.settings.wedriver.maximize_window()

    def setText(self, elementExpression, text):
        __webelement = self.findobject(elementExpression)
        __webelement.send_keys(text)

    def click(self, elementExpression):
        __webelement = self.findobject(elementExpression)
        __webelement.click()

    def select(self, elementExpression, value):
        __webelement = self.findobject(elementExpression)
        __webelement.select_by_value(value)

    def doubleClick(self, elementExpression):
        __webelement = self.findobject(elementExpression)
        action = ActionChains(self.settings.wedriver)
        action.double_click(__webelement).perform()

    def moveToElement(self, elementExpression):
        __webelement = self.findobject(elementExpression)
        action = ActionChains(self.settings.wedriver)
        action.move_to_element(__webelement).perform()

    def checkElementDisplayed(self, elementExpression):
        __webelement = self.findobject(elementExpression)
        if not __webelement.is_displayed():
            raise Exception('webelement is not displayed')

    def checkElementEnabled(self, elementExpression):
        __webelement = self.findobject(elementExpression)
        if not __webelement.is_enabled():
            raise Exception('web element is not enabled')

    def getProperty(self, elementExpression, propertyName):
        __webelement = self.findobject(elementExpression)
        return __webelement.get_property(propertyName)

    def getAttribute(self, elementExpression, attributeName):
        __webelement = self.findobject(elementExpression)
        return __webelement.get_attribute(attributeName)

    def getText(self, elementExpression):
        __webelement = self.findobject(elementExpression)
        return __webelement.text

    def getCSSValue(self, element, cssPropertyName):
        __webelement = self.findobject(element)
        return __webelement.value_of_css_property(cssPropertyName)

    def clearText(self, elementExpression):
        __webelement = self.findobject(elementExpression)
        __webelement.clear()

    def switchToWindow(self, index: int):
        self.settings.wedriver.switch_to.window(
            self.settings.wedriver.window_handles[index])

    def switchToFrame(self, frameId):
        self.settings.wedriver.switch_to.frame(
            self.settings.wedriver.find_element_by_xpath('//*[@id="{0}"]'.format(frameId)))

    def switchToMainFrame(self):
        self.settings.wedriver.switch_to_default_content()

    # find a webelement
    def findobject(self, elementExpression: dict):
        wdw = WebDriverWait(self.settings.wedriver, 30)
        selector = list(elementExpression.keys())[0]
        objectstring = list(elementExpression.values())[0]
        if selector == 'id':
            by = By.ID
        elif selector == 'xpath':
            by = By.XPATH
        elif selector == 'classname':
            by = By.CLASS_NAME
        elif selector == 'cssselector':
            by = By.CSS_SELECTOR
        elif selector == 'name':
            by = By.NAME
        elif selector == 'tagname':
            by = By.TAG_NAME
        elif selector == 'linktext':
            by = By.LINK_TEXT
        elif selector == 'partiallinktext':
            by = By.PARTIAL_LINK_TEXT

        wdw.until(lambda x: self.settings.wedriver.find_element(by, objectstring))
        __webelement = self.settings.wedriver.find_element(by, objectstring)
        self.settings.wedriver.execute_script(
            "arguments[0].style.border = \"5px solid yellow\"", __webelement)
        return __webelement
