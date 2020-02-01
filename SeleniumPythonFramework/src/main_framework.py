'''This is a circulator, run each test case in test plan, and generate html report'''

import logging
# import os
# import sys
import traceback
import unittest

from MailSender.mail_sender import SendMail
from ReportGenerate.StateReport import StateReport
from ReportGenerate.SummaryReport import SummaryReport
from ReportGenerate.SystemReport import SystemReport
from com.FunctionLibrary.ExecuteFunction import ExecuteFunction
from com.TestPlanInfo.TestStateResult import TestStateResult
from com.TestSettings.Settings import Settings
from com.Utility.Tool import Tool

#
# PROJECT = r'D:\GitGUI\SeleniumPythonFramework'  # 项目所在路径
# sys.path.append(os.getcwd().split(PROJECT)[0] + PROJECT)


class MainFramework(unittest.TestCase):
    '''a circulator'''
    test_case_result = None
    test_state_result = None
    test_module_info = None
    settings = None

    @classmethod
    def setUpClass(cls):
        '''set up before execute test'''
        Settings.constructSettings()
        MainFramework.settings = Settings.getSettings()
        logging.info("construct settings successfully")

    def test_execute(self):
        '''execute each test step by step'''
        try:
            wb_plan = self.settings.loadPanFileAndSetCaseNumber()
            wk_plan_sheet = wb_plan['Sheet1']
            for test_case_number in range(2, self.settings.TestCaseNumbers + 2):
                self.test_case_result = self.settings.cleanUpAndSetUpPlanFile(
                    wk_plan_sheet, test_case_number)
                self.settings.createWebDriver()
                try:
                    wb_script = self.settings.loadScriptFile()
                    wk_script_sheet = wb_script['Sheet1']
                    test_state_row: int = self.settings.getStateNumber(
                        wb_script)
                    for test_state_number in range(2, test_state_row + 2):
                        self.settings.setStateFile(
                            wk_script_sheet, test_state_number)
                        self.test_state_result = TestStateResult(
                            self.settings.StateFile)
                        e_f = ExecuteFunction()
                        self.test_state_result = e_f.SetState(
                            self.settings.StateFile)
                        self.test_state_result = self.settings.updateStateResult(
                            wk_script_sheet, self.test_state_result, test_state_number)
                        self.test_case_result.TestStateResultCollection.append(
                            self.test_state_result)
                except Exception as exception:
                    logging.error(
                        f'there is error: "{str(exception)}" "{traceback.format_exc()}"')
                finally:
                    test_case_result = ExecuteFunction.TestCase_Result(
                        self.test_case_result)
                    self.settings.updateScriptFileAndCaseResult(
                        wb_script, self.test_case_result, test_case_result)
                    MainFramework.settings.wedriver.quit()
                    logging.info('webdriver quit successfully')
            for test_case_number in range(2, self.settings.TestCaseNumbers + 2):
                self.settings.updatePlanFile(wk_plan_sheet, test_case_number)
        finally:
            self.settings.testPlanResult.TestPlanEndTime = Tool.CurrentTime()
            wb_plan.save(self.settings.planFilePath)
            logging.info(
                f'save plan file: {self.settings.planFilePath} successfully')

    @classmethod
    def tearDownClass(cls):
        '''generate HTML report after execute test finished'''
        system_report = SystemReport()
        system_report.CreatePlanInfoReport()
        MainFramework.settings.testPlanResult.setAllScenarioPassFailInfo()
        system_report.writeSystemInfo_toHtml()
        MainFramework.settings.testPlanResult.getModuleInfo()
        summay_report = SummaryReport()
        summay_report.writeModuleInfo_toHtml()
        state_report = StateReport()
        state_report.CreateCaseSummaryInfoReport()
        state_report.CreateCaseStateInfoReport()
        state_report.WriteCaseStateInfo()
        state_report.writeCaseSummaryInfo_toHtml()
        state_report.WriteCaseStateInfo_toHtml()
        logging.info(
            f'create report {system_report.planInfoHtml} successfully')

        logging.info('Run tests finished')

        html_report = MainFramework.settings.CurrentTestResultFolder + \
            '\\' + MainFramework.settings.planFile + ".html"

        s = SendMail(html_report)
        s.send()

        MainFramework.settings = None


if __name__ == "__main__":
    unittest.main()
