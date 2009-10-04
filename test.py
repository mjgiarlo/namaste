import os
import shutil 
import unittest
import namaste

TESTDIR = 'namaste-test'


class NamasteTests(unittest.TestCase):

    def setUp(self):
        if os.path.isdir(TESTDIR):
            shutil.rmtree(TESTDIR)
        shutil.copytree('docs', TESTDIR)

    def tearDown(self):
        if os.path.isdir(TESTDIR):
            shutil.rmtree(TESTDIR)

    def test_type(self):
        self.assertFalse(os.path.isfile(os.path.join(TESTDIR, '0=bagit_0.1')))
        namaste.dirtype(TESTDIR, 'bagit_0.1') 
        self.assertTrue(os.path.isfile(os.path.join(TESTDIR, '0=bagit_0.1')))
        self.assertEqual(open(os.path.join(TESTDIR, '0=bagit_0.1')).read(),
                         "bagit_0.1\n")

    def test_who(self):
        self.assertFalse(os.path.isfile(os.path.join(TESTDIR, '1=Twain,M.')))
        namaste.who(TESTDIR, "Twain,M.")
        self.assertTrue(os.path.isfile(os.path.join(TESTDIR, '1=Twain,M.')))
        self.assertEqual(open(os.path.join(TESTDIR, '1=Twain,M.')).read(),
                         "Twain,M.\n")

    def test_what(self):
        self.assertFalse(os.path.isfile(os.path.join(TESTDIR, '2=Hamlet')))
        namaste.what(TESTDIR, "Hamlet")
        self.assertTrue(os.path.isfile(os.path.join(TESTDIR, '2=Hamlet')))
        self.assertEqual(open(os.path.join(TESTDIR, '2=Hamlet')).read(),
                         "Hamlet\n")

    def test_when(self):
        self.assertFalse(os.path.isfile(os.path.join(TESTDIR, '3=2005')))
        namaste.when(TESTDIR, "2005")
        self.assertTrue(os.path.isfile(os.path.join(TESTDIR, '3=2005')))
        self.assertEqual(open(os.path.join(TESTDIR, '3=2005')).read(),
                         "2005\n")

    def test_where(self):
        self.assertFalse(os.path.isfile(os.path.join(TESTDIR, '4=Seattle')))
        namaste.where(TESTDIR, "Seattle")
        self.assertTrue(os.path.isfile(os.path.join(TESTDIR, '4=Seattle')))
        self.assertEqual(open(os.path.join(TESTDIR, '4=Seattle')).read(),
                         "Seattle\n")

    def test_get(self):
        namaste.dirtype(TESTDIR, 'bagit_0.1') 
        namaste.who(TESTDIR, "Twain,M.")
        namaste.what(TESTDIR, "Hamlet")
        namaste.when(TESTDIR, "2005")
        namaste.where(TESTDIR, "Seattle")
        tags = namaste.get(TESTDIR)
        tags.sort()
        self.assertEqual(tags, [
                os.path.join(TESTDIR, namaste._make_namaste(0, 'bagit_0.1')),
                os.path.join(TESTDIR, namaste._make_namaste(1, 'Twain,M.')),
                os.path.join(TESTDIR, namaste._make_namaste(2, 'Hamlet')),
                os.path.join(TESTDIR, namaste._make_namaste(3, '2005')),
                os.path.join(TESTDIR, namaste._make_namaste(4, 'Seattle')),
                ])

