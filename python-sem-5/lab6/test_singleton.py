import unittest
from main import CurrenciesList


class TestInstances(unittest.TestCase):
    def test_instances(self):
        test_obj = CurrenciesList()
        self.assertIsInstance(test_obj, CurrenciesList)

    def test_instances_ids(self):
        ids = []
        for i in range(10):
            ids.append(id(CurrenciesList()))
        self.assertEqual(ids.count(id(CurrenciesList())), len(ids))

    def test_result_type(self):
        test_obj = CurrenciesList()
        self.assertIsInstance(test_obj.get_currencies(), dict)