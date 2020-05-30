import unittest
from multiprocessing.pool import Pool
from Base.BaseRunner import ParametrizedTestCase
from TestCase import HomeTest


def runner_pool():
    devices_Pool = ['http://192.168.0.102:5555/wd/hub', 'http://192.168.0.102:6666/wd/hub']
    pool = Pool(len(devices_Pool))
    pool.map(run, devices_Pool)
    pool.close()
    pool.join()


def run(device):
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(HomeTest.HomeTest, param=device))
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    runner_pool()
