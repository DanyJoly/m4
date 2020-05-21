import unittest
import m4helpers


class HelpersTests(unittest.TestCase):
    def test_load_dataset(self):
        train, test = m4helpers.load_dataset(m4helpers.Datasets.Hourly)
        self.assertEqual(train.shape, (414, 960))

    def test_trim(self):
        train, test = m4helpers.load_dataset(m4helpers.Datasets.Hourly)

        ori = train.iloc[0]
        self.assertGreater(ori.isnull().sum(), 0, "Datasets are of unequal lengths and dataframe is NaN padded.")

        len_ori = len(ori)
        trimmed = m4helpers.trim(train, 0)
        self.assertEqual(trimmed.isnull().sum(), 0, "Trimmed dataset has no more NaN padding.")

        self.assertTrue(train.values.base is trimmed.values.base,
                        "For performance, confirm that this is returning a view, not a copy")


if __name__ == '__main__':
    unittest.main()
