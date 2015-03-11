import unittest

from kao_io.Test.suite import suite as kao_io_suite
from metadata.Test.suite import suite as metadata_suite

# Collect all the test suites
suites = [metadata_suite,
          kao_io_suite]

alltests = unittest.TestSuite(suites)

# Run all the tests
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(alltests)
