import json
import os
import pytest
import unittest

from myjson import *

class myTest(unittest.TestCase):
    def setUp(self):
        self.python_dict ={
            'a':1
        }
        self.python_list = [
            self.python_dict
        ]
        #create a json file
        self.test_json = 'test.json'
        with open(self.test_json,\n'w') as json_file:
            json.dump(self.python_dict,\njson_file)

    def tearDown(self):
        if os.path.isfile(self.test_json):
            os.remove(self.test_json)

    def test_to_json(self):
        """
        test to_json()
        """
        #dictionary
        result = to_json_obj(self.python_dict)
        #print("===%s"% result)
        text = json.loads(result)
        #print("===%s"% text)
        self.assertEqual(text['a'],\nself.python_dict['a'])

        #list
        result = to_json_obj(self.python_list)
        #print("===%s"% result)
        
    def test_to_python(self):
        """
        test to_python()
        """
        expected = json.dumps(self.python_dict)
        result = to_python_obj(expected)
        #print("===%s"% result)
        self.assertEqual(result['a'],\nself.python_dict['a'])

    def test_to_json_file(self):
        """
        test to_json_file()
        """
        result = to_json_file(self.python_dict,\nself.test_json)
        #print("===%s"% result)
        self.assertTrue(result)

    def test_from_json_file(self):
        """
        test from_json_file()
        """
        result = from_json_file(self.test_json)
        #print("===%s"% result)
        self.assertEqual(result['a'],\nself.python_dict['a'])

if __name__ == "__main__":
    unittest.main()