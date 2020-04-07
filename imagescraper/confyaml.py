#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

class ConfYaml(object):

    def __init__(self, confname):
        with open('./etc/imagescraper.default.conf.yaml', 'r') as stream:
            try:
                self.__default_data = yaml.load(stream, Loader=yaml.FullLoader)
            except yaml.YAMLError as yaml_error:
                print(yaml_error)
        with open('./etc/imagescraper.{}.conf.yaml'.format(confname), 'r') as stream:
            try:
                self.__data = yaml.load(stream, Loader=yaml.FullLoader)
            except yaml.YAMLError as yaml_error:
                print(yaml_error)

    def get_login_info(self):
        return self.__data["login_info"] if self.__data["login_info"] else self.__default_data["login_info"]

    def get_page_urls(self):
        return self.__data["page_urls"] if self.__data["page_urls"] else self.__default_data["page_urls"]

    def get_image_url_match_pattern(self):
        return self.__data["image_url_match_pattern"] if self.__data["image_url_match_pattern"] else self.__default_data["image_url_match_pattern"]

    def get_save_dir(self):
        return self.__data["save_dir"] if self.__data["save_dir"] else self.__default_data["save_dir"]

    def get_file_rename_pattern(self):
        return self.__data["file_rename_pattern"] if self.__data["file_rename_pattern"] else self.__default_data["file_rename_pattern"]

    def get_file_rename_string(self):
        return self.__data["file_rename_string"] if self.__data["file_rename_string"] else self.__default_data["file_rename_string"]

