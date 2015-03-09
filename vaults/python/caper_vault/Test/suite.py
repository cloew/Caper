import unittest

from caper_vault.Test.caper_vault_test import suite as caper_vault_suite

suites = [caper_vault_suite]
suite = unittest.TestSuite(suites)