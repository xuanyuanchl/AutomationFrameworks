import os

from com.Enumeration.StepResult import StepResult
from com.TestSettings.Settings import Settings
from com.Utility.Tool import Tool


class DetailsInfoReport(object):
    """description of class"""
    DetailsInfoTemplate: str = None
    DetailsInfoHtml: str = None
    CaseInfoTemplate: str = None
    testStateResult = None

    def __init__(self, testStateRe):
        self.settings = Settings.getSettings()
        self.testStateResult = testStateRe
        self.DetailsInfoTemplate = os.getcwd() + "\\TestResult\\DetailInfoTemplate.html"
        self.DetailsInfoHtml = self.testStateResult.TestStateReportPath
        self.CaseInfoTemplate = os.getcwd() + "\\TestResult\\CaseInfoTemplate.txt"

    def CreateDetailsInfoReport(self):
        if not os.path.exists(self.DetailsInfoHtml):
            Tool.createFile(self.DetailsInfoHtml)

    def writeDetailsInfotoHtml(self):
        DIT = Tool.readFile(self.DetailsInfoTemplate)
        DIT = DIT.replace("TestStateNumber",
                          self.testStateResult.TestStateNumber)
        DIT = DIT.replace("TestStateFile", self.testStateResult.TestStateFile)
        stepInfo = ''
        for sResult in self.testStateResult.TestStepResultCollection:
            CIT = Tool.readFile(self.CaseInfoTemplate)
            CIT = CIT.replace("StepNumber", sResult.StepNumber)
            CIT = CIT.replace("StepDescription", sResult.StepDescription)
            CIT = CIT.replace("StepKeyword", sResult.StepKeyword)
            CIT = CIT.replace("StepParameter", sResult.StepParameter)
            CIT = CIT.replace("StepObjectID", sResult.StepObject)
            CIT = CIT.replace("Expect", sResult.Expect)
            CIT = CIT.replace("Actual", sResult.Actual)
            if sResult.stepResult == StepResult.NotRun:
                CIT = CIT.replace("ResultCategory", "notruncentertext")
            elif sResult.stepResult == StepResult.Error or sResult.stepResult == StepResult.Failed:
                CIT = CIT.replace("ResultCategory", "failedcentertext")
            else:
                CIT = CIT.replace("ResultCategory", "passedcentertext")
            CIT = CIT.replace("StepResult", sResult.stepResult.name)
            CIT = CIT.replace("StepLog", sResult.stepLog)
            stepInfo = stepInfo + CIT + "\r\n"
        DIT = DIT.replace("StepInfo", stepInfo)
        Tool.writeFile(self.DetailsInfoHtml, DIT)
