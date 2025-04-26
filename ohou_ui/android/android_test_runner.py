import unittest
from ohou_ui.android.android_setup import *
from testcase.playstore_test import *

class TestRunner(unittest.TestCase):

    def setUp(self):

        self.wd = setup_prod()

    def tearDown(self):
        self.wd.quit()

    def test_00_run(self):
        PlayStoreTestCase.search_and_open_app(self, self.wd)



if __name__ == '__main__':
    unittest.main()


