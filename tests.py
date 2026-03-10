import dataset
import unittest
from function_file import (is_increasing, filter_by_year)

class TestCase(unittest.TestCase):

    def test_is_increasing(self):
        report1 = dataset.Statistics(
            year = 2016,
            energy = {},
            transportation = {},
            waste = ,
            water = {}
        )
        report2 = dataset.Statistics(
            year = 2010,
            energy = {},
            transportation = {},
            waste = ,
            water = {}
        )

        reports = [report1, report2]

