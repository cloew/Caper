import unittest

from metadata.general.Test.suite import suite as general_suite
from metadata.python.Test.suite import suite as python_suite

suites = [python_suite,
          general_suite]
suite = unittest.TestSuite(suites)