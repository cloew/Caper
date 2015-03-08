import unittest

from metadata.Test.suite import suite as metadata_suite

# Collect all the test suites
suites = [metadata_suite]

alltests = unittest.TestSuite(suites)

# Run all the tests
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(alltests)
