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
        f = open(os.path.join(TESTDIR, '0=bagit_0.1'))
        self.assertEqual(f.read(), "bagit_0.1\n")
        f.close()

    def test_who(self):
        self.assertFalse(os.path.isfile(os.path.join(TESTDIR, '1=Twain,M.')))
        namaste.who(TESTDIR, "Twain,M.")
        self.assertTrue(os.path.isfile(os.path.join(TESTDIR, '1=Twain,M.')))
        f = open(os.path.join(TESTDIR, '1=Twain,M.'))
        self.assertEqual(f.read(), "Twain,M.\n")
        f.close()

    def test_what(self):
        self.assertFalse(os.path.isfile(os.path.join(TESTDIR, '2=Hamlet')))
        namaste.what(TESTDIR, "Hamlet")
        self.assertTrue(os.path.isfile(os.path.join(TESTDIR, '2=Hamlet')))
        f = open(os.path.join(TESTDIR, '2=Hamlet'))
        self.assertEqual(f.read(),"Hamlet\n")
        f.close()

    def test_when(self):
        self.assertFalse(os.path.isfile(os.path.join(TESTDIR, '3=2005')))
        namaste.when(TESTDIR, "2005")
        self.assertTrue(os.path.isfile(os.path.join(TESTDIR, '3=2005')))
        f = open(os.path.join(TESTDIR, '3=2005'))
        self.assertEqual(f.read(), "2005\n")
        f.close()

    def test_where(self):
        self.assertFalse(os.path.isfile(os.path.join(TESTDIR, '4=Seattle')))
        namaste.where(TESTDIR, "Seattle")
        self.assertTrue(os.path.isfile(os.path.join(TESTDIR, '4=Seattle')))
        f = open(os.path.join(TESTDIR, '4=Seattle'))
        self.assertEqual(f.read(), "Seattle\n")
        f.close()

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

    def test_gettypes(self):
        namaste.dirtype(TESTDIR, 'bagit_2323.1')
        namaste.dirtype(TESTDIR, 'redd_0.1333')
        namaste.dirtype(TESTDIR, 'dflat_34.22')
        types = namaste.get_types(TESTDIR)
        self.assertTrue('bagit' in types)
        self.assertTrue('redd' in types)
        self.assertTrue('dflat' in types)
        self.assertEqual(types['bagit'], {'name':'bagit', 'major':'2323', 'minor':'1'})
        self.assertEqual(types['redd'], {'name':'redd', 'major':'0', 'minor':'1333'})
        self.assertEqual(types['dflat'], {'name':'dflat', 'major':'34', 'minor':'22'})

if __name__ == "__main__":
    unittest.main()
