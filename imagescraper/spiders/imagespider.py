#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
import logging
import re
import os
import errno
import sys
from imagescraper.confyaml import ConfYaml
from imagescraper.scrapedimage import ScrapedImage
from datetime import datetime

class ImageSpider(scrapy.Spider):

    name = "imagespider"
    SUCCESS_FLAG = b'success'
    LOGIN_SUCCESS_INFO = 'Login successfully!'
    LOGIN_FAILED_INFO = 'Login failed!'
    SAVING_INFO = 'Saving %s'
    NOSITE_ERROR_MSG = 'Please provide a site name'

    def __create_folder_if_not_exists(self, save_path):
        if not os.path.exists(save_path):
            try:
                os.makedirs(save_path)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

    def __init__(self, site = None):
        if site is None:
            sys.exit(ImageSpider.NOSITE_ERROR_MSG)
        else:
            conf_yaml = ConfYaml(site)
            self.__login_info = conf_yaml.get_login_info()
            self.__page_urls = conf_yaml.get_page_urls()
            self.__image_url_match_pattern = conf_yaml.get_image_url_match_pattern()
            self.__save_dir = conf_yaml.get_save_dir().format(datetime.now())
            self.__create_folder_if_not_exists(self.__save_dir)
            self.__filename_regex = re.compile(conf_yaml.get_file_rename_pattern())
            self.__file_rename_string = conf_yaml.get_file_rename_string()

    def start_requests(self):
        # use the first url to try login staff
        yield scrapy.Request(url = self.__page_urls[0],
            callback = self.fn_start_login,
            dont_filter = True)

    def fn_start_login(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata = self.__login_info,
            callback = self.fn_post_login
        )

    def fn_post_login(self, response):
        if ImageSpider.SUCCESS_FLAG in response.body:
            logging.info(ImageSpider.LOGIN_SUCCESS_INFO)
            for page_url in self.__page_urls:
                yield response.follow(page_url, self.fn_parse_images_urls)
        else:
            logging.info(ImageSpider.LOGIN_FAILED_INFO)

    def fn_parse_images_urls(self, response):
        origin_image_urls = re.findall(self.__image_url_match_pattern, response.text)
        image_urls = list(set(origin_image_urls))
        for image_url in image_urls:
            yield response.follow(image_url, self.fn_retrieve_image)

    def fn_retrieve_image(self, response):
        logging.info(ImageSpider.SAVING_INFO % response.url)
        img = ScrapedImage(response.body)
        img.save(self.__save_dir, self.__filename_regex.sub(self.__file_rename_string, response.url).format(datetime.now()))
