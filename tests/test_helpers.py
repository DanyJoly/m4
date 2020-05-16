import unittest
import helpers
import pandas as pd


class HelpersTests(unittest.TestCase):
    def test_load_dataset(self):
        train, test = helpers.load_dataset(helpers.Datasets.Hourly)
        self.assertEqual(train.shape, (414, 960))


if __name__ == '__main__':
    unittest.main()
