import unittest

from metadata.general.Test.function_finder_test import suite as function_finder_suite
from metadata.general.Test.file_line_test import suite as file_line_suite

suites = [file_line_suite,
          function_finder_suite]
suite = unittest.TestSuite(suites)