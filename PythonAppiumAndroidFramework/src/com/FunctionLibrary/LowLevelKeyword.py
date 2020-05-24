"""this is the place to create low level keyword like click, set function"""
from appium.webdriver.common.mobileby import By
from src.com.Enumeration.StepResult import StepResult
from src.com.TestPlanInfo.TestStepResult import TestStepResult
from src.com.TestSettings.Settings import Settings
from src.com.Utility.Tool import Tool


class LowLevelKeyword():
    '''LowLevelKeyword class'''
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
            self.testStepResult.stepResult = StepResult.Passed
            self.testStepResult.endTime = Tool.CurrentTime()
            self.testStepResult.stepLog = str(self.testStepResult.endTime) + ' ' + \
                func.__name__ + ' execution was ' + self.testStepResult.stepResult.name
        finally:
            fileName = tool.RanString
            Tool.saveScreenShot(
                self.settings.wedriver,
                self.settings.CurrentScriptResultFolder + '\\' + fileName + '.png')
            self.testStepResult.Actual = fileName + '.png'
        return self.testStepResult

    def launchApp(self, command_executor):
        self.settings.createWebDriver(command_executor)

    def click(self, elementExpression):
        __webelement = self.findobject(elementExpression)
        __webelement.click()

    # find a mobile element
    def findobject(self, elementExpression: dict):
        selector = list(elementExpression.keys())[0]
        objectstring = list(elementExpression.values())[0]
        if selector == 'id':
            by = By.ID

        __webelement = self.settings.wedriver.find_element(
            by, objectstring)
        return __webelement
