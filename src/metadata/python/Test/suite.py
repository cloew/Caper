import unittest

from metadata.python.Test.function_start_detector_test import suite as function_start_detector_suite

suites = [function_start_detector_suite]
suite = unittest.TestSuite(suites)