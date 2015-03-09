import unittest

from caper_vault.Test.suite import suite as caper_vault_suite

# Collect all the test suites
suites = [caper_vault_suite]

alltests = unittest.TestSuite(suites)

# Run all the tests
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(alltests)
