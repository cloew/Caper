import unittest

from metadata.python.Test.python_function_test import suite as python_function_suite
from metadata.python.Test.leading_whitespace_test import suite as leading_whitespace_suite
from metadata.python.Test.function_detector_test import suite as function_detector_suite

suites = [function_detector_suite,
          leading_whitespace_suite,
          python_function_suite]
suite = unittest.TestSuite(suites)