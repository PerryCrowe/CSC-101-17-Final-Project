#Author: Gianella Gazzano
import dataset
import unittest
from function_file import (is_increasing, filter_by_year)

class TestCase(unittest.TestCase):

    def test_is_increasing_energy(self):
        report1 = dataset.Statistics(
            year = 2015,
            energy = {"BTUs per Square Foot": 650000},
            transportation = {},
            water = {},
            waste = 0
        )
        report2 = dataset.Statistics(
            year = 2010,
            energy = {"BTUs per Square Foot": 620000},
            transportation = {},
            water = {},
            waste = 0
        )
        print(is_increasing(report1, report2, "energy","BTUs per Square Foot",None))


    def test_is_increasing_transportation(self):
        report1 = dataset.Statistics(
            year = 2015,
            energy = {},
            transportation = {"CP SLO Transit Riders per Year": 400000},
            water = {},
            waste = 0
        )
        report2 = dataset.Statistics(
            year = 2010,
            energy = {},
            transportation = {"CP SLO Transit Riders per Year": 820000},
            waste = 0,
            water = {}
        )
        print(is_increasing(report1, report2, "transportation","CP SLO Transit Riders per Year",None))


    def test_is_increasing_water(self):
        report1 = dataset.Statistics(
            year = 2015,
            energy = {},
            transportation = {},
            water = {"Total Delivered Water": 1180},
            waste = 0
        )
        report2 = dataset.Statistics(
            year = 2010,
            energy = {},
            transportation = {},
            water = {"Total Delivered Water": 3000},
            waste = 0
        )
        print(is_increasing(report1, report2, "water", "Total Delivered Water", None))


    def test_is_increasing_waste(self):
        report1 = dataset.Statistics(
            year = 2015,
            energy = {},
            transportation = {},
            water = {},
            waste = 93.0
        )
        report2 = dataset.Statistics(
            year = 2010,
            energy = {},
            transportation = {},
            water = {},
            waste = 52.3
        )
        print(is_increasing(report1, report2, "waste", "Waste", None))


if __name__ == '__main__':
    unittest.main()