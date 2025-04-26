import os
import traceback
from ohou_ui.android.pages.playstore_page import *

class PlayStoreTestCase:

    def search(self, wd):

        playstore = PlayStore(wd)

        search_btn = playstore.search_btn()
        search_btn.click()