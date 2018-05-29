[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://github.com/chxzqw/imagescraper/blob/master/LICENSE)

# Image Scraper

These scripts aims to do image scraping job from websites especially those which needs logins. Currently the program is still in experimental stage and has only been tested on certain websites. There is no guarantee that it performs well on other ones and you may get banned by using these scripts. Run the program at your own risk.

## Getting Started

### Prerequisites

At this time the program is written and tested by following python branch and packages:

Python 3.6.5  
Scrapy 1.5.0  
Pillow 5.1.0  
PyYAML 3.12  

For Linux please refer to relative documents for installation.

For Windows a Miniconda/Anaconda bundle is preferred and make sure it matches the above Python version.
If it unfortunately encounters a `Microsoft Visual C++ 14.0 is required` error, please consider installing `Unofficial Windows Binaries for Python Extension Packages` from <https://www.lfd.uci.edu/~gohlke/pythonlibs/> for desired packages.  
Reference: [Microsoft Visual C++ 14.0 is required (Unable to find vcvarsall.bat)](https://stackoverflow.com/questions/29846087/microsoft-visual-c-14-0-is-required-unable-to-find-vcvarsall-bat)

### Installing

Finish installing dependent libraries, create the project folder in which run  
`git clone `  

## Usage

Find the `etc/sample.conf.yaml`, copy and rename the file to `conf-name.conf.yaml` which is then opened with preferred text editor and alter the settings to meet your demand.  
In the project folder, run:
`scrapy crawl imagespider -a site=<conf-name>`

Options in <conf-name>.conf.yaml:
* `login_info`: usually includes login name and password, and some other required fields such like token, security question and answer ,etc.
* `page_urls`: urls of pages which holds the images need to be scraped.
* `image_url_match_pattern`: a regex string represents desired images' urls on the web pages.
* `save_dir`: desired save folder for scraped images and is able to contain python-like date time format, e.g. `{%Y%m%d}`
* `file_rename_pattern`: A regex string represents the file name part of the original image url which needs to be searched and renamed later.
* `file_rename_string`: A regex string used to rename the above file name. It supports python-like date time format as well, e.g. `{%Y%m%d}`

## Running the tests

In the project folder just run:  
`python -m unittest tests.test_suite_imagescraper`

## Versioning

`0.1.0`

## Remain issues

* lack of a proper scraping sandbox website as good example.

## Authors

* **Sid Chen** - *Initial work* - [chxzqw](https://github.com/chxzqw)

## License

MIT
