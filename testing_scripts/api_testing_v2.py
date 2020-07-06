import unittest
from urllib import request, parse
import json
import argparse
import os

unittest.TestLoader.sortTestMethodsUsing = None

class TestStringMethods(unittest.TestCase):
    AUTH = ''

    def test1_addTODO(self):
        """
        Adding an item to the todo List.

        """
        data = {
            "title": "Task 14",
            "desc": "Task 14 just added",
            "status": "In Progress",
            "taskDueDate": "2020-04-23"
        }

        true_output = sorted(data.keys())

        url = "http://localhost:8000/todo/addTODO/"
        headers = {
            'Authorization': 'Token %s' % (TestStringMethods.AUTH)
        }

        data = parse.urlencode(data).encode()
        req = request.Request(url, data=data, headers=headers)  # this will make the method "POST"
        resp = request.urlopen(req)
        resp = resp.read().decode('utf-8')
        resp = json.loads(resp)
        self.assertEqual(sorted(resp.keys()), true_output)
        print("Test 1: Add Task TODO")
    #
    def test2_listallTODO(self):
        """
        Listing all the items, sort by title
        """
        data = {
            "sortby": "title"
        }

        url = "http://localhost:8000/todo/listallTODO/"
        headers = {
            # 'Authorization': 'Token %s' % (os.getenv('AuthToken'))
            'Authorization': 'Token %s' % (TestStringMethods.AUTH)
        }

        true_output = ['desc', 'status', 'taskDueDate', 'title', 'userID']

        data = parse.urlencode(data).encode()
        req = request.Request(url, data=data, headers=headers)  # this will make the method "POST"
        resp = request.urlopen(req)
        resp = resp.read().decode('utf-8')
        resp = json.loads(resp)
        self.assertEqual(sorted(resp[0].keys()), true_output)
        print("Test 2: ListAllTODO")

    def test3_updateTODO(self):
        """
        Updating the added todo task
        """
        data = {
            "title": "Task 14",
            "desc": "Task 14 just updated",
            "status": "DONE",
            "taskDueDate": "2020-04-23"
        }

        url = "http://localhost:8000/todo/updateTODO/"
        headers = {
            # 'Authorization': 'Token %s' % (os.getenv('AuthToken'))
            'Authorization': 'Token %s' % (TestStringMethods.AUTH)
        }

        data = parse.urlencode(data).encode()
        req = request.Request(url, data=data, headers=headers)  # this will make the method "POST"
        resp = request.urlopen(req)
        status = resp.getcode()
        self.assertEqual(200, status)
        print("Test 3: update todo app", status)

    def test4_listallTODO_filter(self):
        """
        List todo with title as filter
        """
        data = {
            "title": "Task 14"
        }
        updated_desc = "Task 14 just updated"
        url = "http://localhost:8000/todo/listallTODO/"
        headers = {
            # 'Authorization': 'Token %s' % (os.getenv('AuthToken'))
            'Authorization': 'Token %s' % (TestStringMethods.AUTH)
        }

        data = parse.urlencode(data).encode()
        req = request.Request(url, data=data, headers=headers)  # this will make the method "POST"
        resp = request.urlopen(req)
        resp = resp.read().decode('utf-8')
        resp = json.loads(resp)
        self.assertEqual(resp[0]['desc'].lower(), updated_desc.lower())
        print("Test 4: list all TODO with filter")

    def test5_deleteTODO(self):
        """
        Deleting the task by giving the title
        """
        data = {
            "title": "Task 14"
        }

        url = "http://localhost:8000/todo/deleteTODO/"
        headers = {
            # 'Authorization': 'Token %s' % (os.getenv('AuthToken'))
            'Authorization': 'Token %s' % (TestStringMethods.AUTH)
        }

        data = parse.urlencode(data).encode()
        req = request.Request(url, data=data, headers=headers)  # this will make the method "POST"
        resp = request.urlopen(req)
        resp = resp.read().decode('utf-8')
        resp = json.loads(resp)
        self.assertTrue(resp)
        print("Test 5: Delete TODO")

    def test6_listallTODO_check(self):
        """
        Verifying if the above deleted task is present in the todo list
        """
        data = {
            "title": "Task 14"
        }
        trueData = []
        url = "http://localhost:8000/todo/listallTODO/"
        headers = {
            # 'Authorization': 'Token %s' % (os.getenv('AuthToken'))
            'Authorization': 'Token %s' % (TestStringMethods.AUTH)
        }

        data = parse.urlencode(data).encode()
        req = request.Request(url, data=data, headers=headers)  # this will make the method "POST"
        resp = request.urlopen(req)
        resp = resp.read().decode('utf-8')
        resp = json.loads(resp)
        self.assertEqual(resp, trueData)
        print("Test 6: Deleted TODO not found")

        # 669 233 3868


if __name__ == '__main__':
    TestStringMethods.AUTH = os.environ.get("AUTH")
    unittest.main()
