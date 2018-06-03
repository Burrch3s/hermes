#!/usr/bin/python3

import unittest
from unittest.mock import patch, MagicMock
from webscrapper.scrapper import InspiroScrapper

class TestInspiroScrapper(unittest.TestCase):

    @patch("webscrapper.scrapper.InspiroScrapper._web_scrapper")
    def test_inspiro_scrapper(self, mock_web_scrapper):
        # test image file written and return value set correctly
        image = "helloworld"
        mock_web_scrapper.return_value = str.encode(image)
        x = InspiroScrapper()
        title = x.inspiro_scrapper()
        with open("motivate/{}".format(title), "rb") as f:
            stuff = f.read()

        self.assertIn('motivation', title)
        self.assertEqual(stuff.decode(), "helloworld")

        # test exception raised when IO error occurs
        mock_web_scrapper.return_value = "helloworld"
        ret = x.inspiro_scrapper()
        self.assertEqual(ret, False)

    def test_web_scrapper(self):
        # test webscrapper properly pulling down image
        x = InspiroScrapper()
        ret = x._web_scrapper()
        self.assertIsInstance(ret, bytes)
