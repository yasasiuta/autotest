import unittest
# from unittest_st.test_demo1 import Test_demo
from unittest_st.test_device_mode import test_Device_Mode

# from unittest_st import test_demo1

# suite = unittest.TestSuite()
# suite.addTest(Test_demo("test_01"))
# suite.addTest(Test_demo("test_02"))
# suite.addTest(Test_demo("test_03"))

load = unittest.TestLoader()
suite = unittest.TestSuite()
test1 = load.loadTestsFromTestCase(test_Device_Mode)
# test2 = load.loadTestsFromName('test_device_mode.Test_demo.test_01')
# test3 = load.loadTestsFromModule(test_demo1)
# suite.addTests(test1)
# suite.addTests(test2)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(test1)
# runner.run(test2)
# runner.run(test3)
