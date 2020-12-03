import unittest
# from unittest_st.test_device_mode import test_Device_Mode
from TestCase.testcase_infolist import test_addinfo

load = unittest.TestLoader()
suite = unittest.TestSuite()
# test1 = load.loadTestsFromTestCase(test_Device_Mode)
test1 = load.loadTestsFromTestCase(test_addinfo)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(test1)
