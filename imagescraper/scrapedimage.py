#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PIL import Image
from io import BytesIO

class ScrapedImage(object):

    def __init__(self, stream):
        self.__img = Image.open(BytesIO(stream))

    def save(self, save_dir, save_filename):
        self.__img.save(os.path.join(save_dir, save_filename))
