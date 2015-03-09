import unittest

from metadata.python.Test.function_end_detector_test import suite as function_end_detector_suite
from metadata.python.Test.leading_whitespace_test import suite as leading_whitespace_suite
from metadata.python.Test.function_start_detector_test import suite as function_start_detector_suite

suites = [function_start_detector_suite,
          leading_whitespace_suite,
          function_end_detector_suite]
suite = unittest.TestSuite(suites)