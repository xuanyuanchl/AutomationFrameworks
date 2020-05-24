from src.com.TestSettings.Settings import Settings
import os
from src.com.SummaryInfo.TestModuleInfo import TestModuleInfo
from src.com.Utility.Tool import Tool

class SummaryReport(object):
    """description of class"""
    ModuleInfoTemplatePath:str = None
    planInfoHtml:str = None
    testModuleInfo:str = None
    def __init__(self):
        self.settings = Settings.getSettings()
        self.ModuleInfoTemplatePath = os.getcwd() + '\\TestResult\\ModuleInfoTemplate.txt'
        self.planInfoHtml = self.settings.CurrentTestResultFolder + '\\' + self.settings.planFile + ".html"
        
    def writeModuleInfo(self):
        moduleInfo:str = ''
        for key in self.settings.testPlanResult.moduleInfoCollection:
            self.testModuleInfo = TestModuleInfo()
            self.testModuleInfo.setModuleName(key)
            self.testModuleInfo.setModuleInfo()
            MIR = Tool.readFile(self.ModuleInfoTemplatePath)
            MIR = MIR.replace('ModuleName', self.testModuleInfo.currentModuleName)
            MIR = MIR.replace('ModuleTotalScriptCount', str(self.testModuleInfo.moduleScriptCount))
            MIR = MIR.replace('ModuleScriptPassedCount', str(self.testModuleInfo.moduleScriptPassedCount))
            MIR = MIR.replace('ModuleScriptFailedCount', str(self.testModuleInfo.moduleScriptFailedCount))
            MIR = MIR.replace("ModuleScriptPassPercentage", self.testModuleInfo.modulePassPercentage)
            MIR = MIR.replace("ModuleScriptFailPercentage", self.testModuleInfo.moduleFailPercentage)
            moduleInfo = moduleInfo + MIR + "\r\n"
        return moduleInfo

    def writeModuleInfo_toHtml(self):
        MIR = self.writeModuleInfo();
        planInfo = Tool.readFile(self.planInfoHtml)
        planInfo = planInfo.replace("ModuleInfo", MIR)
        Tool.writeFile(self.planInfoHtml, planInfo)