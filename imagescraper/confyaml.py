#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

class ConfYaml(object):

    def __init__(self, confname):
        with open('./etc/{}.conf.yaml'.format(confname), 'r') as stream:
            try:
                self.__data = yaml.load(stream)
            except yaml.YAMLError:
                raise

    def get_login_info(self):
        return self.__data["login_info"]

    def get_page_urls(self):
        return self.__data["page_urls"]

    def get_image_url_match_pattern(self):
        return self.__data["image_url_match_pattern"]

    def get_save_dir(self):
        return self.__data["save_dir"]

    def get_file_rename_pattern(self):
        return self.__data["file_rename_pattern"]

    def get_file_rename_string(self):
        return self.__data["file_rename_string"]

