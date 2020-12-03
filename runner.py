import unittest
from unittestreport import TestRunner


suite1 = unittest.defaultTestLoader.discover(r"./TestCase")
runner = TestRunner(suite1)
runner.run()










