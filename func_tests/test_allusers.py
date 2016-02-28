# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils.translation import activate
from django.utils import formats
from selenium import webdriver

from datetime import date
import unittest, sys


class HomeNewVisitorTest(StaticLiveServerTestCase):

    ############ FROM SUPERLISTS
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()
    ############

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        activate('en')

    def tearDown(self):
        self.browser.quit()

    def get_full_url(self, namespace):
        return self.server_url + reverse(namespace)


    ############ TESTS ##########

    def test_home(self):
        self.browser.get(self.get_full_url("home"))
        self.assertIn("Squashitlan", self.browser.title)

        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.value_of_css_property("color"),
            "rgba(200, 50, 255, 1)")

    def test_home_files(self):
        # What are these Home Files?
        # I still don't get their purpose.
        # Yeah yeah, I know... Robots and somethings.
        self.browser.get(self.server_url + "/robots.txt")
        self.assertNotIn("Not Found", self.browser.title)
        self.browser.get(self.server_url + "/humans.txt")
        self.assertNotIn("Not Found", self.browser.title)

    def test_localizations(self):
        today = date.today()
        welcome = {'en'   : 'Welcome to Squashitlan!',
                   'es-mx': 'Bienvenido a Squashitlán.'}

        for lang in ['en', 'es-mx']:
            activate(lang)
            self.browser.get(self.get_full_url("home"))

            # Localization
            try:
                local_date = self.browser.find_element_by_id("local-date")
            except NoSuchElementException:
                self.fail("Could not find 'local-date' element on page")
            self.assertEqual(formats.date_format(today, use_l10n=True),
                local_date.text)

            non_local_date = self.browser.find_element_by_id("non-local-date")
            self.assertEqual(today.strftime('%Y-%m-%d'), non_local_date.text)

            # Internationalization
            h1 = self.browser.find_element_by_tag_name("h1")
            self.assertEqual(h1.text, welcome[lang])

        # Time Zones
        self.browser.get(self.get_full_url("home"))
        tz = self.browser.find_element_by_id("time-tz").text
        utc = self.browser.find_element_by_id("time-utc").text
        ny = self.browser.find_element_by_id("time-ny").text
        self.assertNotEqual(tz, utc)
        self.assertNotIn(ny, [tz, utc])

#    def test_annotate_a_game():
#        pass


if __name__ == '__main__':
    unittest.main(warnings='ignore')
