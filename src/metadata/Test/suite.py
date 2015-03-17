import unittest

from metadata.python.Test.suite import suite as python_suite

suites = [python_suite]
suite = unittest.TestSuite(suites)