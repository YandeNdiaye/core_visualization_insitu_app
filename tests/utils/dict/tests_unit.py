""" Dict utils test class
"""
from unittest import TestCase
from collections import OrderedDict
from core_visualization_insitu_app.utils import dict
from os.path import join, dirname, abspath

RESOURCES_PATH = join(dirname(abspath(__file__)), "insitu_data")


class TestGetDictValue(TestCase):
    def test_get_dict_value_valid(self):
        # Arrange
        dict_content = {"k": {"e": {"key": 1}}}
        key = "key"
        # Act
        value = dict.get_dict_value(dict_content, key)
        # Assert
        self.assertTrue(value == 1)


class TestGetDictPathValue(TestCase):
    def test_get_dict_path_value_valid(self):
        # Arrange
        dict_content = {
            u"amTestDB": {u"amTest": {u"partTest": {u"projectID": u"NIST-RPS-14"}}}
        }
        path = "amTestDB.amTest.partTest.projectID"
        # Act
        dict_content_path = dict.get_dict_path_value(dict_content, path)
        result = "NIST-RPS-14"
        # Assert
        self.assertTrue(dict_content_path == result)


class TestGetListInsideDict(TestCase):
    def test_get_list_inside_dict_valid_multi(self):
        # Arrange
        dict_path = "dict_content.amTestDB.amTest.partTest.testResults.chemistry.constituent.element"
        dict_content = {
            u"amTestDB": {
                u"amTest": {
                    u"partTest": {
                        u"testResults": {
                            u"chemistry": {
                                u"constituent": [
                                    {u"element": u"Oxygen"},
                                    {u"element": u"Carbon"},
                                    {u"element": u"Nitrogen"},
                                    {u"element": u"Sulfur"},
                                    {u"element": u"Manganese"},
                                    {u"element": u"Silicon"},
                                    {u"element": u"Phosphorus"},
                                    {u"element": u"Chromium"},
                                    {u"element": u"Molybdenum"},
                                    {u"element": u"Niobium"},
                                    {u"element": u"Tantalum"},
                                    {u"element": u"Cobalt"},
                                    {u"element": u"Titanium"},
                                    {u"element": u"Aluminum"},
                                    {u"element": u"Iron"},
                                ]
                            }
                        }
                    }
                }
            }
        }
        # Act
        list_inside_dict = dict.get_list_inside_dict(dict_path, dict_content)
        result = [
            {u"element": u"Oxygen"},
            {u"element": u"Carbon"},
            {u"element": u"Nitrogen"},
            {u"element": u"Sulfur"},
            {u"element": u"Manganese"},
            {u"element": u"Silicon"},
            {u"element": u"Phosphorus"},
            {u"element": u"Chromium"},
            {u"element": u"Molybdenum"},
            {u"element": u"Niobium"},
            {u"element": u"Tantalum"},
            {u"element": u"Cobalt"},
            {u"element": u"Titanium"},
            {u"element": u"Aluminum"},
            {u"element": u"Iron"},
        ]
        # Assert
        self.assertTrue(list_inside_dict == result)

    def test_get_list_inside_dict_valid_simple(self):
        # Arrange
        dict_path = "dict_content.amTestDB.amTest.partTest.testResults.chemistry.constituent.element"
        dict_content = {
            u"amTestDB": {
                u"amTest": {
                    u"partTest": {
                        u"testResults": {
                            u"chemistry": {u"constituent": [{u"element": u"Iron"}]}
                        }
                    }
                }
            }
        }
        # Act
        list_inside_dict = dict.get_list_inside_dict(dict_path, dict_content)
        result = [{u"element": u"Iron"}]
        # Assert
        self.assertTrue(list_inside_dict == result)

    def test_get_list_inside_dict_none(self):
        # Arrange
        dict_path = "dict_content.amTestDB.amTest.partTest.testResults.chemistry.constituent.element"
        dict_content = {u"amTestDB": {u"amTest": {u"partTest": {u"testResults": {}}}}}
        # Act
        list_inside_dict = dict.get_list_inside_dict(dict_path, dict_content)
        # Assert
        self.assertIsNone(list_inside_dict)


class TestGetDictsInsideListOfDict(TestCase):
    def test_get_dicts_inside_list_of_dict_valid(self):
        # Arrange
        list_path = ["a", "b", "c"]
        list_of_dict = [
            {"a": {"b": {"c": "value1"}}},
            {"a": {"b": {"c": "value2"}}},
            {"a": {"b": {"c": "value3"}}},
        ]
        # Act
        dicts_inside_list_of_dicts = dict.get_dicts_inside_list_of_dict(
            list_path, list_of_dict
        )
        # Assert
        self.assertTrue(
            dicts_inside_list_of_dicts
            == [{"c": "value1"}, {"c": "value2"}, {"c": "value3"}]
        )
