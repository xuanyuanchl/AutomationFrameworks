import logging
import traceback
import unittest

from src.ReportGenerate.StateReport import StateReport
from src.ReportGenerate.SummaryReport import SummaryReport
from src.ReportGenerate.SystemReport import SystemReport
from src.com.FunctionLibrary.ExecuteFunction import ExecuteFunction
from src.com.TestPlanInfo.TestStateResult import TestStateResult
from src.com.TestSettings.Settings import Settings
from src.com.Utility.Tool import Tool


class MainFramework(unittest.TestCase):
    testCaseResult = None
    testStateResult = None
    testModuleInfo = None
    settings = None

    @classmethod
    def setUpClass(cls):
        Settings.constructSettings()
        MainFramework.settings = Settings.getSettings()
        logging.info("construct settings successfully")

    def testExecute(self):
        try:
            wb_plan = self.settings.loadPanFileAndSetCaseNumber()
            wk_plan_sheet = wb_plan['Sheet1']
            for i in range(2, self.settings.TestCaseNumbers + 2):
                self.testCaseResult = self.settings.cleanUpAndSetUpPlanFile(
                    wk_plan_sheet, i)
                try:
                    wb_script = self.settings.loadScriptFile()
                    wk_script_sheet = wb_script['Sheet1']
                    testStateRow: int = self.settings.getStateNumber(wb_script)
                    for i in range(2, testStateRow + 2):
                        self.settings.setStateFile(wk_script_sheet, i)
                        self.testStateResult = TestStateResult(
                            self.settings.StateFile)
                        ef = ExecuteFunction()
                        self.testStateResult = ef.SetState(
                            self.settings.StateFile)
                        self.testStateResult = self.settings.updateStateResult(wk_script_sheet,
                                                                               self.testStateResult, i)
                        self.testCaseResult.TestStateResultCollection.append(
                            self.testStateResult)
                except Exception as e:
                    logging.error('there is error: ' + str(e) +
                                  '.' + traceback.format_exc())
                finally:
                    self.settings.updateScriptFileAndCaseResult(wb_script,
                                                                self.testCaseResult, ExecuteFunction.TestCase_Result(self.testCaseResult))
                    MainFramework.settings.wedriver.quit()
                    logging.info('webdriver quit successfully')
            for i in range(2, self.settings.TestCaseNumbers + 2):
                self.settings.updatePlanFile(wk_plan_sheet, i)
        finally:
            self.settings.testPlanResult.TestPlanEndTime = Tool.CurrentTime()
            wb_plan.save(self.settings.planFilePath)
            logging.info('save plan file: "{0}" successfully'.format(
                self.settings.planFilePath))

    @classmethod
    def tearDownClass(cls):
        systemReport = SystemReport()
        systemReport.CreatePlanInfoReport()
        MainFramework.settings.testPlanResult.setAllScenarioPassFailInfo()
        systemReport.writeSystemInfo_toHtml()
        MainFramework.settings.testPlanResult.getModuleInfo()
        summayReport = SummaryReport()
        summayReport.writeModuleInfo_toHtml()
        stateReport = StateReport()
        stateReport.CreateCaseSummaryInfoReport()
        stateReport.CreateCaseStateInfoReport()
        stateReport.WriteCaseStateInfo()
        stateReport.writeCaseSummaryInfo_toHtml()
        stateReport.WriteCaseStateInfo_toHtml()
        logging.info('create report "{0}" successfully'.format(
            systemReport.planInfoHtml))
        MainFramework.settings = None
        logging.info('Run tests finished')


if __name__ == "__main__":
    unittest.main()
