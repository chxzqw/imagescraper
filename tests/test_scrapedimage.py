#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import io
import os
import os.path
from PIL import Image
from imagescraper.scrapedimage import ScrapedImage

class TestScrapedImage(unittest.TestCase):

    def setUp(self):
        # generate random jpeg image and convert to byte io which is able to be read by Image as stream
        byteImgIO = io.BytesIO()
        test_image = Image.new('RGB', (5, 5))
        test_image.save(byteImgIO, "JPEG")
        byteImgIO.seek(0)
        test_stream = byteImgIO.read()
        self.__img = ScrapedImage(test_stream)

    def tearDown(self):
        pass

    def test_save(self):
        self.__img.save('./', 'test_image.jpg')
        self.assertTrue(os.path.exists('./test_image.jpg'))
        os.remove('./test_image.jpg')
