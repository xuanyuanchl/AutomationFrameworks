from Base.BaseRunner import ParametrizedTestCase
import os
import time

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class HomeTest(ParametrizedTestCase):
    def testSearch(self):
        time.sleep(1)
        self.driver.find_element_by_id("kw").send_keys("selenium")
        time.sleep(2)
        self.driver.find_element_by_id("su").click()
        time.sleep(2)

    @classmethod
    def setUpClass(cls):
        super(HomeTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HomeTest, cls).tearDownClass()
