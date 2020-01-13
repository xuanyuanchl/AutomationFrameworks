import os
import time
import unittest

from HTMLTestRunner import HTMLTestRunner

test_dir = './Test'
discover = unittest.defaultTestLoader.discover(start_dir='./Test', pattern="test1.py")

if __name__ == "__main__":
    report_dir = './test_report'
    os.makedirs(report_dir, exist_ok=True)
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    report_name = '{0}/{1}.html'.format(report_dir, now)

    with open(report_name, 'wb')as f:
        runner = HTMLTestRunner(stream=f, title="test", description="calcultortest")
        runner.run(discover)
