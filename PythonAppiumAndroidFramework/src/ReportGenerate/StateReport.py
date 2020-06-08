from src.com.TestSettings.Settings import Settings
import os
from src.com.TestPlanInfo.TestCaseResult import TestCaseResult
from src.com.Utility.Tool import Tool
from src.ReportGenerate.DetailsInfoReport import DetailsInfoReport

class StateReport(object):
    """description of class"""
    StateInfoTemplate :str = None
    CaseStateInfoTemplate :str = None
    CaseStateInfoReport :str = None
    planInfoHtml :str = None
    caseSummaryInfoTemplate :str = None
    caseSummaryInfoReportPath :str = None
    settings :Settings = None

    def __init__(self):
        self.settings = Settings.getSettings()
        self.StateInfoTemplate = os.getcwd() + '\\TestResult\\StateInfoTemplate.txt'
        self.CaseStateInfoTemplate = os.getcwd() + '\\TestResult\\CaseStateInfoTemplate.txt'
        self.CaseStateInfoReport = self.settings.CurrentTestResultFolder + '\\CaseStateInfoReport.txt'
        self.planInfoHtml = self.settings.CurrentTestResultFolder + '\\' + self.settings.planFile + ".html"
        self.caseSummaryInfoTemplate = os.getcwd() + '\\TestResult\\CaseSummaryInfoTemplate.txt'
        self.caseSummaryInfoReportPath = self.settings.CurrentTestResultFolder + '\\' + "CaseSummaryInfoReport.txt"

    def CreateCaseStateInfoReport(self):
        if not os.path.exists(self.CaseStateInfoReport):
                Tool.createFile(self.CaseStateInfoReport)

    def CreateCaseSummaryInfoReport(self):
        if not os.path.exists(self.caseSummaryInfoReportPath):
                Tool.createFile(self.caseSummaryInfoReportPath)

    def writeCaseSummaryInfo(self, testCaseResult:TestCaseResult):
        CSIT = Tool.readFile(self.caseSummaryInfoTemplate)
        CSIT = CSIT.replace("TestCaseNumber", testCaseResult.TestCaseNumber)
        CSIT = CSIT.replace("TestCaseFile", testCaseResult.TestCaseFile)
        CSIT = CSIT.replace("StartTime", testCaseResult.StartTime)
        if testCaseResult.CaseResult == 'NotRun':
            CSIT = CSIT.replace("ResultCategory", "notruncentertext")
        elif testCaseResult.CaseResult == 'Error' or testCaseResult.CaseResult == 'Failed':
            CSIT = CSIT.replace("ResultCategory", "failedcentertext")
        else:
            CSIT = CSIT.replace("ResultCategory", "passedcentertext")
        CSIT = CSIT.replace("CaseResult", testCaseResult.CaseResult)

        Tool.appendFile(self.caseSummaryInfoReportPath, CSIT)

    def WriteCaseStateInfo(self):
        CaseStateInfo :str = ''
        for CaseResult in self.settings.testPlanResult.TestCaseResultCollection:
            self.writeCaseSummaryInfo(CaseResult)
            CSIT = Tool.readFile(self.CaseStateInfoTemplate)
            CSIT = CSIT.replace("TestCaseNumber", CaseResult.TestCaseNumber)
            CSIT = CSIT.replace("TestCaseName", CaseResult.TestCaseName)
            StateInfo :str = ''
            for StateResult in CaseResult.TestStateResultCollection:
                SIT = Tool.readFile(self.StateInfoTemplate)
                SIT = SIT.replace("TestStateNumber", StateResult.TestStateNumber)
                SIT = SIT.replace("TestStateDescription", StateResult.TestStateDescription)
                SIT = SIT.replace("TestStateFile", StateResult.TestStateFile)
                SIT = SIT.replace("TestStateReportPath", StateResult.RelativeTestStateReportPath)
                if StateResult.StateResult == 'NotRun':
                    SIT = SIT.replace("ResultCategory", "notruncentertext")
                elif StateResult.StateResult == 'Error' or StateResult.StateResult == 'Failed':
                    SIT = SIT.replace("ResultCategory", "failedcentertext")
                else:
                    SIT = SIT.replace("ResultCategory", "passedcentertext")
                SIT = SIT.replace("StateResult", StateResult.StateResult)
                StateInfo = StateInfo + SIT + "\r\n"
                detailsInfoReport = DetailsInfoReport(StateResult)
                detailsInfoReport.CreateDetailsInfoReport()
                detailsInfoReport.writeDetailsInfotoHtml()
            CSIT = CSIT.replace("StateInfo", StateInfo)
            CaseStateInfo = CaseStateInfo + CSIT + "\r\n"
        Tool.appendFile(self.CaseStateInfoReport, CaseStateInfo)

    def writeCaseSummaryInfo_toHtml(self):
        CSIT = Tool.readFile(self.caseSummaryInfoReportPath)
        planInfo = Tool.readFile(self.planInfoHtml)
        planInfo = planInfo.replace("CaseSummaryInfo", CSIT)
        Tool.writeFile(self.planInfoHtml, planInfo)

    def WriteCaseStateInfo_toHtml(self):
        CSIR = Tool.readFile(self.CaseStateInfoReport)
        planInfo = Tool.readFile(self.planInfoHtml)
        planInfo = planInfo.replace("CaseStateInfo", CSIR)
        Tool.writeFile(self.planInfoHtml, planInfo)
