#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from imagescraper.confyaml import ConfYaml
from os import listdir
from os.path import isfile, join, splitext

class TestConfYaml(unittest.TestCase):

    def setUp(self):
        # get all conf.yaml file names in etc folder
        etc_folder = './etc/'
        conf_name_suffix = '.conf.yaml'
        conf_files = [filename for filename in listdir(etc_folder) if (isfile(join(etc_folder, filename)) and filename.endswith(conf_name_suffix))]
        self.__test_conf_yamls = []
        # get the first part of the conf file name
        for conf_file in conf_files:
            conf_name = splitext(splitext(conf_file)[0])[0]
            self.__test_conf_yamls.append(ConfYaml(conf_name))

    def tearDown(self):
        pass

    def test_get_login_info(self):
        for test_conf_yaml in self.__test_conf_yamls:
            self.assertIsNotNone(test_conf_yaml.get_login_info())

    def test_get_page_urls(self):
        for test_conf_yaml in self.__test_conf_yamls:
            self.assertIsNotNone(test_conf_yaml.get_page_urls())

    def test_get_image_url_match_pattern(self):
        for test_conf_yaml in self.__test_conf_yamls:
            self.assertIsNotNone(test_conf_yaml.get_image_url_match_pattern())

    def test_get_save_dir(self):
        for test_conf_yaml in self.__test_conf_yamls:
            self.assertIsNotNone(test_conf_yaml.get_save_dir())

    def test_get_file_rename_pattern(self):
        for test_conf_yaml in self.__test_conf_yamls:
            self.assertIsNotNone(test_conf_yaml.get_file_rename_pattern())

    def test_get_file_rename_string(self):
        for test_conf_yaml in self.__test_conf_yamls:
            self.assertIsNotNone(test_conf_yaml.get_file_rename_string())
