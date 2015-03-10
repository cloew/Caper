import unittest

from metadata.general.Test.function_finder_test import suite as function_finder_suite

suites = [function_finder_suite]
suite = unittest.TestSuite(suites)