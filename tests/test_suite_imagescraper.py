#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from tests.test_scrapedimage import TestScrapedImage
from tests.test_confyaml import TestConfYaml
from tests.spiders.test_imagespider import TestImageSpider

def test_imagescraper_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestImageSpider)
    suite.addTest(TestScrapedImage)
    suite.addTest(TestConfYaml)
    return suite

if __name__ == '__main__':
    import sys
    runner = unittest.TextTestRunner()
    result = runner.run(test_imagescraper_suite())
    sys.exit(not result.wasSuccessful())
