import os

from com.TestSettings.Settings import Settings
from com.Utility.Tool import Tool


class SystemReport(object):
    """description of class"""
    planInfoTemplate: str = None
    planInfoHtml: str = None
    settings: Settings = None

    def __init__(self):
        self.settings = Settings.getSettings()
        self.planInfoTemplate = os.getcwd() + "\\TestResult\\PlanInfoTemplate.html"
        self.planInfoHtml = self.settings.CurrentTestResultFolder + \
            '\\' + self.settings.planFile + ".html"

    def CreatePlanInfoReport(self):
        if not os.path.exists(self.planInfoHtml):
            Tool.createFile(self.planInfoHtml)

    def writeSystemInfo_toHtml(self):
        PIT = Tool.readFile(self.planInfoTemplate)
        PIT = PIT.replace("TestPlanStartTime",
                          self.settings.testPlanResult.TestPlanStartTime)
        PIT = PIT.replace("TestPlanEndTime",
                          self.settings.testPlanResult.TestPlanEndTime)
        PIT = PIT.replace("TotalCount", str(
            self.settings.testPlanResult.TotalCount))
        PIT = PIT.replace("allScenarioPassedCount", str(
            self.settings.testPlanResult.allScenarioPassedCount))
        PIT = PIT.replace("allScenarioFailedCount", str(
            self.settings.testPlanResult.allScenarioFailedCount))
        PIT = PIT.replace("allScenarioPassPercentage",
                          self.settings.testPlanResult.allScenarioPassPercentage)
        PIT = PIT.replace("allScenarioFailPercentage",
                          self.settings.testPlanResult.allScenarioFailPercentage)

        Tool.writeFile(self.planInfoHtml, PIT)
