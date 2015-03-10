import unittest

from kao_io.Test.file_line_test import suite as file_line_suite

suites = [file_line_suite]
suite = unittest.TestSuite(suites)