#!/usr/bin/python3

import unittest
from unittest.mock import patch, MagicMock
from funcs.now import get_picture
from PIL import Image

class TestGetPicture(unittest.TestCase):

    @patch("webscrapper.scrapper.InspiroScrapper.inspiro_scrapper")
    @patch("webscrapper.scrapper.InspiroScrapper.__init__")
    def test_get_picture(
            self,
            mock_init,
            mock_inspiro_scrapper):

        mock_init.return_value = None
        mock_inspiro_scrapper.return_value = "test_picture"

        ret = get_picture()

        # test successful execution
        self.assertEqual(ret, True)
