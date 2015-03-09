import unittest

from metadata.python.Test.whitespace_helper_test import suite as whitespace_helper_suite
from metadata.python.Test.function_start_detector_test import suite as function_start_detector_suite

suites = [function_start_detector_suite,
          whitespace_helper_suite]
suite = unittest.TestSuite(suites)