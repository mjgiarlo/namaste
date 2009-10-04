import os
import shutil 
import unittest
import namaste

class NamasteTests(unittest.TestCase):

    def setUp(self):
        if os.path.isdir('namaste-test'):
            shutil.rmtree('namaste-test')
        shutil.copytree('docs', 'namaste-test')

    def tearDown(self):
        if os.path.isdir('namaste-test'):
            shutil.rmtree('namaste-test')

    def test_type(self):
        self.assertTrue(True)

    def test_who(self):
        self.assertTrue(True)

    def test_what(self):
        self.assertTrue(True)

    def test_when(self):
        self.assertTrue(True)

    def test_where(self):
        self.assertTrue(True)


